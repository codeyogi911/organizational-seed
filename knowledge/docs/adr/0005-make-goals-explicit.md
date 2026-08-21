---
id: 0005-make-goals-explicit
type: Architecture Decision
status: stable
title: Make Goals explicit and remove the singleton current view
description: Model organizational direction as plural Goal artifacts joined to Processes by Tasks instead of one mutable current view.
---

# ADR 0005: make Goals explicit and remove the singleton current view

## Context

A singleton current-view file combined one current Goal, active work, a Decision
queue, and one next action. Those facts already have different owners and
lifecycles: Goals express direction, Tasks own active work and next steps, and
Decisions belong to the artifacts they rule on. A singleton file duplicates
those homes, creates a shared-write bottleneck, and cannot represent several
teams or Goals cleanly.

The architecture also lacked an explicit durable relationship between a Goal
and the Process selected to advance it.

## Decision

Goal is an optional Seed primitive. The Seed ships its Kind definition but no
live Goals; each sovereign Instance creates one only when durable direction
must coordinate several Tasks, people, or time periods. Active Goals are
Working State and terminal Goals are Organizational Memory.

Every Task names one Process and may name one primary Goal. When present, the
Task is the many-to-many join over time: a Goal may need many Processes, and a
Process may serve many Goals. A Goal supplies direction but no Authority. A
Task's local outcome does not require a Goal artifact.

Remove the singleton current view. Goals live under `goals/`, active work and
next steps live in Tasks under `work/`, and pending Judgments remain visible in
their owning artifacts or in replaceable projections.

## Consequences

- An Instance may operate with no Goals; the vocabulary is available when
  coordination beyond an individual Task makes one useful.
- Multiple teams and operators can work without competing to rewrite one
  organizational status file.
- Goal-to-Process traceability is explicit without making reusable Processes
  depend on temporary priorities.
- Goal and Task indexes, dashboards, graphs, and queues are replaceable
  Machinery derived from canonical files.
- Existing Instances adopt the change through their own review; the Seed does
  not rewrite them automatically.

## Verification and rollback

The Seed doctor checks that live Goals never ship in the Seed source, that every
Instance Task names one valid Process, and that an optional Goal link resolves.
Canonical bundle validation, link checking, and focused tests must pass.
Rollback is a Git revert; an existing Instance keeps any local model it has not
chosen to migrate.
