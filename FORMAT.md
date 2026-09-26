# The format

A space is a folder of plain text pages about one thing you run: a business, a
job hunt, a research project, a household. Five rules make it more useful
every time you work in it. Any person with a text editor, and any AI app, can
follow them.

## The five rules

| Rule | What it means |
|---|---|
| **One thing per page** | Each page holds one fact, lesson or skill. Link to a page instead of copying it. |
| **Say where it came from** | A page names its source and date. A fact with no source counts as unchecked. |
| **Add, don't erase** | To correct something, add a newer page that replaces the old one. The history stays, so you can see why it changed. |
| **Turn work into lessons** | When work teaches something, write it down as a lesson and name the page it should improve. When it comes up again, fold it into that page. |
| **Ask only for what steers** | Notes, lessons and facts are added freely. Changes to how work is done, what an AI is told to do, or who may do what ask the owner first. |

## One page looks like this

```markdown
---
id: 2026-03-15-ask-about-allergies-when-ordering
type: lesson
date: 2026-03-15
source: work/2026-03-14-birthday-cake-almond-sponge.md
applies-to: skills/take-a-custom-cake-order/SKILL.md
state: open
---

# Ask about allergies when taking a cake order

A child at the party could not eat nuts, and the cake had an almond sponge.
Nobody had asked when the order was taken.
```

This is the example bakery's lesson on the day it was written. The lines
between the two `---` marks say what the page is, when it was
written, where it came from and whether it is still current. The rest is
ordinary writing. Pages are Markdown, so any editor or app can open them.

## The lines at the top

| Line | Needed on | What to write |
|---|---|---|
| `id` | every page | The file name without `.md`. |
| `type` | every page | One of the page types below. |
| `date` | every page | The day the page was written, as `YYYY-MM-DD`. |
| `source` | every page except work notes | Where it came from: another page in the space, a web address, or plain words such as `Tom, by phone`. |
| `state` | every page | One of the states listed for its type. |
| `applies-to` | lessons | The page this lesson should improve, or `unknown` if nobody knows yet. |
| `updated` | optional | The day something was last added to the page. |
| `replaces` / `replaced-by` | optional | The page this one replaces, or the newer page that replaced it. |

Paths in these lines start from the top of the space, where `about.md` is. A
work note is its own source, so it has none.

## Page types

| Type | Holds | States | Where it lives |
|---|---|---|---|
| `about` | What this space is, who the owner is, what matters. One per space. | `current` | `about.md` |
| `skill` | How one kind of work is done, step by step. | `draft`, `current`, `replaced` | `skills/<name>/SKILL.md` (see below) |
| `decision` | Something the owner decided, and why. | `current`, `replaced` | `decisions/` |
| `fact` | Something true about the world: a price, a supplier, an account. | `current`, `replaced` | `facts/` |
| `lesson` | What a piece of work taught, and which page it should improve. | `open`, `folded-in`, `closed` | `lessons/` |
| `work` | A note on one piece of work: what was asked, what was done, what happened. | `open`, `done` | `work/` |

## Skills

A skill is written in the [Agent Skills](https://agentskills.io) format, so
Claude, Codex, Cursor and other AI apps that read skills can use it as it is.
Each skill is a folder named for it, holding one `SKILL.md`:

```markdown
---
name: take-a-custom-cake-order
description: "Take a custom cake order: agree the date, size and flavour, ask about allergies, and take the deposit. Use when a customer asks for a cake made to order."
metadata:
  type: skill
  date: "2026-02-03"
  source: Mira and Tom
  state: current
---

# Take a custom cake order
```

`name` is the folder's name: lower-case letters, digits and hyphens.
`description` says what the skill does and when to use it; that is how an AI
app knows to pick it, so name the moment. The other lines at the top go under
`metadata`, as the Agent Skills format asks. Keep a skill's scripts,
templates or longer notes in the same folder.

Name lesson and work files with their date first, such as
`2026-03-15-ask-about-allergies-when-ordering.md`, so they sort in order.
Name the others for what they are, such as `deposit-for-custom-cakes.md`.
Make a folder only when its first page arrives.

## How the rules play out

**Adding and correcting.** Adding to a page is fine; set `updated`. When
something a page says turns out to be wrong, write a new page with
`replaces:` naming the old one, and set the old page to `state: replaced`
with `replaced-by:` naming the new one. Don't delete it.

**The lesson loop.** Work leaves a work note. When the work taught something,
write a lesson with `source:` naming the work note and `applies-to:` naming
the page it should improve. Once the owner agrees, add the teaching to that
page, link back to the lesson, and set the lesson to `folded-in`. A lesson
that turns out not to matter becomes `closed`, with a line saying why. A
lesson that isn't clear yet stays `open`; that is fine.

**Work with no skill yet.** Do the work and keep a work note. If the same
kind of work comes up again, write a skill for it as `draft` and ask the
owner to make it `current`.

**What steers, and what doesn't.** Work notes, lessons and facts are added
freely by anyone working in the space, including an AI. The about page,
skills, decisions and the instructions an AI follows (`AGENTS.md`) steer
future work, so the owner says yes before they change.

**What never goes in.** Passwords, keys, card numbers and other secrets.
Name where a secret is kept, never the secret itself.

## A worked example

[example/](example/about.md) is a small invented bakery. Its lesson came from
a work note, applies to a skill, and was folded into it; the skill
follows a decision the owners made. Read it in that order:
[work note](example/work/2026-03-14-birthday-cake-almond-sponge.md),
[lesson](example/lessons/2026-03-15-ask-about-allergies-when-ordering.md),
[skill](example/skills/take-a-custom-cake-order/SKILL.md),
[decision](example/decisions/deposit-for-custom-cakes.md).
