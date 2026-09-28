# Migration 0.40.0 (module 2.2.0): ceremony tiers, steps on close, template fixes

> Apply together with the kernel's `migrations/0.40.0/explicit-install-and-tiers.md`
> when a deployment of this module is synchronized past kernel `0.39.0` to
> `0.40.0` or later (module `2.1.0` → `2.2.0`). Never re-run once applied.

## What changed

1. **Ceremony tiers** (`code-of-conduct.module.md` §3 "Ceremony tiers",
   `INVARIANTS.module.md` INV-27 revised, `rules-of-rules.module.md`
   addendum to §12 and §21). A **chore** — no rule's behaviour changes — has
   no artifact: one `catalyst journal append --tier chore` entry with no
   target. A **fix** is a `BUG-` targeting the rule it restores; its steps
   are optional. A **feature** is a `REQ-` with steps opened as the work
   happens and at least one before it closes. The agent states the tier
   before starting and escalates if the change grows. `HK-` stays
   available for housekeeping worth tracking but is no longer required for
   a chore.
2. **A requirement needs a step to close.** `schemas/requirement.yaml`
   marks `Steps` `required_when_closed`; `catalyst validate` reports a
   requirement in a closed state with no step as `closed-incomplete`.
3. **ETD locations.** `schemas/bug.yaml`, `house-keeping.yaml` and
   `roadmap.yaml` declare `location: development`, where those folders
   already live (`development/bugs/`, `development/house-keeping/`,
   `development/roadmaps/`). Nothing moves.
4. **Templates.** `templates/requirement.template.md` is complete again: it
   had lost its `## Business rules`, `## Non-functional requirements`,
   `## Design / implementation plan`, `## Test plan`, `## Open questions`
   and `## Related` sections. `templates/requirements.template.md` and
   `templates/features.template.md`, which had been copies of the item
   templates, are now what `module.yaml` says they are — the skeletons of
   the `requirements.md` and `features.md` indexes.

## Steps

1. **Refresh the module** as the kernel migration's step 4 says: replace
   `.criterion/modules/software-engineering/` with the whole `2.2.0` tree.
   The kernel migration's step 1 recomposes `CODE-OF-CONDUCT.md` and
   `Rules-of-Rules.md`, which brings in the tiers.
2. **Requirement template.** Open the highest
   `requirements/templates/TEMPLATE-REQUIREMENT-vN.md`. If it ends at
   `## UI requirements` (the truncated one), add
   `TEMPLATE-REQUIREMENT-v<N+1>.md` from the module's
   `templates/requirement.template.md` and a row for it in
   `templates-requirement.md` (INV-20: a new version is a new file; never
   edit `vN` in place). If it already has `## Test plan`, do nothing.
3. **Closed requirements without steps.** `catalyst check` lists every
   requirement closed with an empty `Steps` field as `closed-incomplete`.
   Show the list to the user; **never create steps after the fact** to
   satisfy the check (INV-29). For each, the user chooses to reopen it and
   record its remaining or confirming work as steps before closing it
   again, or to leave it closed with a `comment` meta-tag saying why —
   knowing the check keeps reporting it.
4. **Version.** Record module `2.2.0` in `DEPLOYMENT.md`; journal the
   refreshed files in the kernel migration's single `--action sync` entry.
