# The open format

Keep what you know about something you run (a business, a job hunt, a
project) as a folder of plain text pages that gets more useful every time you
work. Five rules and one page format, readable by you and by any AI app. No
account, no special software, and nothing to leave behind if you switch apps.

- [FORMAT.md](FORMAT.md): the five rules and how a page is written.
- [AGENTS.md](AGENTS.md): what any AI follows in a folder like this.
- [example/](example/about.md): a small invented bakery, written this way.

## Start

Download this repository (on GitHub: **Code**, then **Download ZIP**), or
copy it with git. Keep `AGENTS.md` and `FORMAT.md`. Then either:

- **Copy the example.** Rename `example/` to your own name and rewrite its
  pages for what you run.
- **Start with one page.** Delete `example/`, make a folder, and write an
  `about.md` in it: what this is, who the owner is, what matters. Add the
  rest as work happens.

## Use it with any AI app

Many apps that work in a folder, such as Codex and Cursor, read `AGENTS.md`
on their own. If yours doesn't (Claude Code looks for `CLAUDE.md`), tell it
to read `AGENTS.md` first. In a chat app such as
ChatGPT, Claude or Grok, add `AGENTS.md`, `FORMAT.md` and your space's pages
to the chat, then paste:

```text
Read AGENTS.md and follow it for this folder. Start with about.md.
```

The pages are Markdown, so you can also read and edit every one of them
yourself in any text editor.

## Mainmind

[Mainmind](https://mainmind.app/docs/knowledge-format) is one app that runs
this format for you, across every AI app you use. You don't need it, and you
can leave it at any time with your folder intact.

## License

Apache-2.0. See [LICENSE](LICENSE).
