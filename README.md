# f1-time-capsule

`f1-time-capsule` is planned as a race-by-race historical Formula 1 archive that
lets readers encounter a season without knowledge leaking backward from later
events. Time is part of factual correctness here: every future document will
declare what was publicly knowable and the latest moment its narrative may use.

Future historical content will default to natural Polish. Repository
instructions, metadata, and filenames use English.

## Historical viewpoints

- A **season prelude** stops immediately before the season's first official
  session.
- A **race prelude** stops immediately before a given weekend's first official
  session.
- A **pre-start weekend brief** includes preceding sessions but stops before
  the race starts.
- A **post-race report** includes the race and immediate official procedures,
  but nothing learned during the next event or later.

Spoiler safety excludes more than future results. It also excludes hindsight,
dramatic foreshadowing, and emphasis that only makes sense because of later
history. Later sources may support separable earlier facts, but may not expand a
document's permitted knowledge.

## Current status: Phase 0 scaffolding

This repository contains governance, research methodology, future content
contracts, reusable templates, and placeholder-only archive scaffolding. No
season directory, race directory, or historical content has been generated.

The canonical policies are:

- [`docs/temporal-scope.md`](docs/temporal-scope.md) — knowledge boundaries,
  metadata, and spoiler safety;
- [`docs/source-policy.md`](docs/source-policy.md) — evidence quality,
  traceability, and disagreements;
- [`docs/methodology.md`](docs/methodology.md) — drafting, language, editing,
  and deduplication;
- [`docs/content-contracts.md`](docs/content-contracts.md) — contracts for
  future document types;
- [`docs/future-architecture.md`](docs/future-architecture.md) — the scaffold
  and intended season layout;
- [`docs/archive-workflow.md`](docs/archive-workflow.md) — sequential cutoff and
  repository-state transitions;
- [`docs/agent-task-recipes.md`](docs/agent-task-recipes.md) — reusable
  natural-language task contracts.

See [`AGENTS.md`](AGENTS.md) for the shortest AI-agent entry point. A user must
explicitly begin Phase 1 or authorise historical content. Generic templates and
the empty `archive/seasons/` root do not themselves change the project phase.