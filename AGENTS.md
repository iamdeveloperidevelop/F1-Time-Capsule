# Agent entry point

This repository governs a future spoiler-safe, race-by-race Formula 1 archive.
For historical work, the declared knowledge cutoff is a correctness boundary:
future outcomes, accidents, hindsight, foreshadowing, and later-informed
emphasis are spoilers. Exact publication-day trivia for clearly pre-cutoff
contemporary material is not; see content-based availability in
`docs/source-policy.md` and spoiler calibration in `docs/temporal-scope.md`.
Published prose must read as contemporary motorsport journalism—never as a
reminder of the anti-spoiler rule. Put dating and source caveats in footnotes
as a careful reporter would, not in every sentence and not as meta commentary
about cutoffs or “what was not yet known.”

- Read the relevant `.cursor/rules/` files and canonical documents they cite.
- Use an applicable `.cursor/skills/` workflow before substantial research,
  drafting, auditing, editing, or state updates.
- Future historical content defaults to Polish unless the task says otherwise.
- Verify historical claims; never invent facts, quotations, or citations.
- Write published prose as a contemporary motorsport journalist: always from
  the historical point of view, never explaining that viewpoint, spoilers, or
  cutoffs. Show uncertainty through attribution and natural status language;
  omit future facts silently. See `docs/methodology.md` (Published voice).
- Preserve credible conflicts and uncertainty instead of guessing or silently
  reconciling them; keep those caveats in footnotes and source apparatus, not
  as constant interruptions in reader-facing prose.
- Do not create broad repository or content structures without an explicit task.
- Do not create historical content during Phase 0. Only a user instruction that
  explicitly begins Phase 1 or explicitly authorises historical content changes
  the phase; an isolated content-like request does not change it implicitly.

An explicit Phase 0 scaffolding task may create placeholder-only directories,
templates, repository state, and workflow documentation. It does not authorise
historical research, populated season or race directories, or factual content.

Use `templates/` for future documents, `docs/archive-workflow.md` for sequential
cutoff transitions, and `docs/agent-task-recipes.md` for task contracts.
Progress is the existence and metadata of documents under
`archive/seasons/[YYYY]/`—there is no global workflow lock. Parallel agents
may work on disjoint seasons or rounds when each command's on-disk prerequisites
are already satisfied. Document metadata and verified sources remain
authoritative for historical knowledge.

Use the manually invoked archive commands listed in
`docs/commands.md`; normal season work begins with `/prepare-season [YYYY]`.

When instructions conflict, apply this authority order:

1. explicit current user instruction;
2. the target document's declared knowledge cutoff;
3. canonical spoiler and source policy;
4. the selected content contract;
5. the relevant template;
6. style preference.

Detailed policy lives in `docs/`; do not duplicate it in local instructions.
