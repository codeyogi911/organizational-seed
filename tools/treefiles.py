"""Walk one Git work tree without crossing into nested work trees."""

from __future__ import annotations

import os
from fnmatch import fnmatch
from pathlib import Path
from typing import Iterator


def is_work_tree_root(path: Path) -> bool:
    """Return whether ``path`` is the root of a Git work tree."""

    return (Path(path) / ".git").exists()


def foreign_tree_names(directory: Path, names) -> set[str]:
    """Return child directories that begin another work tree."""

    directory = Path(directory)
    foreign = set()
    for name in names:
        candidate = directory / name
        try:
            if (
                candidate.is_dir()
                and not candidate.is_symlink()
                and is_work_tree_root(candidate)
            ):
                foreign.add(name)
        except OSError:
            continue
    return foreign


def own_tree_files(root: Path, pattern: str = "*") -> Iterator[Path]:
    """Yield files owned by ``root``, excluding Git data and nested work trees."""

    root = Path(root)
    for current, dirnames, filenames in os.walk(
        root, topdown=True, followlinks=False
    ):
        here = Path(current)
        foreign = foreign_tree_names(here, dirnames)
        dirnames[:] = sorted(
            name for name in dirnames if name != ".git" and name not in foreign
        )
        for name in sorted(filenames):
            if name == ".git":
                continue
            if fnmatch(name, pattern):
                yield here / name
