---
name: init-season
description: Initialize one season directory from canonical templates without importing historical content or advancing beyond the authorized scope.
---

# Initialize season

Read `AGENTS.md`, `docs/future-architecture.md`,
`docs/archive-workflow.md`, `docs/temporal-scope.md`, and
`docs/content-contracts.md`. Use `archive-state.yaml` only as a workflow pointer.

## Canonical inputs

- Season templates: `templates/season/`
- Shared schemas: `templates/shared/`
- Race templates, only when explicit race slots are authorized:
  `templates/race/`
- Metadata contract: `docs/temporal-scope.md`
- Source contract: `docs/source-policy.md`
- Sequential state rules: `docs/archive-workflow.md`
- Structure and authority: `docs/future-architecture.md` and `AGENTS.md`
- Natural-language task contract: `docs/agent-task-recipes.md`

## Template-to-destination map

| Template | Destination under `archive/seasons/[SEASON]/` |
| --- | --- |
| `README.template.md` | `README.md` |
| `metadata.template.yaml` | `metadata.yaml` |
| `prelude.template.md` | `season/prelude.md` |
| `context.template.md` | `season/context.md` |
| `regulations.template.md` | `season/regulations.md` |
| `technology.template.md` | `season/technology.md` |
| `teams.template.md` | `season/teams.md` |
| `drivers.template.md` | `season/drivers.md` |
| `people-and-organisations.template.md` | `season/people-and-organisations.md` |
| `calendar.template.md` | `season/calendar.md` |
| `glossary.template.md` | `season/glossary.md` |

## Workflow

1. Require `[SEASON]`, initialization mode, and explicit race-slot scope.
2. Confirm no directory already exists for `[SEASON]`.
3. Copy each season template to its mapped destination exactly once.
4. In structure-only mode, replace only structural identifiers explicitly
   supplied by the task. Keep historical placeholders and initial statuses.
5. Create race folders only when the task explicitly supplies them; use
   `templates/race/` without researching or inferring a calendar.
6. Update `archive-state.yaml` according to `docs/archive-workflow.md`.
7. Stop before research unless the task separately authorizes historical
   content and provides an exact knowledge boundary.

## Prohibited behavior

- Initializing an inferred or additional season
- Researching historical facts in structure-only mode
- Guessing a calendar, race, participant, date, or cutoff
- Replacing canonical metadata or source schemas
- Advancing to `pre-weekend` or a later stage
- Overwriting an existing season directory

## Self-check

- [ ] All 11 season templates map to one destination each.
- [ ] Required shared schemas and policies were read.
- [ ] No unauthorized race folder was created.
- [ ] Structure-only files contain no historical facts.
- [ ] Document statuses remain `planned`, `unstarted`, and `not-run`.
- [ ] Repository state is a workflow pointer, not historical evidence.
