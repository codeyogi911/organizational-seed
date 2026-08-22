"""Open Knowledge Format bundle inventory, compilation, and validation.

The module owns the tolerant legacy-to-OKF scalar projection and delegates full
emitted-frontmatter parsing to the repository-pinned YAML dependency.
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import re
import shutil
import tempfile
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable

from treefiles import own_tree_files


PROFILE_BLOCK = re.compile(
    r"```json okf-profile\s*\n(?P<payload>.*?)\n```", re.DOTALL
)
TOP_LEVEL_FIELD = re.compile(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$")
OKF_STATUSES = {"draft", "stable", "deprecated"}
RESERVED_NAMES = {"index.md", "log.md"}
VALIDATION_LEVEL = "okf-profile-structural-v0"
YAML_VALIDATION_LEVEL = "okf-yaml-v0"
BLOCK_SCALAR_VALUES = {">", ">-", ">+", "|", "|-", "|+"}
YAML_LIST_ITEM = re.compile(r"^(?P<indent>\s*)-\s+(?P<value>.*?)(?P<newline>\r?\n)?$")
STRING_SCALAR_FIELDS = {"id", "state", "status", "type"}
OKF_STANDARD_FIELDS = {
    "attester",
    "computation",
    "description",
    "executor",
    "generated",
    "parameters",
    "resource",
    "runtime",
    "sources",
    "stale_after",
    "status",
    "tags",
    "title",
    "usage_window",
    "verified",
}
MARKDOWN_HEADING = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FENCE_OPEN = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
FENCE_CLOSE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,})[ \t]*$")
INDEX_ENTRY = re.compile(
    r"^(?:[ \t]*[-*+][ \t]+|[ \t]*\|).*?\[[^\]]+\]\([^)]+\)",
    re.MULTILINE,
)
LOG_ENTRY = re.compile(r"^[ \t]*[-*+][ \t]+\S", re.MULTILINE)


class KnowledgeBundleError(RuntimeError):
    """A profile, source, output, or bundle violates the public contract."""


@dataclass(frozen=True)
class ParsedConcept:
    """Resolved frontmatter and source positions for compiled-result consumers."""

    fields: dict[str, str] | None
    raw_fields: dict[str, str]
    field_lines: dict[str, int]
    body_start: int
    body: str


def read_utf8_exact(path: Path) -> str:
    """Read UTF-8 without universal-newline translation."""

    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write_utf8_exact(path: Path, text: str) -> None:
    """Write UTF-8 without platform newline translation."""

    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def target_diff_sha256(changes: Iterable[dict[str, Any]]) -> str:
    """Digest complete governed before/after bytes using Mainmind's contract.

    Paths sort by Unicode code point. Each complete file is reduced to its
    operation, path, before SHA-256 (or null), and after SHA-256. That list is
    encoded as compact UTF-8 JSON without a trailing newline and hashed once
    more. The field insertion order is part of the cross-runtime contract.
    """

    canonical = []
    paths = set()
    for change in changes:
        operation = change.get("operation")
        path = change.get("path")
        before = change.get("was")
        after = change.get("now")
        valid = (
            operation in {"create", "update"}
            and isinstance(path, str)
            and bool(path)
            and isinstance(after, str)
            and (
                (operation == "create" and before is None)
                or (operation == "update" and isinstance(before, str))
            )
        )
        if not valid:
            raise KnowledgeBundleError(
                "governed target diff requires complete create/update bytes"
            )
        if path in paths:
            raise KnowledgeBundleError(
                "governed target diff cannot contain a duplicate path"
            )
        paths.add(path)
        canonical.append(
            {
                "operation": operation,
                "path": path,
                "before_sha256": (
                    None
                    if before is None
                    else hashlib.sha256(before.encode("utf-8")).hexdigest()
                ),
                "after_sha256": hashlib.sha256(after.encode("utf-8")).hexdigest(),
            }
        )
    if not canonical:
        raise KnowledgeBundleError("governed target diff cannot be empty")
    canonical.sort(key=lambda item: item["path"])
    envelope = json.dumps(
        canonical,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(envelope).hexdigest()


def yaml_parser():
    try:
        import yaml
    except ImportError as exc:
        raise KnowledgeBundleError(
            "PyYAML is required for bundle validation; "
            "install tools/requirements.txt"
        ) from exc
    return yaml


def yaml_safe_load_unique(text: str):
    """Parse YAML safely while rejecting duplicate mapping keys at any depth."""

    yaml = yaml_parser()

    class UniqueKeySafeLoader(yaml.SafeLoader):
        pass

    def construct_unique_mapping(loader, node, deep=False):
        loader.flatten_mapping(node)
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            try:
                duplicate = key in mapping
            except TypeError as exc:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    "found an unhashable mapping key",
                    key_node.start_mark,
                ) from exc
            if duplicate:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key ({key!r})",
                    key_node.start_mark,
                )
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    UniqueKeySafeLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_unique_mapping,
    )
    return yaml.load(text, Loader=UniqueKeySafeLoader)


def yaml_has_anchor_or_alias(lines: Iterable[str]) -> bool:
    """Detect context-sensitive YAML constructs the line projector cannot edit."""

    yaml = yaml_parser()
    text = "".join(lines)
    token_types = (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)
    try:
        return any(isinstance(token, token_types) for token in yaml.scan(text))
    except yaml.YAMLError:
        # Invalid legacy scalars are repaired line by line. Continue scanning each
        # non-block line so an unrelated invalid line cannot hide an anchor.
        in_block_scalar = False
        for line in lines:
            match = TOP_LEVEL_FIELD.match(line.rstrip("\r\n"))
            if match:
                in_block_scalar = (
                    (match.group(2) or "").strip() in BLOCK_SCALAR_VALUES
                )
            if in_block_scalar:
                continue
            try:
                if any(
                    isinstance(token, token_types) for token in yaml.scan(line)
                ):
                    return True
            except yaml.YAMLError:
                continue
        return False


def visible_markdown_structure(text: str) -> str:
    """Remove fenced examples and HTML comments before structure checks."""

    kept: list[str] = []
    active_fence: str | None = None
    for line in text.splitlines():
        if active_fence is None:
            opening = FENCE_OPEN.match(line)
            if opening:
                fence = opening.group("fence")
                if fence[0] != "`" or "`" not in opening.group("info"):
                    active_fence = fence
                    kept.append("")
                    continue
            kept.append(line)
            continue
        closing = FENCE_CLOSE.match(line)
        if (
            closing
            and closing.group("fence")[0] == active_fence[0]
            and len(closing.group("fence")) >= len(active_fence)
        ):
            active_fence = None
        kept.append("")
    visible = "\n".join(kept)
    without_comments: list[str] = []
    cursor = 0
    while True:
        start = visible.find("<!--", cursor)
        if start < 0:
            without_comments.append(visible[cursor:])
            break
        without_comments.append(visible[cursor:start])
        end = visible.find("-->", start + len("<!--"))
        if end < 0:
            without_comments.append(
                "\n" * visible[start:].count("\n")
            )
            break
        comment = visible[start : end + len("-->")]
        without_comments.append("\n" * comment.count("\n"))
        cursor = end + len("-->")
    return "".join(without_comments)


def valid_index_structure(text: str) -> bool:
    """Require every index entry to belong to a non-empty H1 section."""

    sections: list[bool] = []
    active_section: int | None = None
    orphan_entry = False
    for line in text.splitlines():
        heading = MARKDOWN_HEADING.match(line)
        if heading and len(heading.group("marks")) == 1:
            sections.append(False)
            active_section = len(sections) - 1
            continue
        if INDEX_ENTRY.match(line):
            if active_section is None:
                orphan_entry = True
            else:
                sections[active_section] = True
    return bool(sections) and all(sections) and not orphan_entry


def valid_log_structure(text: str) -> bool:
    """Require a flat newest-first list whose entries belong to date groups."""

    dates: list[date] = []
    group_has_entry: list[bool] = []
    active_group: int | None = None
    invalid = False
    for line in text.splitlines():
        heading = MARKDOWN_HEADING.match(line)
        if heading:
            title = heading.group("title")
            if len(heading.group("marks")) == 2 and ISO_DATE.fullmatch(title):
                try:
                    parsed = date.fromisoformat(title)
                except ValueError:
                    invalid = True
                    active_group = None
                    continue
                dates.append(parsed)
                group_has_entry.append(False)
                active_group = len(dates) - 1
            else:
                if len(heading.group("marks")) == 2:
                    invalid = True
                active_group = None
            continue
        if LOG_ENTRY.match(line):
            if active_group is None:
                invalid = True
            else:
                group_has_entry[active_group] = True
    return (
        bool(dates)
        and all(group_has_entry)
        and dates == sorted(dates, reverse=True)
        and not invalid
    )


def yaml_safe_top_level_line(line: str) -> str:
    match = TOP_LEVEL_FIELD.match(line.rstrip("\r\n"))
    if not match or not (match.group(2) or "").strip():
        return line if line.endswith(("\n", "\r")) else line + "\n"

    key = match.group(1)
    raw_value = match.group(2) or ""
    if raw_value.strip() in BLOCK_SCALAR_VALUES:
        return line if line.endswith(("\n", "\r")) else line + "\n"
    expected_value = scalar(raw_value)
    yaml = yaml_parser()
    try:
        parsed = yaml.safe_load(f"{key}: {raw_value}\n")
    except yaml.YAMLError:
        parsed = None

    parsed_value = parsed.get(key) if isinstance(parsed, dict) else None
    loses_scalar_data = (
        isinstance(parsed_value, str) and parsed_value != expected_value
    ) or (parsed_value is None and raw_value.lstrip().startswith("#")) or (
        key in STRING_SCALAR_FIELDS and not isinstance(parsed_value, str)
    )
    if parsed is None or loses_scalar_data:
        return f"{key}: {json.dumps(expected_value, ensure_ascii=False)}\n"
    return line if line.endswith(("\n", "\r")) else line + "\n"


def yaml_safe_list_item(line: str) -> str:
    match = YAML_LIST_ITEM.match(line)
    if not match:
        return line if line.endswith(("\n", "\r")) else line + "\n"
    raw_value = match.group("value")
    expected_value = scalar(raw_value)
    yaml = yaml_parser()
    try:
        parsed = yaml.safe_load(f"- {raw_value}\n")
    except yaml.YAMLError:
        parsed = None
    parsed_value = parsed[0] if isinstance(parsed, list) and parsed else None
    loses_scalar_data = (
        isinstance(parsed_value, str) and parsed_value != expected_value
    ) or (parsed_value is None and raw_value.lstrip().startswith("#"))
    if parsed is None or loses_scalar_data:
        return (
            f"{match.group('indent')}- "
            f"{json.dumps(expected_value, ensure_ascii=False)}\n"
        )
    return line if line.endswith(("\n", "\r")) else line + "\n"


@dataclass(frozen=True)
class MarkdownDocument:
    frontmatter_lines: tuple[str, ...] | None
    fields: dict[str, str]
    body: str


@dataclass(frozen=True)
class RenderedConcept:
    text: str
    normalized_scalar_lines: int
    field_dispositions: tuple[str, ...]


def sha256_bytes(value: bytes) -> str:
    return f"sha256:{hashlib.sha256(value).hexdigest()}"


def scalar(value: str) -> str:
    stripped = value.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] == '"':
        try:
            parsed = json.loads(stripped)
        except json.JSONDecodeError:
            return stripped[1:-1]
        return parsed if isinstance(parsed, str) else stripped
    if len(stripped) >= 2 and stripped[0] == stripped[-1] == "'":
        return stripped[1:-1].replace("''", "'")
    return stripped


def okf_datetime(value: Any) -> bool:
    if isinstance(value, datetime):
        return value.tzinfo is not None and value.utcoffset() is not None
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() is not None


def okf_actor(value: Any) -> bool:
    if (
        not isinstance(value, str)
        or not value.strip()
        or value != value.strip()
    ):
        return False
    return (
        (value.startswith("human:") and len(value) > len("human:"))
        or (value.startswith("process:") and len(value) > len("process:"))
        or (
            "/" in value
            and all(
                part and part == part.strip()
                for part in value.split("/", 1)
            )
        )
    )


def okf_usage_window(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and okf_datetime(value.get("from"))
        and okf_datetime(value.get("to"))
    )


def okf_source_entries(value: Any) -> bool:
    if not isinstance(value, list):
        return False
    for entry in value:
        if (
            not isinstance(entry, dict)
            or not isinstance(entry.get("resource"), str)
            or not entry["resource"].strip()
        ):
            return False
        for key in ("id", "title"):
            if key in entry and (
                not isinstance(entry[key], str) or not entry[key].strip()
            ):
                return False
        if "author" in entry and not (
            okf_actor(entry["author"])
            or (
                isinstance(entry["author"], str)
                and entry["author"] == entry["author"].strip()
                and entry["author"].startswith("team:")
                and len(entry["author"]) > len("team:")
            )
        ):
            return False
        if "usage_count" in entry and (
            not isinstance(entry["usage_count"], int)
            or isinstance(entry["usage_count"], bool)
            or entry["usage_count"] < 0
        ):
            return False
        if "last_modified" in entry and not okf_datetime(
            entry["last_modified"]
        ):
            return False
        if "usage_window" in entry and not okf_usage_window(
            entry["usage_window"]
        ):
            return False
    return True


def okf_verification_events(value: Any) -> bool:
    events = value if isinstance(value, list) else [value]
    return bool(events) and all(
        isinstance(event, dict)
        and okf_actor(event.get("by"))
        and okf_datetime(event.get("at"))
        for event in events
    )


def okf_standard_field_valid(key: str, value: Any) -> bool:
    """Check the pinned v0.2 shape for a standardized optional field."""

    if key in {"title", "description", "resource", "runtime", "computation"}:
        return isinstance(value, str) and bool(value.strip())
    if key == "tags":
        return isinstance(value, list) and all(
            isinstance(item, str) and bool(item.strip()) for item in value
        )
    if key == "sources":
        return okf_source_entries(value)
    if key == "usage_window":
        return okf_usage_window(value)
    if key == "generated":
        return (
            isinstance(value, dict)
            and okf_actor(value.get("by"))
            and ("at" not in value or okf_datetime(value.get("at")))
        )
    if key == "verified":
        return okf_verification_events(value)
    if key == "stale_after":
        return okf_datetime(value)
    if key == "parameters":
        return isinstance(value, list) and all(
            isinstance(parameter, dict)
            and isinstance(parameter.get("name"), str)
            and bool(parameter["name"].strip())
            and isinstance(parameter.get("type"), str)
            and bool(parameter["type"].strip())
            and isinstance(parameter.get("required"), bool)
            for parameter in value
        )
    if key == "executor":
        return (
            isinstance(value, dict)
            and isinstance(value.get("resource"), str)
            and bool(value["resource"].strip())
            and (
                "receipt" not in value
                or (
                    isinstance(value["receipt"], list)
                    and all(
                        isinstance(field, str) and bool(field.strip())
                        for field in value["receipt"]
                    )
                )
            )
        )
    if key == "attester":
        return (
            isinstance(value, dict)
            and isinstance(value.get("resource"), str)
            and bool(value["resource"].strip())
        )
    return True


def parse_markdown(text: str) -> MarkdownDocument:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        return MarkdownDocument(None, {}, text)

    close_at: int | None = None
    fields: dict[str, str] = {}
    for index, line in enumerate(lines[1:], start=1):
        if line.rstrip("\r\n") == "---":
            close_at = index
            break
        match = TOP_LEVEL_FIELD.match(line.rstrip("\r\n"))
        if match:
            fields[match.group(1)] = scalar(match.group(2) or "")
    if close_at is None:
        raise KnowledgeBundleError("unclosed YAML frontmatter")
    return MarkdownDocument(
        tuple(lines[1:close_at]), fields, "".join(lines[close_at + 1 :])
    )


def resolved_frontmatter(document: MarkdownDocument) -> dict[Any, Any] | None:
    if document.frontmatter_lines is None:
        return None
    yaml = yaml_parser()
    try:
        parsed = yaml_safe_load_unique("".join(document.frontmatter_lines))
    except yaml.YAMLError:
        return None
    return parsed if isinstance(parsed, dict) else None


def _consumer_value(value: Any) -> str:
    """Render resolved YAML values for existing scalar-oriented consumers."""

    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, list):
        return ", ".join(_consumer_value(item) for item in value)
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def parse_concept(text: str) -> ParsedConcept:
    """Resolve one canonical concept through the bundle's full YAML parser.

    Doctor, graph and index machinery consume this seam instead of maintaining
    their own interpretations of quoted, nested or typed YAML values.
    """

    document = parse_markdown(text)
    if document.frontmatter_lines is None:
        return ParsedConcept(None, {}, {}, 0, document.body)
    resolved = resolved_frontmatter(document)
    if resolved is None:
        raise KnowledgeBundleError("invalid YAML frontmatter")
    yaml = yaml_parser()
    node = yaml.compose("".join(document.frontmatter_lines), Loader=yaml.SafeLoader)
    scalar_values: dict[str, str] = {}
    raw_fields: dict[str, str] = {}
    if isinstance(node, yaml.MappingNode):
        yaml_text = "".join(document.frontmatter_lines)
        for key_node, value_node in node.value:
            if isinstance(key_node, yaml.ScalarNode):
                raw_fields[key_node.value] = yaml_text[
                    value_node.start_mark.index : value_node.end_mark.index
                ]
                if isinstance(value_node, yaml.ScalarNode):
                    scalar_values[key_node.value] = value_node.value
    fields = {
        str(key): scalar_values.get(str(key), _consumer_value(value))
        for key, value in resolved.items()
        if isinstance(key, str)
    }
    field_lines: dict[str, int] = {}
    lines = text.splitlines()
    close_at = 0
    for index, line in enumerate(lines[1:], start=2):
        if line == "---":
            close_at = index
            break
        match = TOP_LEVEL_FIELD.match(line)
        if match:
            field_lines[match.group(1)] = index
    return ParsedConcept(fields, raw_fields, field_lines, close_at, document.body)


def resolved_repaired_frontmatter(
    document: MarkdownDocument,
) -> dict[Any, Any] | None:
    """Resolve a legacy-invalid document after the projector's scalar repairs."""

    if document.frontmatter_lines is None:
        return None
    repaired: list[str] = []
    in_block_scalar = False
    for line in document.frontmatter_lines:
        match = TOP_LEVEL_FIELD.match(line.rstrip("\r\n"))
        if match:
            in_block_scalar = (
                (match.group(2) or "").strip() in BLOCK_SCALAR_VALUES
            )
            repaired.append(yaml_safe_top_level_line(line))
        elif in_block_scalar:
            repaired.append(
                line if line.endswith(("\n", "\r")) else line + "\n"
            )
        else:
            repaired.append(yaml_safe_list_item(line))
    yaml = yaml_parser()
    try:
        parsed = yaml_safe_load_unique("".join(repaired))
    except yaml.YAMLError:
        return None
    return parsed if isinstance(parsed, dict) else None


def load_profile(path: Path) -> dict[str, Any]:
    try:
        text = read_utf8_exact(path)
    except OSError as exc:
        raise KnowledgeBundleError(f"cannot read profile {path}: {exc}") from exc
    match = PROFILE_BLOCK.search(text)
    if not match:
        raise KnowledgeBundleError(f"{path}: missing `json okf-profile` block")
    try:
        profile = json.loads(match.group("payload"))
    except json.JSONDecodeError as exc:
        raise KnowledgeBundleError(f"{path}: invalid profile JSON: {exc}") from exc
    if not isinstance(profile, dict):
        raise KnowledgeBundleError("profile must be an object")
    required = {
        "profile",
        "okf_version",
        "upstream_commit",
        "bundle_root",
        "source",
        "type_rules",
        "lifecycle",
    }
    missing = sorted(required - profile.keys())
    if missing:
        raise KnowledgeBundleError(f"{path}: profile missing {', '.join(missing)}")
    if profile["okf_version"] != "0.2":
        raise KnowledgeBundleError(f"{path}: only OKF v0.2 is supported")
    if not re.fullmatch(r"[0-9a-f]{40}", str(profile["upstream_commit"])):
        raise KnowledgeBundleError("profile upstream_commit must be a full Git SHA")
    if not isinstance(profile["profile"], str) or not profile["profile"].strip():
        raise KnowledgeBundleError("profile name must be a non-empty string")
    if "bundle_title" in profile and (
        not isinstance(profile["bundle_title"], str)
        or not profile["bundle_title"].strip()
    ):
        raise KnowledgeBundleError("profile bundle_title must be a non-empty string")
    bundle_root = profile["bundle_root"]
    if (
        not isinstance(bundle_root, str)
        or not bundle_root
        or bundle_root in {".", ".."}
        or Path(bundle_root).name != bundle_root
    ):
        raise KnowledgeBundleError("profile bundle_root must be one directory name")
    source = profile["source"]
    if not isinstance(source, dict):
        raise KnowledgeBundleError("profile source must be an object")
    source_root = source.get("root", ".")
    if (
        not isinstance(source_root, str)
        or not source_root
        or Path(source_root).is_absolute()
        or ".." in Path(source_root).parts
    ):
        raise KnowledgeBundleError(
            "profile source.root must be a repository-relative directory"
        )
    for field in ("files", "directories"):
        values = source.get(field, [])
        if not isinstance(values, list) or not all(
            isinstance(value, str) and value for value in values
        ):
            raise KnowledgeBundleError(f"profile source.{field} must be a list of paths")
    rules = profile["type_rules"]
    if not isinstance(rules, list):
        raise KnowledgeBundleError("profile type_rules must be a list")
    for index, rule in enumerate(rules):
        if not isinstance(rule, dict) or not all(
            isinstance(rule.get(field), str) and rule[field]
            for field in ("glob", "type")
        ):
            raise KnowledgeBundleError(
                f"profile type_rules[{index}] must carry non-empty glob and type"
            )
    identity_overrides = profile.get("identity_overrides", {})
    if not isinstance(identity_overrides, dict) or not all(
        isinstance(path, str)
        and path
        and isinstance(identity, str)
        and identity
        for path, identity in identity_overrides.items()
    ):
        raise KnowledgeBundleError(
            "profile identity_overrides must map paths to non-empty ids"
        )
    incompatible_field_overrides = profile.get(
        "incompatible_field_overrides", {}
    )
    if not isinstance(incompatible_field_overrides, dict) or not all(
        isinstance(source_field, str)
        and source_field in OKF_STANDARD_FIELDS
        and source_field != "status"
        and isinstance(extension_field, str)
        and bool(extension_field)
        and extension_field not in OKF_STANDARD_FIELDS
        and extension_field not in {"id", "kind", "state", "type"}
        for source_field, extension_field in incompatible_field_overrides.items()
    ):
        raise KnowledgeBundleError(
            "profile incompatible_field_overrides must map optional OKF fields "
            "to non-standard extension fields"
        )
    if len(set(incompatible_field_overrides.values())) != len(
        incompatible_field_overrides
    ):
        raise KnowledgeBundleError(
            "profile incompatible_field_overrides targets must be unique"
        )
    lifecycle = profile["lifecycle"]
    if not isinstance(lifecycle, dict):
        raise KnowledgeBundleError("profile lifecycle must be an object")
    for field in (
        "draft_types",
        "draft_state_prefixes",
        "deprecated_state_prefixes",
    ):
        values = lifecycle.get(field)
        if not isinstance(values, list) or not all(
            isinstance(value, str) and value for value in values
        ):
            raise KnowledgeBundleError(f"profile lifecycle.{field} must be a list of strings")
    if lifecycle.get("default") not in OKF_STATUSES:
        raise KnowledgeBundleError("profile lifecycle.default must be an OKF status")
    return profile


def configured_source_root(root: Path, profile: dict[str, Any]) -> Path:
    """Resolve the profile's bundle content root inside its repository."""

    repository = root.resolve()
    source_root = profile["source"].get("root", ".")
    configured = (repository / source_root).resolve()
    if configured != repository and repository not in configured.parents:
        raise KnowledgeBundleError("configured source root escapes repository")
    return configured


def source_files(root: Path, profile: dict[str, Any]) -> tuple[list[Path], list[str]]:
    root = root.resolve()
    base = configured_source_root(root, profile)
    configured = profile["source"]
    paths: dict[str, Path] = {}
    errors: list[str] = []
    if not base.is_dir():
        return [], [f"missing configured source root: {configured.get('root', '.')}"]
    for relative in configured.get("files", []):
        path = (base / relative).resolve()
        if path != base and base not in path.parents:
            errors.append(f"configured source escapes repository: {relative}")
            continue
        if not path.is_file():
            errors.append(f"missing configured file: {relative}")
            continue
        paths[path.relative_to(base).as_posix()] = path
    for relative in configured.get("directories", []):
        directory = (base / relative).resolve()
        if directory != base and base not in directory.parents:
            errors.append(f"configured source escapes repository: {relative}")
            continue
        if not directory.is_dir():
            errors.append(f"missing configured directory: {relative}")
            continue
        for path in own_tree_files(directory):
            rel = path.relative_to(base).as_posix()
            resolved = path.resolve()
            if resolved != base and base not in resolved.parents:
                errors.append(f"source file escapes repository: {rel}")
                continue
            paths[rel] = path
    return [paths[key] for key in sorted(paths)], errors


def mapped_type(relative: str, document: MarkdownDocument, profile: dict[str, Any]) -> tuple[str | None, str]:
    kind = document.fields.get("kind")
    existing_type = document.fields.get("type")
    if kind and existing_type:
        return None, "both kind and type are present"
    if kind:
        return kind, "kind"
    if existing_type:
        return existing_type, "type"
    for rule in profile["type_rules"]:
        if fnmatch.fnmatchcase(relative, rule["glob"]):
            return scalar(rule["type"]), "rule"
    return None, "no kind, type, or matching type rule"


def inventory(root: Path, profile: dict[str, Any]) -> dict[str, Any]:
    files, source_errors = source_files(root, profile)
    base = configured_source_root(root, profile)
    concepts = 0
    resources = 0
    mapped_kind = 0
    existing_type = 0
    synthesized_type = 0
    reserved = 0
    reserved_metadata = 0
    frontmatter_documents = 0
    identity_fields = 0
    operational_state_fields = 0
    extension_field_occurrences = 0
    identity_overrides_applied = 0
    unmapped: list[dict[str, str]] = []

    def tally_identity_override(
        relative: str, document: MarkdownDocument
    ) -> None:
        nonlocal identity_overrides_applied
        if relative not in profile.get("identity_overrides", {}):
            return
        if document.frontmatter_lines is None or not document.fields.get("id"):
            unmapped.append(
                {
                    "path": relative,
                    "reason": (
                        "identity override target does not emit a concept "
                        "with an existing id"
                    ),
                }
            )
            return
        identity_overrides_applied += 1

    def tally_fields(document: MarkdownDocument) -> None:
        nonlocal frontmatter_documents
        nonlocal identity_fields
        nonlocal operational_state_fields
        nonlocal extension_field_occurrences
        if document.frontmatter_lines is None:
            return
        frontmatter_documents += 1
        identity_fields += int("id" in document.fields)
        operational_state_fields += int("status" in document.fields)
        extension_field_occurrences += len(
            set(document.fields) - {"kind", "type", "status"}
        )

    for path in files:
        relative = path.relative_to(base).as_posix()
        if path.suffix.lower() != ".md":
            resources += 1
            continue
        if path.name in RESERVED_NAMES:
            reserved += 1
            try:
                document = parse_markdown(read_utf8_exact(path))
            except (OSError, UnicodeDecodeError, KnowledgeBundleError) as exc:
                unmapped.append({"path": relative, "reason": str(exc)})
                continue
            tally_fields(document)
            tally_identity_override(relative, document)
            if document.frontmatter_lines is not None:
                reserved_metadata += 1
                type_name, source = mapped_type(relative, document, profile)
                if not type_name:
                    unmapped.append({"path": relative, "reason": source})
                elif source == "kind":
                    mapped_kind += 1
                elif source == "type":
                    existing_type += 1
                else:
                    synthesized_type += 1
            continue
        concepts += 1
        try:
            document = parse_markdown(read_utf8_exact(path))
        except (OSError, UnicodeDecodeError, KnowledgeBundleError) as exc:
            unmapped.append({"path": relative, "reason": str(exc)})
            continue
        tally_fields(document)
        tally_identity_override(relative, document)
        type_name, source = mapped_type(relative, document, profile)
        if not type_name:
            unmapped.append({"path": relative, "reason": source})
        elif source == "kind":
            mapped_kind += 1
        elif source == "type":
            existing_type += 1
        else:
            synthesized_type += 1

    unmapped.extend({"path": "", "reason": error} for error in source_errors)
    configured_overrides = set(profile.get("identity_overrides", {}))
    markdown_source_relatives = {
        path.relative_to(base).as_posix()
        for path in files
        if path.suffix.lower() == ".md"
    }
    for relative in sorted(configured_overrides - markdown_source_relatives):
        unmapped.append(
            {
                "path": relative,
                "reason": (
                    "identity override does not match configured Markdown source"
                ),
            }
        )
    return {
        "ok": not unmapped,
        "validation_level": VALIDATION_LEVEL,
        "yaml_conformance": "not-checked",
        "profile": profile["profile"],
        "okf_version": profile["okf_version"],
        "upstream_commit": profile["upstream_commit"],
        "concepts": concepts,
        "resources": resources,
        "reserved": reserved,
        "reserved_metadata": reserved_metadata,
        "projected_concepts": concepts + reserved_metadata,
        "frontmatter_documents": frontmatter_documents,
        "identity_fields": identity_fields,
        "operational_state_fields": operational_state_fields,
        "extension_field_occurrences": extension_field_occurrences,
        "identity_overrides_applied": identity_overrides_applied,
        "mapped_kind": mapped_kind,
        "existing_type": existing_type,
        "synthesized_type": synthesized_type,
        "unmapped": unmapped,
    }


def lifecycle_status(type_name: str, state: str | None, profile: dict[str, Any]) -> str:
    lifecycle = profile["lifecycle"]
    lowered_type = type_name.lower()
    lowered_state = (state or "").lower()
    if lowered_type in {value.lower() for value in lifecycle["draft_types"]}:
        return "draft"
    if any(lowered_state.startswith(prefix.lower()) for prefix in lifecycle["draft_state_prefixes"]):
        return "draft"
    if any(
        lowered_state.startswith(prefix.lower())
        for prefix in lifecycle["deprecated_state_prefixes"]
    ):
        return "deprecated"
    default = lifecycle["default"]
    if default not in OKF_STATUSES:
        raise KnowledgeBundleError(f"invalid lifecycle default: {default}")
    return default


def incompatible_field_target(
    key: str,
    value: Any,
    source_fields: dict[Any, Any],
    profile: dict[str, Any],
) -> str | None:
    target = profile.get("incompatible_field_overrides", {}).get(key)
    if not target or okf_standard_field_valid(key, value):
        return None
    if target in source_fields:
        raise KnowledgeBundleError(
            f"cannot preserve incompatible {key}: extension target {target} exists"
        )
    return target


def render_concept(
    relative: str, document: MarkdownDocument, profile: dict[str, Any]
) -> RenderedConcept:
    type_name, reason = mapped_type(relative, document, profile)
    if not type_name:
        raise KnowledgeBundleError(f"{relative}: {reason}")
    if "state" in document.fields:
        raise KnowledgeBundleError(
            f"{relative}: source already carries state; status-to-state mapping would duplicate it"
        )
    if document.frontmatter_lines is not None and yaml_has_anchor_or_alias(
        document.frontmatter_lines
    ):
        raise KnowledgeBundleError(
            f"{relative}: source YAML anchors and aliases require "
            "document-context projection"
        )
    resolved_source = resolved_frontmatter(document)
    disposition_source = resolved_source or resolved_repaired_frontmatter(document)
    state = document.fields.get("status")
    okf_status = lifecycle_status(type_name, state, profile)

    rendered: list[str] = ["---\n"]
    emitted_type = False
    emitted_state = False
    in_block_scalar = False
    normalized_scalar_lines = 0
    field_dispositions: list[str] = []
    identity_override = profile.get("identity_overrides", {}).get(relative)
    if identity_override and "id" not in document.fields:
        raise KnowledgeBundleError(
            f"{relative}: identity override requires an existing id"
        )
    if document.frontmatter_lines is not None:
        for line in document.frontmatter_lines:
            match = TOP_LEVEL_FIELD.match(line.rstrip("\r\n"))
            key = match.group(1) if match else None
            if match:
                in_block_scalar = (match.group(2) or "").strip() in BLOCK_SCALAR_VALUES
            source_value = (
                disposition_source.get(key)
                if key is not None and disposition_source is not None
                else document.fields.get(key or "")
            )
            field_target = (
                incompatible_field_target(
                    key,
                    source_value,
                    disposition_source or document.fields,
                    profile,
                )
                if key is not None
                else None
            )
            if key == "kind":
                rendered.append(yaml_safe_top_level_line(f"type: {type_name}\n"))
                emitted_type = True
            elif key == "type":
                normalized = yaml_safe_top_level_line(line)
                rendered.append(normalized)
                original = line if line.endswith(("\n", "\r")) else line + "\n"
                normalized_scalar_lines += int(normalized != original)
                emitted_type = True
            elif key == "status":
                normalized = yaml_safe_top_level_line(
                    f"state: {match.group(2) or ''}\n"
                )
                rendered.append(normalized)
                normalized_scalar_lines += int(
                    normalized != f"state: {match.group(2) or ''}\n"
                )
                emitted_state = True
            elif key == "id" and identity_override:
                rendered.append(f"id: {json.dumps(identity_override)}\n")
            elif field_target:
                renamed = line.replace(f"{key}:", f"{field_target}:", 1)
                normalized = yaml_safe_top_level_line(renamed)
                rendered.append(normalized)
                original = (
                    renamed
                    if renamed.endswith(("\n", "\r"))
                    else renamed + "\n"
                )
                normalized_scalar_lines += int(normalized != original)
                field_dispositions.append(f"{key}->{field_target}")
            elif in_block_scalar:
                rendered.append(line if line.endswith(("\n", "\r")) else line + "\n")
            elif not match:
                if resolved_source is not None:
                    rendered.append(
                        line if line.endswith(("\n", "\r")) else line + "\n"
                    )
                else:
                    normalized = yaml_safe_list_item(line)
                    rendered.append(normalized)
                    original = (
                        line if line.endswith(("\n", "\r")) else line + "\n"
                    )
                    normalized_scalar_lines += int(normalized != original)
            else:
                original = line if line.endswith(("\n", "\r")) else line + "\n"
                resolved_value = (
                    resolved_source.get(key) if resolved_source is not None else None
                )
                if (
                    key not in STRING_SCALAR_FIELDS
                    and isinstance(resolved_value, (dict, list, set))
                ):
                    rendered.append(original)
                else:
                    normalized = yaml_safe_top_level_line(line)
                    rendered.append(normalized)
                    normalized_scalar_lines += int(normalized != original)
    if not emitted_type:
        rendered.append(yaml_safe_top_level_line(f"type: {type_name}\n"))
    if state is not None and not emitted_state:
        normalized = yaml_safe_top_level_line(f"state: {state}\n")
        rendered.append(normalized)
        normalized_scalar_lines += int(normalized != f"state: {state}\n")
    rendered.append(f"status: {okf_status}\n")
    rendered.append("---\n")
    rendered.append(document.body)
    return RenderedConcept(
        "".join(rendered), normalized_scalar_lines, tuple(field_dispositions)
    )


def expected_fields(
    document: MarkdownDocument,
    type_name: str,
    okf_status: str,
    relative: str,
    profile: dict[str, Any],
) -> dict[str, str]:
    expected = dict(document.fields)
    for key, value in tuple(expected.items()):
        target = incompatible_field_target(key, value, expected, profile)
        if target:
            expected[target] = expected.pop(key)
    expected.pop("kind", None)
    expected["type"] = type_name
    state = expected.pop("status", None)
    if state is not None:
        expected["state"] = state
    expected["status"] = okf_status
    identity_override = profile.get("identity_overrides", {}).get(relative)
    if identity_override:
        expected["id"] = identity_override
    return expected


def expected_resolved_fields(
    document: MarkdownDocument,
    type_name: str,
    okf_status: str,
    relative: str,
    profile: dict[str, Any],
) -> dict[Any, Any] | None:
    expected = resolved_frontmatter(document) or resolved_repaired_frontmatter(
        document
    )
    if expected is None:
        return None
    expected = dict(expected)
    for key, value in tuple(expected.items()):
        target = incompatible_field_target(key, value, expected, profile)
        if target:
            expected[target] = expected.pop(key)
    for line in document.frontmatter_lines or ():
        match = TOP_LEVEL_FIELD.match(line.rstrip("\r\n"))
        if not match or match.group(1) in {"kind", "status"}:
            continue
        key = profile.get("incompatible_field_overrides", {}).get(
            match.group(1), match.group(1)
        )
        if key not in expected:
            key = match.group(1)
        if (
            key not in STRING_SCALAR_FIELDS
            and isinstance(expected.get(key), (dict, list, set))
        ):
            continue
        normalized = yaml_safe_top_level_line(line)
        original = line if line.endswith(("\n", "\r")) else line + "\n"
        if normalized == original:
            continue
        parsed_line = yaml_safe_load_unique(normalized)
        if isinstance(parsed_line, dict):
            expected[key] = parsed_line[match.group(1)]
    expected.pop("kind", None)
    expected["type"] = type_name
    state = document.fields.get("status")
    expected.pop("status", None)
    if state is not None:
        expected["state"] = state
    expected["status"] = okf_status
    identity_override = profile.get("identity_overrides", {}).get(relative)
    if identity_override:
        expected["id"] = identity_override
    return expected


def companion_name(name: str) -> str:
    return "_index.md" if name == "index.md" else "_log.md"


def companion_document(source_name: str, document: MarkdownDocument) -> MarkdownDocument:
    body = (
        f"\n# {source_name} metadata\n\n"
        f"Metadata preserved from [{source_name}]({source_name}) so the reserved "
        "OKF file remains frontmatter-free.\n"
    )
    return MarkdownDocument(document.frontmatter_lines, document.fields, body)


def root_index(profile: dict[str, Any], source_paths: Iterable[Path], root: Path) -> str:
    top_level: set[str] = set()
    for path in source_paths:
        relative = path.relative_to(root)
        top_level.add(relative.parts[0])
    lines = [
        "---\n",
        f"okf_version: {json.dumps(profile['okf_version'])}\n",
        "---\n",
        "\n",
    ]
    bundle_title = profile.get("bundle_title", "Open Knowledge Format").strip()
    lines.extend([f"# {bundle_title} knowledge bundle\n", "\n"])
    for name in sorted(top_level):
        target = f"{name}/" if (root / name).is_dir() else name
        lines.append(f"- [{name}]({target})\n")
    return "".join(lines)


def compile_bundle(root: Path, output: Path, profile: dict[str, Any]) -> dict[str, Any]:
    root = root.resolve()
    base = configured_source_root(root, profile)
    output = output.resolve()
    if output.name != profile["bundle_root"]:
        raise KnowledgeBundleError(
            f"shadow output name must match bundle_root: {profile['bundle_root']}"
        )
    if output == root or root in output.parents:
        raise KnowledgeBundleError("shadow output must be outside the source repository")
    if output.exists():
        raise KnowledgeBundleError(f"shadow output already exists: {output}")

    report = inventory(root, profile)
    if not report["ok"]:
        raise KnowledgeBundleError(
            f"source inventory has {len(report['unmapped'])} unmapped item(s)"
        )
    files, source_errors = source_files(root, profile)
    if source_errors:
        raise KnowledgeBundleError("; ".join(source_errors))

    output.parent.mkdir(parents=True, exist_ok=True)
    body_mismatches: list[str] = []
    resource_mismatches: list[str] = []
    frontmatter_mismatches: list[str] = []
    normalized_scalar_lines = 0
    normalized_documents = 0
    field_dispositions: dict[str, int] = {}
    with tempfile.TemporaryDirectory(prefix="okf-shadow-", dir=output.parent) as tmp:
        staging = Path(tmp)
        for source in files:
            relative = source.relative_to(base)
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.suffix.lower() != ".md":
                shutil.copyfile(source, target)
                if sha256_bytes(source.read_bytes()) != sha256_bytes(target.read_bytes()):
                    resource_mismatches.append(relative.as_posix())
                continue

            text = read_utf8_exact(source)
            document = parse_markdown(text)
            if source.name in RESERVED_NAMES:
                rendered = document.body if document.frontmatter_lines is not None else text
                write_utf8_exact(target, rendered)
                target_body = parse_markdown(read_utf8_exact(target)).body
                if document.body.encode("utf-8") != target_body.encode("utf-8"):
                    body_mismatches.append(relative.as_posix())
                if document.frontmatter_lines is not None:
                    metadata_target = target.with_name(companion_name(source.name))
                    if metadata_target.exists():
                        raise KnowledgeBundleError(
                            f"{relative}: metadata companion collides with "
                            f"{metadata_target.relative_to(staging).as_posix()}"
                        )
                    type_name, reason = mapped_type(relative.as_posix(), document, profile)
                    if not type_name:
                        raise KnowledgeBundleError(f"{relative}: {reason}")
                    okf_status = lifecycle_status(
                        type_name, document.fields.get("status"), profile
                    )
                    rendered_concept = render_concept(
                        relative.as_posix(),
                        companion_document(source.name, document),
                        profile,
                    )
                    write_utf8_exact(metadata_target, rendered_concept.text)
                    normalized_scalar_lines += rendered_concept.normalized_scalar_lines
                    normalized_documents += int(
                        rendered_concept.normalized_scalar_lines > 0
                    )
                    for disposition in rendered_concept.field_dispositions:
                        field_dispositions[disposition] = (
                            field_dispositions.get(disposition, 0) + 1
                        )
                    metadata_document = parse_markdown(
                        read_utf8_exact(metadata_target)
                    )
                    resolved_expected = expected_resolved_fields(
                        document, type_name, okf_status, relative.as_posix(), profile
                    )
                    resolved_actual = resolved_frontmatter(metadata_document)
                    if (
                        resolved_expected is not None
                        and resolved_actual != resolved_expected
                    ) or (
                        resolved_expected is None
                        and metadata_document.fields
                        != expected_fields(
                            document,
                            type_name,
                            okf_status,
                            relative.as_posix(),
                            profile,
                        )
                    ):
                        frontmatter_mismatches.append(relative.as_posix())
                continue
            else:
                resolved_source = resolved_frontmatter(document)
                canonical_source = (
                    "kind" not in document.fields
                    and isinstance(resolved_source, dict)
                    and isinstance(resolved_source.get("type"), str)
                    and bool(resolved_source["type"].strip())
                    and resolved_source.get("status") in OKF_STATUSES
                )
                rendered_concept = (
                    RenderedConcept(text, 0, ())
                    if canonical_source
                    else render_concept(relative.as_posix(), document, profile)
                )
                rendered = rendered_concept.text
                normalized_scalar_lines += rendered_concept.normalized_scalar_lines
                normalized_documents += int(rendered_concept.normalized_scalar_lines > 0)
                for disposition in rendered_concept.field_dispositions:
                    field_dispositions[disposition] = (
                        field_dispositions.get(disposition, 0) + 1
                    )
            write_utf8_exact(target, rendered)
            target_document = parse_markdown(read_utf8_exact(target))
            target_body = target_document.body
            if document.body.encode("utf-8") != target_body.encode("utf-8"):
                body_mismatches.append(relative.as_posix())
            type_name, reason = mapped_type(relative.as_posix(), document, profile)
            if not type_name:
                raise KnowledgeBundleError(f"{relative}: {reason}")
            okf_status = lifecycle_status(type_name, document.fields.get("status"), profile)
            resolved_actual = resolved_frontmatter(target_document)
            if canonical_source:
                resolved_expected = resolved_frontmatter(document)
                if (
                    resolved_expected is not None
                    and resolved_actual != resolved_expected
                ) or (
                    resolved_expected is None
                    and target_document.fields != document.fields
                ):
                    frontmatter_mismatches.append(relative.as_posix())
            else:
                resolved_expected = expected_resolved_fields(
                    document, type_name, okf_status, relative.as_posix(), profile
                )
                if (
                    resolved_expected is not None
                    and resolved_actual != resolved_expected
                ) or (
                    resolved_expected is None
                    and target_document.fields
                    != expected_fields(
                        document,
                        type_name,
                        okf_status,
                        relative.as_posix(),
                        profile,
                    )
                ):
                    frontmatter_mismatches.append(relative.as_posix())

        write_utf8_exact(staging / "index.md", root_index(profile, files, base))
        if body_mismatches or resource_mismatches or frontmatter_mismatches:
            mismatch_summary = "; ".join(
                f"{label}: {', '.join(paths)}"
                for label, paths in (
                    ("body", body_mismatches),
                    ("resource", resource_mismatches),
                    ("frontmatter", frontmatter_mismatches),
                )
                if paths
            )
            raise KnowledgeBundleError(
                "compiled bundle failed equivalence: " + mismatch_summary
            )
        validation = validate_bundle(staging)
        if not validation["ok"]:
            finding_summary = "; ".join(
                f"{finding['path']} [{finding['code']}]"
                for finding in validation["findings"]
            )
            raise KnowledgeBundleError(
                "compiled bundle validation failed: " + finding_summary
            )
        staging.rename(output)

    return {
        **report,
        "ok": not body_mismatches and not resource_mismatches,
        "validation_level": validation["validation_level"],
        "yaml_conformance": validation["yaml_conformance"],
        "bundle": str(output),
        "body_mismatches": body_mismatches,
        "resource_mismatches": resource_mismatches,
        "frontmatter_mismatches": frontmatter_mismatches,
        "normalized_scalar_lines": normalized_scalar_lines,
        "normalized_documents": normalized_documents,
        "field_dispositions": dict(sorted(field_dispositions.items())),
        "validation_findings": validation["findings"],
    }


def validate_bundle(bundle: Path) -> dict[str, Any]:
    bundle = bundle.resolve()
    if not bundle.is_dir():
        raise KnowledgeBundleError(f"bundle directory does not exist: {bundle}")
    yaml = yaml_parser()
    findings: list[dict[str, str]] = []
    concepts = 0
    reserved = 0
    resources = 0
    identities: dict[tuple[str, str], list[str]] = {}
    for path in own_tree_files(bundle):
        relative = path.relative_to(bundle).as_posix()
        if path.suffix.lower() != ".md":
            resources += 1
            continue
        try:
            document = parse_markdown(read_utf8_exact(path))
        except (OSError, UnicodeDecodeError, KnowledgeBundleError) as exc:
            findings.append({"code": "unreadable-markdown", "path": relative, "detail": str(exc)})
            continue
        if document.frontmatter_lines is not None:
            try:
                parsed_frontmatter = yaml_safe_load_unique(
                    "".join(document.frontmatter_lines)
                )
            except yaml.YAMLError as exc:
                findings.append(
                    {"code": "invalid-yaml", "path": relative, "detail": str(exc)}
                )
                continue
            if not isinstance(parsed_frontmatter, dict):
                findings.append(
                    {
                        "code": "invalid-yaml-shape",
                        "path": relative,
                        "detail": "frontmatter must be a mapping",
                    }
                )
                continue
        if path.name in RESERVED_NAMES:
            reserved += 1
            if document.frontmatter_lines is not None:
                allowed_root_index = (
                    relative == "index.md"
                    and parsed_frontmatter == {"okf_version": "0.2"}
                )
                if not allowed_root_index:
                    findings.append(
                        {"code": "reserved-frontmatter", "path": relative}
                    )
            structure = visible_markdown_structure(document.body)
            if path.name == "index.md":
                if not valid_index_structure(structure):
                    findings.append(
                        {
                            "code": "invalid-index-structure",
                            "path": relative,
                            "detail": (
                                "index entries must belong to non-empty "
                                "level-one sections"
                            ),
                        }
                    )
            if path.name == "log.md":
                if not valid_log_structure(structure):
                    findings.append(
                        {
                            "code": "invalid-log-structure",
                            "path": relative,
                            "detail": (
                                "log entries must belong to newest-first "
                                "ISO-date groups"
                            ),
                        }
                    )
            continue

        concepts += 1
        if document.frontmatter_lines is None:
            findings.append({"code": "missing-frontmatter", "path": relative})
            continue
        if "kind" in parsed_frontmatter:
            findings.append({"code": "legacy-kind", "path": relative})
        type_name = parsed_frontmatter.get("type")
        valid_type = isinstance(type_name, str) and bool(type_name.strip())
        if type_name is None or (isinstance(type_name, str) and not type_name.strip()):
            findings.append({"code": "missing-type", "path": relative})
        elif not isinstance(type_name, str):
            findings.append({"code": "invalid-type", "path": relative})
        identity_value = parsed_frontmatter.get("id")
        valid_identity = isinstance(identity_value, str) and bool(
            identity_value.strip()
        )
        if "id" in parsed_frontmatter and not valid_identity:
            findings.append({"code": "invalid-id", "path": relative})
        elif valid_type and valid_identity:
            identity = (type_name, identity_value)
            identities.setdefault(identity, []).append(relative)
        status = parsed_frontmatter.get("status")
        if status is None:
            findings.append({"code": "missing-status", "path": relative})
        elif not isinstance(status, str) or status not in OKF_STATUSES:
            findings.append(
                {"code": "invalid-status", "path": relative, "value": str(status)}
            )
        for key in sorted((set(parsed_frontmatter) & OKF_STANDARD_FIELDS) - {"status"}):
            if not okf_standard_field_valid(key, parsed_frontmatter[key]):
                findings.append(
                    {
                        "code": f"invalid-okf-{key.replace('_', '-')}",
                        "path": relative,
                    }
                )
        if type_name == "Attested Computation" and "runtime" not in parsed_frontmatter:
            findings.append(
                {"code": "missing-okf-runtime", "path": relative}
            )

    for (type_name, identity), paths in identities.items():
        path_scoped_definition = (
            type_name == "kind-definition"
            and identity == "_kind"
            and all(Path(path).name == "_kind.md" for path in paths)
        )
        if len(paths) > 1 and not path_scoped_definition:
            findings.append(
                {
                    "code": "duplicate-type-id",
                    "path": ", ".join(sorted(paths)),
                    "detail": f"{type_name}:{identity}",
                }
            )

    findings.sort(key=lambda finding: (finding["path"], finding["code"]))
    yaml_failed = any(
        finding["code"] in {"invalid-yaml", "invalid-yaml-shape"}
        for finding in findings
    )
    return {
        "ok": not findings,
        "validation_level": YAML_VALIDATION_LEVEL,
        "yaml_conformance": "failed" if yaml_failed else "passed",
        "bundle": str(bundle),
        "concepts": concepts,
        "reserved": reserved,
        "resources": resources,
        "findings": findings,
    }
