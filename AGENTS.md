# Agent entry point

This repository governs a future spoiler-safe, race-by-race Formula 1 archive.
For historical work, the declared knowledge cutoff is a correctness boundary:
future facts, hindsight, foreshadowing, and later-informed emphasis are spoilers.

- Read the relevant `.cursor/rules/` files and canonical documents they cite.
- Use an applicable `.cursor/skills/` workflow before substantial research,
  drafting, auditing, editing, or state updates.
- Future historical content defaults to Polish unless the task says otherwise.
- Verify historical claims; never invent facts, quotations, or citations.
- Preserve credible conflicts and uncertainty instead of guessing or silently
  reconciling them.
- Do not create broad repository or content structures without an explicit task.
- Do not create historical content during Phase 0. Only a user instruction that
  explicitly begins Phase 1 or explicitly authorises historical content changes
  the phase; an isolated content-like request does not change it implicitly.
- Do not commit or push unless the user explicitly instructs you to do so.

An explicit Phase 0 scaffolding task may create placeholder-only directories,
templates, repository state, and workflow documentation. It does not authorise
historical research, populated season or race directories, or factual content.

Use `templates/` for future documents, `docs/archive-workflow.md` for sequential
state transitions, and `docs/agent-task-recipes.md` for task contracts. The
machine-readable `archive-state.yaml` is a workflow aid, never historical
evidence or a substitute for document metadata.

When instructions conflict, apply this authority order:

1. explicit current user instruction;
2. the target document's declared knowledge cutoff;
3. canonical spoiler and source policy;
4. the selected content contract;
5. the relevant template;
6. style preference.

Detailed policy lives in `docs/`; do not duplicate it in local instructions.
