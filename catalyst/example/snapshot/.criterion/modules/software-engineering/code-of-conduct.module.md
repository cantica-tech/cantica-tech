# Code of Conduct — `software-engineering` module contribution

> Composed into each deployment's `CODE-OF-CONDUCT.md` by the kernel's
> instantiation and `/sync-framework` procedures
> (`MODULE-SPECIFICATION.md` §6.2): the `## 3.` section below is inserted
> at the end of the deployed §3 (Standard document types), and the `## 4.`
> section at the end of the deployed §4 (Slash-command entry points), each
> under a `### From module software-engineering` heading. Section numbers
> cited in this file (§1, §2, §4, ...) are the deployed
> `CODE-OF-CONDUCT.md`'s; meta-rules are cited by their stable
> `rr-META-NNN` IDs, which this module's `rules-of-rules.module.md` keeps.
> Every command bullet in §4 below has a matching entry in `module.yaml`'s
> `commands`, and a matching task in `Taskfile.module.yml`.

## 3. Standard document types

This module contributes seven entity types. Four of them — bugs,
requirements, house-keeping items, and tests — are **development
artifacts**, fully bound by `CODE-OF-CONDUCT.md` §1 (`Targets`, `Domain`,
closed against a rule). Feature entries, roadmap items, and steps are
related but exempt schemes, described after the table.

| Type | Folder | Template | ID prefix |
|---|---|---|---|
| Bug | `development/bugs/` | `templates/bug.template.md` | `BUG-NNNNNN` |
| Requirement | `requirements/` | `templates/requirement.template.md` | `REQ-NNNNNN` |
| House-keeping | `development/house-keeping/` | `templates/house-keeping.template.md` | `HK-NNNNNN` |
| Test | `tests/` | `templates/test.template.md` | `TEST-NNNNNN` |

House-keeping is this module's one category where "no rule applies" is a
legitimate answer to `CODE-OF-CONDUCT.md` §1 (pure repo hygiene with no
bearing on any documented behavior or process) — but it must be stated
explicitly, not left blank. It stays available for housekeeping worth
tracking, but a chore (below) no longer needs one.

#### Ceremony tiers

Every change is one of three tiers (`CODE-OF-CONDUCT.md` §9,
`INVARIANTS.module.md` INV-27), and carries only that tier's ceremony:

| Tier | When | What it needs | Journal |
|---|---|---|---|
| **chore** | No rule's behaviour changes: a typo, formatting, a comment, a dependency bump without behaviour change, a documentation fix. | No artifact. | One entry: `catalyst journal append --command chore --action update --tier chore --artifact "<short description>" --intent "<goal>" --file ...`, with no `--target` (`targets: []` — explicitly no rule, INV-5). |
| **fix** | Restores the behaviour a documented rule already describes. | A `BUG-` targeting that rule; steps optional. | `--tier fix` on its entries. |
| **feature** | New or changed behaviour. | A `REQ-`, vetted against every rule document and targeting or proposing rules (`rr-META-001`); `STEP-`s opened as the work happens, at least one before it closes; tests as §3's test entries and the rules' test plans require. | `--tier feature` on its entries. |

The agent picks the tier, **states it to the user before starting**, and
escalates (chore → fix → feature) as soon as the change turns out bigger —
opening the artifact the new tier needs at that point, never
retroactively (`INVARIANTS.md` INV-29). When unsure, the higher tier.
A feature-tier change is a `REQ-`, not a feature entry: a `FEAT-` (below)
records an idea before any work starts, and becomes a `REQ-` when it does.

Feature entries (`FEAT-NNNNNN`, folder `features/`, template
`templates/feature.template.md` → `TEMPLATE-FEATURE-vN.md`) are a related but
**separate, non-rule-linked** scheme — see `Rules-of-Rules.md` `rr-META-009`.
They document possible future work, are not one of the four
development-artifact types above, and are exempt from `CODE-OF-CONDUCT.md`'s
rules (no `Targets`, no `Domain`, never "done" against a rule). When a new
feature actually needs to be developed, open a `REQ-NNNNNN` requirement —
never a `BUG-NNNNNN` — to track it.

Roadmap items (`RM-NNNNNN`, table rows inside `development/roadmaps/<name>.md`
files — one file per named roadmap, template `templates/roadmap.template.md`,
index `development/roadmaps/roadmaps.md`) sit one level above feature entries
— see `Rules-of-Rules.md` `rr-META-010`. They are populated by
`/roadmap-add`/`/roadmap-update`/`/roadmap-merge` from an external source file
rather than created one at a time, and are exempt from `CODE-OF-CONDUCT.md`'s
rules the same way feature entries are (no `Targets`, no `Domain`, never
"done" against a rule). Formalizing a roadmap item means opening a
`FEAT-NNNNNN` for it via `/create-feature`, citing the `RM-NNNNNN` ID in the
feature's `Roadmap` field. A roadmap item of real size is expected to
decompose into **more than one** requirement rather than one oversized
`REQ-NNNNNN` standing in for the whole item — its row's `Linked` field names
every `FEAT-`/`REQ-NNNNNN` currently associated with it, not just one.

Steps (`STEP-NNNNNN`, folder `steps/`, template `templates/step.template.md`)
sit one level *below* a requirement or a bug — see `Rules-of-Rules.md`
`rr-META-021`. Each names exactly one parent — a `REQ-NNNNNN` or a `BUG-NNNNNN`
(the `Parent` field) — and records one concrete unit of implementation
work performed toward it (files touched, commands run, how it was
verified). Like feature entries and roadmap items, a step is exempt from
`CODE-OF-CONDUCT.md`'s rules (no `Targets`, no `Domain` of its own — it
inherits its parent's), but unlike them it's created *during* active
implementation, not before it: a requirement (a feature, in tier terms)
has steps opened as its work happens and cannot close without at least
one; a bug's steps are optional. Neither moves to one of its ETD's
closed states (requirement: `Completed`/`Abandoned`; bug:
`Closed`/`WontFix`) while any of its steps is still `planned` or
`in-progress` — each must be `done` or `abandoned` first. Opened and
closed as the work itself happens, not batched afterward, per
`INVARIANTS.md` INV-29.

Tests (`TEST-NNNNNN`, folder `tests/`, template `templates/test.template.md`)
join this module's development-artifact types as of framework `0.30.0` — see
`Rules-of-Rules.md` `rr-META-022`. Unlike features, roadmap items, and steps,
a test is **not** exempt from `CODE-OF-CONDUCT.md`'s rules: it always carries
its own `Targets`/`Domain`, vetted the same way a bug or requirement is. On
top of that, a test may independently name `(0,n)` `REQ-NNNNNN` and `(0,n)`
`STEP-NNNNNN` it verifies — both optional, and neither implies the other.
Named requirements/steps get the new test's ID appended to their own `Tests`
field in the same action — the mirror image of a requirement's `Steps` field.

#### Hard rule: individual files and indexes

- Bugs, requirements, house-keeping items, and tests each follow
  `CODE-OF-CONDUCT.md` §3's individual-file and index hard rules. Their
  index files are:
  - `development/bugs/bugs.md` for the bug index.
  - `requirements/requirements.md` for the requirements index.
  - `development/house-keeping/house-keeping.md` for the house-keeping index.
  - `tests/tests.md` for the test index.
  - Feature entries and steps are indexed the same way, in
    `features/features.md` and `steps/steps.md`.
  - Every one of these indexes is regenerated from the artifact files by
    `catalyst index regen` (`CODE-OF-CONDUCT.md` §3), never hand-edited.
    Roadmaps are the exception: their items are rows of hand-edited
    tables (`naming: free-form`), and `development/roadmaps/roadmaps.md`
    is kept by the `/roadmap-*` commands.
- **This is a hard requirement.** `development/BACKLOG.md` always
  exists — seeded from `templates/backlog.template.md` on first deploy —
  as the go-to document for developers to review work to be done and
  current status. It is not hand-maintained: `/show-backlog` regenerates
  it in full every time it runs, so it never drifts from the real
  indexes — including every `development/roadmaps/<name>.md`. See
  `INVARIANTS.module.md` INV-14.
- **This is also a hard requirement.** `development/roadmaps/` and its
  `roadmaps.md` index always exist (empty is fine — individual named
  roadmaps are created only via `/roadmap-add`). Within any
  `development/roadmaps/<name>.md` that does exist, only the
  `/roadmap-add`/`-update`/`-merge`/`-remove` commands and `/show-backlog`
  (Status/Linked refresh) ever change it; hand-editing anything but a
  row's Notes column is pointless, the same way hand-editing `BACKLOG.md`
  is. See `INVARIANTS.module.md` INV-15.

- **Bug**: an existing ✅ rule doesn't actually hold in the running system,
  or formalizes an already-known ⚠️/❌ rule into trackable, closeable work.
  Never introduces a new rule by itself.
- **Requirement**: an explicit, tracked requirement that captures
  user/business behavior that must be implemented and tested — this is the
  artifact to open when a new feature needs to be developed, never a bug. It
  must be vetted against every existing rule document (`Rules-of-Rules.md`
  `rr-META-001` conflict check) before it's opened, it always carries a
  `Domain`, and it always answers — targets and/or proposes — one or more
  rules (and, if needed, a new domain — see `Rules-of-Rules.md`
  `rr-META-006`/`rr-META-007`) inline in the requirement doc so rule and
  requirement are reviewed together. None of those three are optional.
- **House-keeping**: dev-support tooling/process, not product behavior.
  Still targets a rule where one exists — most commonly a `rr-META-*`
  process rule.
- **Test**: verifies that a targeted rule actually holds, the same
  `Targets`/`Domain` requirement as a bug or requirement. Optionally
  names `(0,n)` requirements and/or `(0,n)` steps it verifies, on top of
  its own rule target — see `Rules-of-Rules.md` `rr-META-022`.

#### Rule documents' Linked Artifacts quick index

Every rule document carries a `## Linked Artifacts — Quick Index` heading
(kernel `INSTANTIATION-GUIDE.md` §1). This module lists there each open
`BUG-NNNNNN` whose `Targets` include one of the document's rules, as
`BUG-NNNNNN — <Name> (<Status>)`, and removes the line once the bug is
closed. Other artifact types are not listed.

#### Domain field

Feature entries under `features/` (and roadmap items and steps) are not
development artifacts under `CODE-OF-CONDUCT.md` and carry no `Domain`
field of their own — see `Rules-of-Rules.md` `rr-META-009`.

#### Development-artifact IDs

Per `Rules-of-Rules.md` `rr-META-006`: `(BUG|REQ|HK|TEST)-(NNNNNN)-(userid)`,
global per type, sequential, zero-padded 6 digits, never reused, plus the
signer's `userid` suffix (`rr-META-020`, INV-26), under
`CODE-OF-CONDUCT.md` §6's naming rule. Every ID of this module's types —
`STEP-`, `FEAT-` and `RM-` included — comes from
`catalyst id next <PREFIX> --as <signer>`, never from reading an index by
hand. Example:
`BUG-000001-Ab3xR9pQ-login-form-validation` or
`BUG-000001-Ab3xR9pQ-login-form-validation.md`, and
`REQ-000002-Ab3xR9pQ-password-reset-flow` or
`REQ-000002-Ab3xR9pQ-password-reset-flow.md`.

#### Closing an item

Before closing a bug or requirement, ensure the corresponding entry exists in
its individual file and is reflected in the relevant index file
(`CODE-OF-CONDUCT.md` §7).

Each type's Status takes exactly its entity type definition's
`allowed_values`, and "closed" means one of its `closed_states`. Only the
requirement's `Steps` check below is enforced by `catalyst validate`; the
rest are this module's rules, applied by the agent and the reviewer.

- **Bug** (`Open` → `Under Review` → `Fixed` → `Closed`, or `WontFix`;
  closed states `Closed`/`WontFix`): fix-tier work, steps optional. Does not
  move to `Closed`/`WontFix` while any `STEP-NNNNNN` in its `Steps` field is
  not `done` or `abandoned` (`Rules-of-Rules.md` `rr-META-021`). Its Test
  plan should name the test covering the fix before it moves to `Closed` —
  guidance, not a tool-enforced condition.
- **Requirement** (`Draft` → `Proposed` → `Vetted` → `Active` →
  `Completed`, or `Abandoned`; closed states `Completed`/`Abandoned`):
  feature-tier work. Its `Steps` field must name at least one step before
  it closes (`required_when_closed` in its ETD — `catalyst validate`
  reports a closed requirement without one as `closed-incomplete`), and
  every `STEP-NNNNNN` in it is `done` or `abandoned` (`Rules-of-Rules.md`
  `rr-META-021`). It moves to `Completed` once its acceptance criteria and
  rule targets are reflected in the implementation; tests follow the test
  entries of §3 and its own Test plan — guidance, not a tool-enforced
  condition.
- **Step** (`planned` → `in-progress` → `done`, or `abandoned`): not
  `done` without its own Verification section filled in; `abandoned`
  requires a reason there instead.
- **House-keeping** (`Open` → `Completed`): `Completed` once its stated
  verification passes.
- **Test** (`Draft` → `Active` → `Passing`/`Failing`, or `Disabled`;
  closed state `Passing`): not `Passing` without its own Actual outcome
  section reflecting a real run; `Failing`/`Disabled` require the same
  section explaining why.

Closing a bug as `WontFix` or a requirement as `Abandoned` never retires
the rule(s) it targeted, and vice versa (`CODE-OF-CONDUCT.md` §8).

## 4. Slash-command entry points

This module contributes the following slash commands. Each one that
creates or changes an artifact allocates IDs with `catalyst id next`, and
ends with `CODE-OF-CONDUCT.md` §4's common steps: `catalyst index regen`,
`catalyst journal append`, and `catalyst check` where no end-of-turn hook
runs it.

- `/create-bug` — create a new bug artifact immediately, register it in
  `development/bugs/bugs.md`, and track it in the same workflow as any other bug.
- `/create-req` or `/create-requirement` — create a new requirement artifact
  immediately, register it in `requirements/requirements.md`, and track it in
  the same workflow.
- `/create-test` — create a new test artifact immediately, register it in
  `tests/tests.md`, and track it in the same workflow as any other development
  artifact. Prompts for a rule target and domain like
  `/create-bug`/`/create-req` — a test is not exempt from `CODE-OF-CONDUCT.md`
  §1. Optionally accepts `(0,n)` requirements and/or `(0,n)` steps it verifies
  (`Rules-of-Rules.md` `rr-META-022`); neither is required. Named
  requirements/steps get the new test's ID appended to their own `Tests` field
  in the same action.
- `/create-feature` — create a new feature entry immediately and register it
  in `features/features.md`. Unlike `/create-bug`/`/create-req`, this never
  prompts for a rule target or domain — features are not rule-linked (see
  `Rules-of-Rules.md` `rr-META-009`).
- `/create-step <REQ-id|BUG-id>` — create a new step immediately against
  an existing requirement or bug, register it in `steps/steps.md`, and
  append its ID to that parent's own `Steps` field. Like `/create-feature`,
  never prompts for a rule target or domain — a step inherits its
  parent's (see `Rules-of-Rules.md` `rr-META-021`). Refuses if `<REQ-id|BUG-id>`
  doesn't resolve to an existing requirement or bug.
- `/roadmap-add <name> <file>` — ingest a new named roadmap from a local
  file, creating `development/roadmaps/<name>.md` from
  `templates/roadmap.template.md` and registering it in
  `development/roadmaps/roadmaps.md` (see `Rules-of-Rules.md` `rr-META-010`).
  Refuses if `<name>` already exists — use `/roadmap-update` or
  `/roadmap-merge` instead.
- `/roadmap-remove <name>` — delete `development/roadmaps/<name>.md` and
  its `roadmaps.md` entry if no row is linked to a `FEAT-`/`REQ-`;
  otherwise retire it in place (never hard-deletes a linked roadmap).
- `/roadmap-update <name> <file>` — re-ingest `<file>` as the new full,
  authoritative version of an existing named roadmap: add new rows,
  update matched rows, flag (never delete) rows missing from the new
  file.
- `/roadmap-merge <name> <update file>` — fold a partial delta file into
  an existing named roadmap: add/update only the rows the delta
  mentions, without flagging anything as missing.
- `/show-backlog` — summarize open work, blockers, and missing links,
  refresh `development/BACKLOG.md` with the result, and refresh every
  active `development/roadmaps/<name>.md`'s Status/Linked columns from
  the `FEAT-`/`REQ-` each row is linked to.

When the user enters `/create-bug: ...`, create a new bug artifact immediately
with the ID from `catalyst id next BUG --as <signer>`, register it in
`development/bugs/bugs.md` (`catalyst index regen`), and track it in the same
workflow as any other bug. It starts `Status: Open` and carries exactly one
`Severity` of `Critical`/`High`/`Medium`/`Low`. If the domain cannot be inferred from context, prompt for the
domain and rule before creating the artifact. Journal it with
`catalyst journal append --command /create-bug --action create --tier fix`,
its `Targets` as `--target`s.

When the user enters `/create-req:` or `/create-requirement: ...`, create a
new requirement artifact immediately with the ID from
`catalyst id next REQ --as <signer>`, register it in
`requirements/requirements.md` (`catalyst index regen`), and track it in the
same workflow. It starts `Status: Draft`. If the domain or target rule
cannot be inferred, prompt for both before creating the artifact. Journal it
with `catalyst journal append --action create --tier feature`, its `Targets`
as `--target`s.

When the user enters `/create-test: ...`, create a new test artifact
immediately using `templates/test.template.md` and the ID from
`catalyst id next TEST --as <signer>`, register it in
`tests/tests.md` (`catalyst index regen`), and track it in the same workflow as any other development
artifact. If the domain or target rule cannot be inferred, prompt for both
before creating the artifact — a test is not exempt from `CODE-OF-CONDUCT.md`
§1 ("no development without a targeted rule"). If the user names one or more
`REQ-NNNNNN`/`STEP-NNNNNN` this test verifies, populate the
`Requirements`/`Steps` fields accordingly, and append the new test's own ID to
each named requirement's/step's own `Tests` field (creating that field if this
is its first test); if `<REQ-id>`/`<STEP-id>` doesn't resolve to an existing
artifact, refuse with a clear message rather than citing a dangling id. Both
fields are optional — a test naming neither is valid as long as
`Targets`/`Domain` are still set. It starts `Status: Draft`. Journal it with
`catalyst journal append --action create --tier feature`, covering the test file, every
requirement/step file whose `Tests` field changed, and the regenerated
indexes.

When the user enters `/create-feature: ...`, create a new feature entry
immediately using `templates/feature.template.md` and the ID from
`catalyst id next FEAT --as <signer>`, register it in
`features/features.md` (`catalyst index regen`), and track it as idea/roadmap content, not
rule-linked development work. Do not prompt for a domain or rule target —
neither field exists on this artifact type. If this feature formalizes an
existing roadmap row (in any `development/roadmaps/<name>.md`), cite that
row's `RM-NNNNNN` ID in the new feature's `Roadmap` field and set the row's
`Status` to `Triaged` and `Linked` to the new `FEAT-NNNNNN` (the row's first
linked entry). If the user later asks to start building a registered
feature, create a `REQ-NNNNNN` requirement instead (prompting for
domain/target rule as usual), link it back to the `FEAT-NNNNNN` entry's
`Requirement(s)` field, and **append** (never replace) that `REQ-NNNNNN` to
the roadmap row's `Linked` list — a feature may reasonably decompose into
more than one requirement, each added to `Linked` as it's opened, per
`Rules-of-Rules.md` `rr-META-021`. Roadmap rows are edited in place by
hand. Journal the change with `catalyst journal append --action create`
(no `--target`: features are not rule-linked), covering the feature file,
the index and any roadmap file touched.

When the user enters `/create-step <REQ-id|BUG-id>: ...`, refuse with a
clear message if `<REQ-id|BUG-id>` doesn't resolve to an existing file
under `requirements/` or `development/bugs/`. Otherwise create a new
step immediately using `templates/step.template.md` and the ID from
`catalyst id next STEP --as <signer>`, register it in
`steps/steps.md` (`catalyst index regen`), set its `Parent` field to `<REQ-id|BUG-id>`, and
append its own `STEP-NNNNNN` ID to that parent's `Steps` field (creating
the field if this is its first step). Do not prompt for a domain or rule
target — neither field exists on this artifact type; it inherits
`<REQ-id|BUG-id>`'s own `Targets`/`Domain`. New steps start `Status:
planned` unless the user says
work is already underway, in which case `in-progress`. Journal it with
`catalyst journal append --action create --tier feature` (`--tier fix` when
the parent is a `BUG-`), covering the step file, the
parent file and the regenerated index.

When the user enters `/roadmap-add <name> <file>: ...`, refuse with a clear
message if `development/roadmaps/<name>.md` already exists (point to
`/roadmap-update`/`/roadmap-merge`). Otherwise read `<file>` from the
local filesystem, identify its distinct items, and create
`development/roadmaps/<name>.md` from `templates/roadmap.template.md` with
one `RM-NNNNNN` row per item (`Description`: a sentence or two summarizing
the item, drawn from `<file>` — not a restatement of `Title`; `Status: Not
triaged`, `Linked: *(none)*`), IDs continuing the global sequence across
every existing named roadmap — never reused, never guessed: the first
from `catalyst id next RM --as <signer>`, the rest consecutive from it in
the same write. Register the new roadmap in
`development/roadmaps/roadmaps.md` (a hand-edited row — roadmaps have no
generated index), journal it with
`catalyst journal append --action create`, then report the roadmap name
and the IDs assigned.

When the user enters `/roadmap-remove <name>`, refuse with a clear message
if `development/roadmaps/<name>.md` does not exist. If every row's `Linked`
field is empty, delete the file and its `roadmaps.md` entry outright and
report that. If any row has a non-empty `Linked` field, do **not** delete
anything — instead add a `Retired` field (today's date) to the file, mark
its `roadmaps.md` entry `retired`, leave every row and `RM-NNNNNN` ID exactly
as they are, and tell the user it was retired rather than removed because
removing it would break a live `FEAT-`/`REQ-` cross-reference. Either way,
journal it with `catalyst journal append --action retire` covering the
roadmap file and `roadmaps.md`.

When the user enters `/roadmap-update <name> <file>: ...`, refuse with a
clear message if `development/roadmaps/<name>.md` does not exist (point to
`/roadmap-add`). Otherwise treat `<file>` as the new full, authoritative
version of this roadmap: add a new `RM-NNNNNN` row for each item not already
present (with its own `Description`, same rule as `/roadmap-add`, numbered
from `catalyst id next RM`), update
the `Title`/`Description`/`Notes` of any row that matches an item in
`<file>` by title/description similarity (ask the user rather than
guessing when a match is ambiguous), and flag — in `Notes`, never by
deleting — any existing row whose item no longer appears in `<file>`.
Update the file's `Source` and `Last updated` fields, journal it with
`catalyst journal append --action update`, then report a short summary of
what was added/updated/flagged.

When the user enters `/roadmap-merge <name> <update file>: ...`, refuse
with a clear message if `development/roadmaps/<name>.md` does not exist
(point to `/roadmap-add`). Otherwise treat `<update file>` as a partial
delta, not the full roadmap: apply the same add/update matching rule as
`/roadmap-update` for only the items `<update file>` actually contains,
but do not compare against or flag any row it doesn't mention, and do not
change the `Source` field — only `Last updated`. Journal it with
`catalyst journal append --action update`, then report a short summary of
what was added/updated.

When the user enters `/show-backlog`, run `catalyst index regen`, then
inspect the current artifact indexes (open bugs — Status `Open`/`Under Review`/`Fixed` — by severity, open
requirements — Status `Draft`/`Proposed`/`Vetted`/`Active` —, work items with no
linked `REQ-`/`BUG-` doc, rules with no open work targeting them, feature
ideas with no requirement yet, and every `development/roadmaps/<name>.md`
not marked `Retired`, rows grouped by roadmap name then Status),
**overwrite `development/BACKLOG.md` in full** with the result (from
`templates/backlog.template.md`'s structure, with a refreshed timestamp),
**also refresh every active `development/roadmaps/<name>.md`** in place —
for each `RM-NNNNNN` row, resolve every `FEAT-`/`REQ-` its `Linked` field
names (if any — it's a list, not a single id) and set `Status` to
`Not triaged` (nothing linked) / `Triaged` (only a `FEAT-` linked) /
`In progress` (at least one linked `REQ-` isn't yet `Completed` or
`Abandoned`) / `Done` (every linked `REQ-` is `Completed` or `Abandoned`)
accordingly, leaving `Title`/`Notes`/`Source`
untouched; journal any roadmap row whose `Status` changed with
`catalyst journal append --action status-change` — and also report the
same summary to the user in this turn. No
file write is optional — a stale `BACKLOG.md`, or any roadmap file that
doesn't match the last `/show-backlog` run, is itself a bug in the
deployment.
