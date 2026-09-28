# Rules of Rules — software-engineering module meta-rules

> Module contribution (`MODULE-SPECIFICATION.md` §6.1). This file is
> appended to the deployed `rules/Rules-of-Rules.md`, after the kernel's
> own sections, under a `### From module software-engineering` heading.
> It never replaces kernel content. Sections that moved here from the
> kernel keep their original `rr-META-NNN` IDs; the kernel keeps a
> one-line placeholder at each moved number so its numbering and
> cross-references stay intact. "Addendum" sections carry the
> software-engineering-specific part of a kernel section that otherwise
> stays in the kernel; read each one together with the kernel section it
> names.

This module's development artifacts are bugs (`BUG-`), requirements
(`REQ-`), house-keeping items (`HK-`) and tests (`TEST-`), all
rule-linked; its non-rule-linked entity types are features (`FEAT-`),
roadmap items (`RM-`) and steps (`STEP-`), plus the machine-generated
backlog (`development/BACKLOG.md`). The module's grounding type is the
kernel rule: a development artifact grounds to one or more rules, each
of which belongs to a domain.

---

## Addendum to §6 (`rr-META-006`): the development-artifact ID scheme

Format: **`(BUG|REQ|HK|TEST)-(NNNNNN)`** — see the deployed
`CODE-OF-CONDUCT.md`. `NNNNNN` is a zero-padded 6-digit sequence number,
assigned in creation order, never reused, never renumbered — unique within
its type and signer: the `userid` suffix keeps the full ID unique when two
contributors of a shared deployment draw the same number (kernel §6).
`TEST-NNNNNN` joined this format at framework `0.30.0` (§22) — like
every other member, it carries its own `Targets`/`Domain` and is
subject to `CODE-OF-CONDUCT.md` §1 ("no development without a targeted
rule"). See §9 for the separate, non-rule-linked `FEAT-` scheme used
for feature entries — that one is not a member of this format.

## Addendum to §7 (`rr-META-007`): domains proposed by development work

A bug or requirement is not required to fit an existing domain — it may
propose a new one, but only by following the kernel's §7 standard, in
every rule document.

## 9. `rr-META-009` Feature entries have their own, non-rule-linked scheme

Format: **`FEAT-(NNNNNN)`** — zero-padded 6-digit sequence number, global,
assigned in creation order, never reused. Same descriptive-naming
requirement as every other artifact and work-item ID (`INSTANTIATION-GUIDE.md`
§1): the name and filename are `FEAT-NNNNNN-<short-summary>` /
`FEAT-NNNNNN-<short-summary>.md`, never the bare ID. Stored one file per
entry under `features/`, indexed in `features/features.md`, using the
module's `templates/features.template.md` → the current
`features/templates/TEMPLATE-FEATURE-vN.md`.

A feature entry documents a possible future capability — an idea or
roadmap item, not a claim about current or required behavior. It is
**not** one of the development artifacts in §6 and is exempt from:

- §1 (`rr-META-001`)'s conflict check,
- `CODE-OF-CONDUCT.md` §1 ("no development without a targeted
  rule"), and
- ever carrying a `Targets` or `Domain` field.

It is never "done" against a rule and is never itself implemented. Once
work on a feature actually starts, open a `REQ-NNNNNN` requirement (§6)
that targets or proposes the rule(s) the feature requires — that
requirement, not the feature entry, is what gets vetted against existing
rules, assigned a domain, and measured for completion. The feature entry
records which requirement(s) resulted from it, for traceability back to
the original idea, but that link is informational, not a rule target.

## 10. `rr-META-010` Roadmap items have their own, source-tracked scheme

Format: **`RM-(NNNNNN)`** — zero-padded 6-digit sequence number, **one
sequence across every named roadmap** (unique per signer, kernel §6), assigned in the order `/roadmap-add`/
`/roadmap-update`/`/roadmap-merge` first adds each item, never reused.
Unlike a rule or a dev-artifact but like `FEAT-NNNNNN`, an `RM-` item is a
table row, not its own file — but unlike `FEAT-NNNNNN` (one flat
`features/features.md`), roadmap rows are partitioned across **one file
per named roadmap**: `development/roadmaps/<name>.md`
(the module's `templates/roadmap.template.md`), each registered in
`development/roadmaps/roadmaps.md`. A project may hold several named
roadmaps at once (e.g. a product roadmap and an infra roadmap, ingested
and updated independently); an `RM-NNNNNN` ID stays unique and resolvable
regardless of which named roadmap's file it lives in.

A roadmap item records that an external source (a product roadmap, a
planning doc, a stakeholder request) named this as a future direction —
not a claim about current or required behavior, and not itself one of the
development artifacts in §6. It is exempt from:

- §1 (`rr-META-001`)'s conflict check,
- `CODE-OF-CONDUCT.md` §1 ("no development without a targeted
  rule"), and
- ever carrying a `Targets` or `Domain` field.

A roadmap item is never "done" against a rule and is never itself
implemented. Once a human decides it's worth tracking inside catalyst,
`/create-feature` opens a `FEAT-NNNNNN` for it (§9), citing the `RM-NNNNNN` ID
in the feature's `Roadmap` field — that feature entry, and the one or more
`REQ-NNNNNN` requirements it may later become (§21 formalizes the
expectation that a roadmap item of real size decomposes into more than one
requirement), are what actually get vetted, assigned a domain, and
measured.

**`Linked` is a list, not a single ID**: every `FEAT-`/`REQ-NNNNNN`
currently associated with that row, comma-separated, in the order each was
linked. Each roadmap file's `Status`/`Linked` columns mirror every one of
those, refreshed by `/show-backlog`: `Not triaged` while nothing is linked;
`Triaged` while only a `FEAT-NNNNNN` is linked; `In progress` once at least
one `REQ-NNNNNN` is linked and at least one of them isn't yet in a closed
state (`Completed`/`Abandoned`); `Done` only once **every** linked
`REQ-NNNNNN` is `Completed` or `Abandoned` — so a roadmap
item's progress stays visible without becoming a second, competing source
of truth for completion.

A named roadmap itself is never hard-deleted once any of its rows carry a
`Linked` value — see §4's retirement principle. `/roadmap-remove` retires
it in place instead (marks it retired, keeps every row and ID resolvable)
whenever removing it outright would break a `FEAT-`/`REQ-` cross-reference.
`development/roadmaps/roadmaps.md` may legitimately be empty — unlike the
kernel's `IAM/users/users.json` (§11), a project with no roadmap yet is
complete.

## Addendum to §11 (`rr-META-011`): signed module entities

Every development artifact (`BUG-`/`REQ-`/`HK-`/`TEST-`), feature entry,
roadmap item and step carries a `Signed-off-by` field recording the
outcome of the kernel's advisory signer check (§11), and its signer's
`userid` as its id suffix (§20). A named roadmap is retired in place,
never deleted (§10) — the same "never delete, retire in place" principle
§11 applies to `/user-remove`.

## Addendum to §12 (`rr-META-012`): journal entries for module entities

A journal entry written by a module command names the module entity in
`artifact` and its files in `files`, e.g.:

```json
{
  "command": "/create-req",
  "action": "create",
  "artifact": "REQ-000001",
  "targets": ["fw-STRUCTURE-003"],
  "files": [
    {"path": "requirements/REQ-000001-foo.md", "before": null, "after": "a1b2c3..."},
    {"path": "requirements/requirements.md", "before": "d4e5f6...", "after": "g7h8i9..."}
  ]
}
```

`targets` is `[]` for this module's non-rule-linked entities (`FEAT-`,
`RM-`, `STEP-`) — a step inherits its parent's rule target rather than
naming its own (§21).

Each entry states its ceremony tier (`CODE-OF-CONDUCT.md` §3 "Ceremony
tiers", INV-27) with `--tier`: `feature` for a requirement's work,
`fix` for a bug's. A **chore** — no rule's behaviour changes — has no
artifact at all: its one entry names the change in `artifact`, carries
`"tier": "chore"` and `targets: []`, the explicit statement that it
serves no rule (kernel §12: every entry names the rules it serves or
explicitly carries none). If a chore turns out to change behaviour, it
stops being one: open the bug or requirement then, and journal the rest
under that tier.

## Addendum to §13 (`rr-META-013`): module artifacts in a shared deployment

- **Union-merged indexes.** The indexes of this module's per-file types —
  `requirements.md`, `bugs.md`, `house-keeping.md`, `tests.md`,
  `steps.md` and `features.md` — merge by union and are regenerated by
  `catalyst criterion push`.
- **Not union-merged.** Roadmap files and `roadmaps.md` (free-form
  tables) and `development/BACKLOG.md` merge normally: concurrent edits
  to the same lines stop the push for a human to resolve.
  `/show-backlog` regenerates `BACKLOG.md` after a sync.

## Addendum to §15 (`rr-META-015`): where this module's artifact types sit

- `requirements/`, `features/` — top-level, siblings of `rules/`, each
  with the full `templates/` treatment.
- `steps/` — top-level folder, sibling of `requirements/`: `STEP-NNNNNN`
  execution records, each naming exactly one parent `REQ-NNNNNN` or
  `BUG-NNNNNN` (§21).
- `tests/` — top-level folder, sibling of `requirements/`/`steps/`:
  `TEST-NNNNNN` development artifacts, each carrying its own `Targets`/
  `Domain` plus optional `(0,n)` links to the `REQ-`/`STEP-` it verifies
  (§22).
- `development/` — `roadmaps/`, `bugs/`, `house-keeping/` each a full
  artifact-type folder (previously bugs and house-keeping items lived as
  loose files directly under `development/`); `BACKLOG.md` stays flat,
  cross-cutting, not an artifact type itself. Roadmap files are one per
  named roadmap (§10) — an example of the free-form `[...]` area.
- `reconciliations/` and `workflows/` (kernel) sit as siblings of
  `requirements/`/`features/`.

## Addendum to §16 (`rr-META-016`): reconciliation and module artifacts

A `RECON-` is exempt from the chain invariant's
epic→story→task→`REQ`/`BUG`/`HK`→rule requirement. Its file is edited in
place across its lifecycle the same way `BUG-`/`REQ-` files already are.

## Addendum to §19 (`rr-META-019`): workflows for module processes

A typical module workflow documents, for example, how a bug moves from
triage to resolution.

## Addendum to §20 (`rr-META-020`): module IDs carry their signer's userid

- Every `BUG-`/`REQ-`/`HK-`/`TEST-`, `FEAT-`, `RM-` and `STEP-` ID
  carries its signer's `userid` as the trailing segment, exactly like the
  kernel's own entities; each has a resolvable signer.
- The rule-authorship limitation §20 documents should be tracked as its
  own future `HK-` item once it actually bites.
- A rename also updates this module's structured cross-reference fields:
  `Feature`, `Roadmap`, `Requirement(s)`, `Steps`, `Tests`, `Linked`.
- A rename never hand-edits `development/BACKLOG.md` (INV-14 —
  machine-regenerated); run `/show-backlog` after the rename instead.

## 21. `rr-META-021` Steps record a requirement's or bug's actual implementation work

`STEP-NNNNNN` (the module's `templates/step.template.md`) is the itemized
record of one concrete unit of work performed toward a specific
`REQ-NNNNNN` or `BUG-NNNNNN` — the files touched, commands run, and how
it was verified. It exists so a requirement's or a bug's real
implementation history is structured and independently referenceable,
not only prose buried in a `## Design / implementation plan` /
`## Fix plan` section or the journal's free-text `intent`.

Format: **`STEP-(NNNNNN)`** — zero-padded 6-digit sequence number, global
across every requirement and bug, assigned in creation order, never
reused — same scheme as every other numbered type. Same
descriptive-naming requirement as every other artifact
(`INSTANTIATION-GUIDE.md` §1): name and filename are
`STEP-NNNNNN-<short-summary>` / `STEP-NNNNNN-<short-summary>.md`, never the
bare ID. Stored one file per instance under `steps/`, top-level, sibling of
`requirements/`/`features/`/`reconciliations/`/`workflows/`, full INV-20
treatment (`templates/`, `README.md`, `steps.md` index).

**Always names exactly one parent — a requirement or a bug** — the
`Parent` field, required, never blank. A step with nothing to belong to
isn't a step; open the requirement or bug first (`/create-req`/
`/create-bug`), then steps under it. A step is opened as work on its
parent actually starts, not in advance of it (§23).

Exempt from:

- §1 (`rr-META-001`)'s conflict check,
- `CODE-OF-CONDUCT.md` §1 ("no development without a targeted
  rule"), and
- ever carrying a `Targets` or `Domain` field of its own —

it inherits its parent's already-vetted rule target; a step documents
*executing* that work, it never asserts a new behavioral claim of its
own. A step's own `Status` (`planned`/`in-progress`/`done`/`abandoned`)
tracks that one unit of work's completion, independent of the parent's
own `Status` — a requirement or bug stays open (requirement:
`Draft`/`Proposed`/`Vetted`/`Active`; bug: `Open`/`Under Review`/`Fixed`)
while its steps range across every status, and doesn't move to a closed
state (requirement: `Completed`/`Abandoned`; bug: `Closed`/`WontFix`)
(`CODE-OF-CONDUCT.md` §7) until every one of its steps is `done` or
explicitly `abandoned` with a reason.

**A `Steps` field, on both the requirement and the bug template**
(`CODE-OF-CONDUCT.md`) lists every `STEP-NNNNNN` opened against
that instance, in creation order — populated as steps are opened, never
guessed or backfilled from unrelated work. **How many steps follows the tier** (`CODE-OF-CONDUCT.md` §3, INV-27).
A requirement — feature-tier work — has its steps opened as the work
happens and cannot close without at least one: its ETD marks `Steps`
`required_when_closed`, and `catalyst validate` reports a closed
requirement with none as `closed-incomplete`. A bug — fix-tier work — may
record steps but need not. A chore has no parent, so no steps. A
requirement with real implementation work underway and zero steps
recorded is incomplete documentation, the same posture
`CODE-OF-CONDUCT.md` §2's `Test plan` requirement already takes toward
untested rules; never backfill steps to satisfy the check (§23).

**Roadmap items decompose the same way, one level up.** A roadmap row's
`Linked` field (§10) names one or more `FEAT-`/`REQ-NNNNNN` — a roadmap
item of real size is expected to become more than one requirement, each
targeting its own rule(s) and accumulating its own steps, rather than one
oversized requirement standing in for the whole item. Nothing here
numerically requires more than one requirement or more than one step, but
a roadmap item that closes out via exactly one requirement with zero
recorded steps is a signal the work was either trivial or
under-documented — worth a second look before marking it `Done`.

## 22. `rr-META-022` Tests are development artifacts that may verify requirements and/or steps

`TEST-NNNNNN` (the module's `templates/test.template.md`) joined the
`(BUG|REQ|HK|TEST)` development-artifact format at framework `0.30.0`
(§6) — unlike `STEP-` (§21), it is **not** exempt from
`CODE-OF-CONDUCT.md` §1: a test always carries its own `Targets` (one or
more rule IDs) and `Domain`, vetted the same way a bug or requirement
is. Stored one file per instance under `tests/`, top-level, sibling of
`requirements/`/`steps/`, indexed in `tests/tests.md`, full INV-20
treatment.

**Two additional, independent link fields, each `(0,n)`:**

- `Requirements` — zero or more `REQ-NNNNNN` this test verifies.
- `Steps` — zero or more `STEP-NNNNNN` this test verifies.

Both are optional, independently of each other and of the test's own
`Targets`/`Domain` — a test naming zero requirements and zero steps is
valid (e.g. an exploratory or smoke test not yet tied to specific
tracked work); it still must carry `Targets`/`Domain` like any other
development artifact. A test naming a real `REQ-`/`STEP-` id in either
field gets the same generic `dangling-reference` validation as any
other structured cross-reference — an id that doesn't resolve is
flagged, no bespoke check needed.

**Many-to-many, not ownership.** Unlike a step's single required
`Parent` (§21), a test's `Requirements`/`Steps` lists impose no
cardinality constraint on the other side — one requirement may be
verified by several tests, and one test may verify several requirements
and/or steps at once (e.g. one integration test exercising work spread
across multiple requirements). Neither field is exclusive: a test may
name requirements, steps, both, or neither.

**Back-referenced, like a requirement's `Steps` list.** A requirement
gains a `Tests` field, and a step gains a `Tests` field
(the module's `templates/requirements.template.md`,
`templates/step.template.md`) — each the list of `TEST-NNNNNN` that name
it, in creation order. `/create-test` populates both sides in one
action: it fills the new test's own `Requirements`/`Steps` fields, and
appends the new test's ID to the `Tests` field of every requirement/step
it just named. Never hand-edited directly on the requirement/step side —
always kept in sync by whichever command changes the test's own links.

## Addendum to §23 (`rr-META-023`): steps are recorded as work happens

A step (§21) is opened when its unit of work starts and closed when it
finishes, not backfilled after the fact — `STEP-NNNNNN`'s own definition
states this narrowly ("opened as work on its parent actually starts, not
in advance of it"); the kernel's §23 generalizes the same posture to
every artifact update.
