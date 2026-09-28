# Module migrations index

One-time migrations for this module's entity shapes. `From`/`Target` name
catalyst kernel versions; `/sync-framework` applies these together with the
kernel's own migrations, in version order. They moved here from the kernel's
index (and, for `0.4.0`, from the kernel's `SYNCHRONIZE.md`) in kernel
0.36.0.

| File | From version | Target version | What it migrates |
|---|---|---|---|
| [`0.4.0/audit-bugs-misfiled-as-features.md`](0.4.0/audit-bugs-misfiled-as-features.md) | `0.3.1` | `0.4.0` | One-time audit of `BUG-` items that were actually feature requests; confirmed ones become `REQ-NNNNNN` requirements and the bug is retired in place (was inline in the kernel's `SYNCHRONIZE.md`). |
| [`0.20.0/roadmap-description-column.md`](0.20.0/roadmap-description-column.md) | `0.19.0` | `0.20.0` | Every `RM-NNNNNN` roadmap row gains a `Description` column (between `Title` and `Status`), populated by `/roadmap-add`/`-update`/`-merge` the same way they already populate `Title`. |
| [`0.29.0/add-step-entity-and-roadmap-multilink.md`](0.29.0/add-step-entity-and-roadmap-multilink.md) | `0.28.0` | `0.29.0` | New `STEP-NNNNNN` entity (`steps/`, `/create-step`) recording a requirement's actual implementation work; every requirement gains a `Steps` field; a roadmap row's `Linked` field generalizes from one implicit ID to an explicit list (`Rules-of-Rules.md` §21, INV-27). |
| [`0.30.0/add-test-entity.md`](0.30.0/add-test-entity.md) | `0.29.0` | `0.30.0` | New `TEST-NNNNNN` entity (`tests/`, `/create-test`) joining `BUG-`/`REQ-`/`HK-` as a fourth rule-targeting development-artifact type, with two independent optional `(0,n)` link fields, `Requirements` and `Steps`; every requirement and step gains a back-referencing `Tests` field (`Rules-of-Rules.md` §22, INV-28). |
| [`0.31.0/step-parent-bug-or-requirement.md`](0.31.0/step-parent-bug-or-requirement.md) | `0.30.0` | `0.31.0` | A step's single required parent field (renamed `Requirement` → `Parent`) now accepts a `BUG-NNNNNN` as well as a `REQ-NNNNNN`; the bug template gains its own `Steps` field, mirroring the requirement's (`Rules-of-Rules.md` §21, INV-27). |
| [`0.40.0/ceremony-tiers-and-template-fixes.md`](0.40.0/ceremony-tiers-and-template-fixes.md) | `0.39.0` | `0.40.0` | Module `2.2.0`. Ceremony tiers: a chore needs no artifact (one `--tier chore` journal entry, no target), a fix is a `BUG-` with optional steps, a feature a `REQ-` that cannot close without a step (`Steps` `required_when_closed`, `closed-incomplete`); `HK-` no longer required for chores (INV-27 revised). Bug, house-keeping and roadmap ETDs declare `location: development`. `requirement.template.md` restored in full (a truncated deployed `TEMPLATE-REQUIREMENT-vN` gets a `vN+1`); the requirements/features index templates become index skeletons. |
