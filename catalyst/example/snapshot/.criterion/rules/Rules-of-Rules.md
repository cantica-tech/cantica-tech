# Rules of Rules — template

> Instantiates the catalyst kernel's rules-of-rules template (`framework/kernel/rules-of-rules.template.md` in the `catalyst` repository), with the active module's `rules-of-rules.module.md` appended under `### From module software-engineering` (`MODULE-SPECIFICATION.md` §6.1).

Meta-rules governing how any rule gets added to, changed in, or retired
from one of this project's rule documents: `conversion-rules.md`. These
apply to the *process* of maintaining those documents and the code they
describe, not to the app's behavior itself. Binding on anyone (human or
agent) adding to any of them, at any point after this file exists.

Each rule must belong to a rule type directory under `rules/`, be
stored as its own markdown file in that directory, be listed in the
corresponding type index, and be referenced from the global index
`rules/rules.md`. There must be exactly one template file at
`rules/TEMPLATE-RULE.md` and no `TEMPLATE-RULE.md` files inside the
rule-type directories. No rule may be orphaned by missing a type, a local
index entry, or a global index entry.

---

## 1. `rr-META-000001-Tc0nvEx1` Check for conflicts before adding a new rule

Before a new rule is implemented, check it against the rules already
recorded in **every** rule document in `conversion-rules.md` — not just the
document that seems most relevant, since the same underlying behavior is
sometimes governed from more than one angle (e.g. a UI-visible
enabled/disabled state and the backend constraint it's supposed to
reflect), and a change to one side can silently break the other. Check,
in order:

1. The same functionality area in whichever document(s) are relevant.
2. Each document's Cross-Cutting Notes heading (or equivalent).
3. Each document's `## Linked Artifacts — Quick Index` heading — a "new" rule is
   sometimes actually a conflicting rewrite of an existing one.

If the new rule **contradicts, narrows, silently overrides, or would
break** an existing ✅ rule in any document, **stop and prompt for a
decision** — do not silently override it, and do not silently implement
both side by side and let whichever runs last win.

## 2. `rr-META-000002-Tc0nvEx1` A new rule is never done until it's gathered, implemented, tested, and documented

All four, no exceptions:

- **Gathered** — the rule's actual current/intended behavior is
  understood and written down before code changes.
- **Implemented** — the rule actually exists in the code, not just in a
  comment, commit message, or this documentation.
- **Tested** — it has **at least one test** exercising it. Name the
  project's test locations here: `tests/`. A rule with zero
  test coverage is not "done" — it's "implemented but untested," and
  should be marked as such (see status markers below), not treated as an
  acceptable end state.
- **Documented** — added to the correct rule document, under the
  functionality domain it belongs to and the right rule category, with a
  `file:line` citation and a status marker, in the same format every
  existing entry already uses.

**Status markers**: ✅ working · ⚠️ buggy/incomplete · ❌ not implemented
/ regressed · 🗑 retired (see §4).

## Which document does a rule belong in?

Project-specific tiebreaker guidance goes here — e.g.:

- **{{RULE_DOC_1}}**: {{tiebreaker description}}.
- **{{RULE_DOC_2}}**: {{tiebreaker description}}.

Not a hard wall — some rules legitimately have entries in more than one
document (one for how it's surfaced, one for the constraint it enforces)
and should cross-reference rather than pick just one.

## 3. `rr-META-000003-Tc0nvEx1` Every rule has a unique, stable ID

Format: **`(DOC_PREFIX)-(DOMAIN)-(NNNNNN)[-(parent-id)]-(userid)`**

- **`DOC_PREFIX`** — which rule document the rule lives in. Define one
  short lowercase prefix per document in `conversion-rules.md` (e.g. `ui`,
  `br`), plus the fixed `rr` prefix reserved for this file itself.
- **Name format** — every rule name and development entity must carry a name summarizing its purpose. The canonical rule name format is **`<rule-id>-<short-summary>`**, where the suffix is a lowercase slug that briefly describes what the rule is about. Example: `br-AUTH-000003-login-flow`. Similarly, every development entity (rules, domains, reconciliations, workflows, the active module's entity types, etc.) contains an explicit **Name** field (`**Name**` in field tables or rule metadata) that summarizes the purpose of the entity. This is a hard requirement for all new rules and development entities and must also be applied retroactively to existing deployed items during framework deployment or synchronization. Existing names that are only the ID must be renamed to include a summary suffix, and every index entry and link that references the old name must be updated.
- **`DOMAIN`** — a short, stable mnemonic code for the `##` functional
domain the rule sits under. Fixed once assigned — renaming a domain's
prose heading does not change its code, since existing IDs (in code
comments, tests, linked-artifact indexes, cross-references) must keep
resolving.
- **`NNNNNN`** — a zero-padded **6-digit** sequence number, unique within
  that `DOMAIN` and signer `userid`, assigned in document order the first
  time IDs are retrofitted (or in creation order thereafter: one above
  the highest number the domain has seen). Two contributors working
  concurrently in a shared deployment (§13) may draw the same number
  under different userids; the full ID stays unique through its `userid`
  suffix, and both are valid. Never reused, never renumbered, even if an
  earlier rule in the same domain is later deleted/retired. Zero-padding is always applied before the `userid`
  suffix (rr-META-000020-Tc0nvEx1) is appended — never after, and never left
  half-done across a document (a mix of 3-digit and padded 6-digit IDs
  breaks lexicographic sort).
- **`[-parent-id]`** — optional. Used two ways: (a) a rule that is a
  specialization/consequence of another rule references that rule's full
  ID (including its own `userid` suffix) as its own suffix; (b) a
  numbered sub-item inside a single rule bullet that enumerates several
  concretely distinct behaviors gets the parent's ID plus its own
  position (e.g. `br-EVTO-000015-1`, before that rule's own `userid` is
  appended). Prefer this over inventing a new top-level rule when the
  sub-items are only meaningful in the context of the parent bullet.
- **`(userid)`** — always the final segment, after any `[-parent-id]`.
  See rr-META-000020-Tc0nvEx1 for the full mechanism and the rule/domain
  authorship limitation.

Rules with no sub-items or parent never have that trailing segment —
it's absent, not empty. The `userid` segment, by contrast, is never
absent once rr-META-000020-Tc0nvEx1 applies.

### Domain codes — {{RULE_DOC_1}}

| Code | Domain |
|------|--------|
| `{{CODE}}` | {{Domain name}} |

### Domain codes — {{RULE_DOC_2}}

| Code | Domain |
|------|--------|
| `{{CODE}}` | {{Domain name}} |

### Domain code — this file

| Code | Domain |
|------|--------|
| `META` | This file's own numbered rules (`rr-META-NNN`) |

### Adding a new rule

1. Pick (or confirm) the `DOMAIN` it belongs to.
2. Take the next unused `NNN` in that domain — check both the domain's
   existing bullets and the Linked Artifacts quick index.
3. Only add `[-parent-id]` if the rule is a numbered sub-case of one
   existing bullet, or an explicit specialization of another rule.

## 4. `rr-META-000004-Tc0nvEx1` Retiring a rule

A rule ID, once assigned, is **never deleted and never reused** —
deleting the bullet outright breaks every cross-reference to it with no
trace of why. Instead, retire it in place:

1. Change its status marker to **🗑 retired**.
2. Leave the rule's text as-is (don't rewrite it to match new behavior —
   that's a *new* rule with a *new* ID) and append a one-line reason plus
the date, e.g. `🗑 retired {{DATE}} — superseded by \`{{new-id}}\``.
3. If something replaces it, the replacement is a normal new rule (next
   `NNN` in its domain) — retirement does not imply the new rule
   inherits the old number, even via `[-parent-id]`.
4. Never repurpose a retired rule's ID for an unrelated rule later, even
   in the same domain.
5. A retired rule can still be a valid target for dev-artifact work (e.g.
   an artifact explaining why it had to be retired) — retirement is a status
   change, not removal from the graph of things development work can
   cite.

## 5. `rr-META-000005-Tc0nvEx1` Rules use typed directories and indexes

Every rule must live in a type-specific directory under `rules/`, for
example `business/`, `ui/`, or `infra/`. This is a hard requirement. Each
rule must be stored as its own markdown file in that directory, and that file
must be listed in the corresponding local type index and the global
`rules/rules.md` index. A rule that is not present in its type index
or the global index is considered invalid until it is added to both. The
only rule-template file is the current
`rules/templates/TEMPLATE-RULE-vN.md` (§15 — versioned, catalogued,
nested under `templates/`, never at the rules root directly); concrete
rule files belong under the type folders, not under `templates/` or the
rules root. Aggregating multiple rules into one file or relying on
unindexed notes is not permitted.

## 6. `rr-META-000006-Tc0nvEx1` Development artifacts have their own ID scheme

If the deployed framework is missing `version.txt`, or if its version is
lower than this framework's own `version.txt`, the
deployed framework must be synchronized before further work proceeds. See
[`SYNCHRONIZE.md`](SYNCHRONIZE.md).

Format: **`<PREFIX>-(NNNNNN)`** — one `<PREFIX>` per development-artifact
entity type of the active module (its `module.yaml` `entity_types`); see
[`rules-of-development.template.md`](rules-of-development.template.md).
`NNNNNN` is a zero-padded 6-digit sequence number, assigned in creation
order (one above the highest number the type has seen), never reused,
never renumbered. It is unique within its type and signer: the trailing
`userid` (§20) keeps the full ID unique, so two contributors working
concurrently in a shared deployment (§13) may legitimately hold the same
number under different userids. Every rule-linked member
carries its own `Targets`/`Domain` and is subject to
`rules-of-development.md` §1 ("no development without a targeted
rule"). Which prefixes belong to this format, and any separate,
non-rule-linked schemes the module also defines, are the active
module's meta-rules (`MODULE-SPECIFICATION.md` §6.1).

## 7. `rr-META-000007-Tc0nvEx1` Defining a new `##` domain

A development artifact of the active module is not required to fit an
existing domain — it may propose a new one, but only by following this standard, in every rule
document.

**Domains are defined in their own directory, not inline in the rule
document.** `rules/domains/` is nested under the rules directory
(not a top-level sibling — domains exist to group rules, so they live
where rules live) and follows the same uniform shape as every other
artifact type (§15): its own `templates/`, `README.md`, `domains.md`
catalog, and free-form space for the actual domain files. Each domain
gets one file at
`rules/domains/{{DOC_PREFIX}}-{{CODE}}-{{short-description}}.md` (e.g.
`domains/br-REDIS-caching-layer.md`). This is a hard requirement, the same as
for artifact and work-item filenames (see `INSTANTIATION-GUIDE.md` §1): the
bare `{{DOC_PREFIX}}-{{CODE}}.md` is not a valid filename, the file must carry
a short description of what the domain covers as part of its name. The
`{{CODE}}` used inside rule IDs (`{{DOC_PREFIX}}-{{CODE}}-{{NNN}}`) is
unaffected by this — only the on-disk filename gains the description suffix.
See [`templates/domain.template.md`](templates/domain.template.md) → the
current `rules/domains/templates/TEMPLATE-DOMAIN-vN.md`, for the
exact file structure (`Document`, `Defined`, `Parent`, `Sub-domains`,
`Scope`, `Relationship to other domains`).

### Sub-domains

A domain may be split into sub-domains when its scope is genuinely
large enough that "which part of GATE does this rule belong to" stops
being obvious from the flat list — not by default, and not just to make a
domain file shorter.

- **Code**: `{{PARENT}}.{{SUB}}` — parent code, a literal `.`, then a
  short sub-mnemonic (e.g. `GATE.DOCKER`). This is still one `DOMAIN`
  value for ID purposes: a rule under it is
  `{{DOC_PREFIX}}-{{PARENT}}.{{SUB}}-{{NNN}}` (e.g. `ui-GATE.DOCKER-004`),
  with `NNN` scoped to the sub-domain, not the parent.
- **File**: `domains/{{DOC_PREFIX}}-{{PARENT}}.{{SUB}}-{{short-description}}.md`,
  alongside (not nested under) the parent's own
  `domains/{{DOC_PREFIX}}-{{PARENT}}-{{short-description}}.md` — the
  directory itself stays flat; the nesting is expressed by the code and by
  the `Parent`/`Sub-domains` fields cross-linking the two files.
- **Parent file** lists every child in its `Sub-domains` field. **Child
  file** names its `Parent` and inherits the parent's Scope/Relationship
  statements unless it explicitly narrows or overrides them.
- A sub-domain is subject to every other rule in this domain (conflict
  check, permanence, retirement) exactly like a top-level domain — it is
  not a lesser or informal category, just a narrower one.
- Sub-domains do not nest further than one level. If a sub-domain needs
  its own sub-domains, that's a sign the parent domain should be split
  into multiple top-level domains instead.

The `##` heading in the rule document itself carries only a one-line
pointer back to this file, not the full metadata:

```
## {{Domain name}}

> **Domain:** `CODE` — see [`domains/{{DOC_PREFIX}}-{{CODE}}-{{short-description}}.md`](domains/{{DOC_PREFIX}}-{{CODE}}-{{short-description}}.md).
```

This keeps the rule document itself readable (just rules) while the
domain's scope/conflict metadata lives in one findable, greppable place
per domain — `rules/domains/` is the authoritative index of
every domain that exists across every rule document, independent of
which document's prose you happen to be reading.

### Creating a new domain

1. **Conflict check first**, at the domain level: does an existing
domain already cover this scope, even partially, under a different
name? Check `rules/domains/` directly — it's the complete
list. Extend the existing domain instead of duplicating it.
2. **Pick a code** — uppercase mnemonic, 3–7 characters, not already used
   as a `DOMAIN` code in the same document.
3. **Add the code to the canonical table** in this file, and create its
   `domains/{{DOC_PREFIX}}-{{CODE}}-{{short-description}}.md` file, in the
   same change that adds the domain.
4. **Write the domain file's Scope and Relationship-to-other-domains**,
declaring either no conflict or the specific supersede/amend/
contradict relationship to named existing rule IDs.
5. Add the one-line pointer under the `##` heading in the rule document.
6. Only then add the domain's first rule bullet(s), `NNN` starting at
   `001`.

A domain's code is permanent, same as a rule ID — never reused for an
unrelated domain even if the original is later emptied out or retired
(its `domains/` file gets the same 🗑 retired treatment as a rule, §4).

## 8. `rr-META-000008-Tc0nvEx1` Scrum/agile work items are plugin-territory, not core

The kernel version is tracked in `version.txt` at the catalyst repository root.
If a deployed framework has no `version.txt`, or its version is lower than
this framework's own `version.txt`, it is considered
out of date and must be synchronized using [`SYNCHRONIZE.md`](SYNCHRONIZE.md).

**`work-items/` is not part of the core deployed layout.** Unlike
`rules/`/`reconciliations/`/`workflows/`/`IAM/` or the active module's
own artifact-type folders, no
deployment gets it by default. It only exists once a
project-management-type plugin extending the agile schema at
`plugins/_prototyping/project-management/agile/` (framework repository)
is activated (INV-13, INV-22) — that schema defines
`(EPIC|STORY|TASK|SPIKE)-(NNNNNN)`, `SPRINT-(NNN)`, and the one further
optional type below, but defines them as *what a plugin deploys*, not
as content core instantiation writes. See `INVARIANTS.md` INV-22 for the
activation mechanism (§17 below defines it here) and INV-5 for the
chain invariant's plugin-conditional wording. No concrete plugin extends
this schema yet — it exists so the shape is ready to build against.
(`WORKFLOW-(NNNNNN)` used to be part of this schema too; it's core now
— see §19.)

The schema's one further, optional type:

- **`BOARD-(NNNNNN)`** — the Kanban-flavor structural counterpart to
  `SPRINT-NNN`: a trackable container with its own `Status`
  (`Active`/`Archived`) that `STORY-`/`TASK-` items reference instead of
  sprint membership. Relevant only under the Kanban/Scrumban flavor (§2
  of `INSTANTIATION-GUIDE.md`) — a pure-Scrum deployment has no need for
  it, the same way a pure-Kanban one has no need for `sprints/`.

**`TICKET-(NNNNNN)` is deliberately not a defined type even within the
schema.** A `work-items/tickets/` folder, if a plugin deploys one,
carries no prescribed semantics — its actual population and lifecycle
(e.g. syncing from an external tracker) is that plugin's own concern.

## 9. `rr-META-000009-Tc0nvEx1` — owned by the active module

`rr-META-000009-Tc0nvEx1` — owned by the active module (`MODULE-SPECIFICATION.md`
§6.1); never reused.

## 10. `rr-META-000010-Tc0nvEx1` — owned by the active module

`rr-META-000010-Tc0nvEx1` — owned by the active module (`MODULE-SPECIFICATION.md`
§6.1); never reused.

## 11. `rr-META-000011-Tc0nvEx1` Users and roles are advisory, not access control

`IAM/users/users.json` (`templates/users.template.json`) is the registry
of people who can sign work — a JSON array of `{name, roles, registered,
active, notes, userid}` objects, kept as data rather than a hand-edited
document because it is managed exclusively by commands:
`/user-add`/`/user-remove`/`/user-modify`/`/user-assign-role`/`/user-list`
— see `rules-of-development.md` §4. `IAM/roles/roles.json`
(`templates/roles.template.json`) maps each role to the actions/commands
it typically performs — a JSON array of `{name, actions, reconciliation}`
objects (`reconciliation` is `full`/`propose`/`none` — see §16, the one
field in this file that's genuinely enforced rather than advisory), seeded
with a default agile-role mapping and then extended via `/role-add`
(new role) and `/role-modify` (change an existing role's actions).
`IAM/users/` and `IAM/roles/` each follow the same uniform shape as every
other artifact type (§15) — their own `templates/` and `README.md`.

**`userid` generation (`/user-add`, INV-26).** `catalyst userid gen`
(`CLI.md`) implements this; it is specified here so the rule stays
checkable. Draw 8 characters, each
independently and uniformly from the 62-character alphabet
`[A-Za-z0-9]`, using a cryptographically-secure random source. Redraw if the result contains no uppercase letter (this
closes a real parsing ambiguity in host UIs that derive an id from a
filename: an 8-letter, all-lowercase summary word like `database` must
never be mistakable for a `userid` suffix — see rr-META-000020-Tc0nvEx1). Check
the candidate against every existing `userid` already in `users.json`
(including any assigned earlier in the same batch operation); redraw
from scratch on any collision, never patch a colliding draw. Assign
once unique. A `userid`, once assigned, never changes — the same
"never retroactively changes" posture as `Signed-off-by` below.

**`IAM/users/users.json` must contain at least one entry with `"active":
true`.** This is a hard requirement, unlike registries that may
legitimately start empty: a project with zero active users has nobody to sign work, so
deployment is not complete until `/user-add` has registered at least one
person. `/user-remove` refuses if removing the last active user would
leave zero — this specific case isn't advisory, since it would break
this file's own hard existence requirement (INV-25's
fundamental-invariant exception to acting without asking).

Catalyst has no way to verify who is actually typing, so beyond that one
hard existence requirement, this scheme is **advisory**: before an
artifact-creating or status-changing command completes, the agent
resolves who is signing it, checks their role(s) against `roles.json`,
and — if the action isn't one their role covers, or they aren't
registered at all — proceeds anyway (INV-25), noting the mismatch rather
than pausing for confirmation or refusing outright. Every entity of the
active module's entity types, and every work item, carries a `Signed-off-by`
field recording the outcome (`rules-of-development.md` §2); at the same
moment, that resolved signer's `userid` is appended as the entity's own
id suffix (INV-26, rr-META-000020-Tc0nvEx1) — never resolved separately or later.

`/user-remove` never deletes a user's entry, the same "never delete,
retire in place" principle as §4: it sets `active` to `false` so
every `Signed-off-by` reference already recorded against that name stays
resolvable. A changed or removed role in `roles.json` likewise never
retroactively changes a `Signed-off-by` value already recorded — that
value reflects who signed it under the mapping in effect at the time.

## 12. `rr-META-000012-Tc0nvEx1` The journal is transaction-log-grade, not a changelog

`development/journal.jsonl` — one JSON object per line, strictly
append-only. A "changelog" narrates what happened; this journal is
precise enough to **replay**: every entry carries exact content pointers,
not just prose, so a point in time is mechanically reconstructable, not
just describable. Entries are written with `catalyst journal append`
(`CLI.md`), never by hand.

### Entry schema

Shown for the fictional `example-process` module's `ITEM` entity
(`MODULE-SPECIFICATION.md`); a real entry names the active module's own
command, entity and files.

```json
{
  "timestamp": "2026-08-23T19:00:00Z",
  "actor": "<name from IAM/users/users.json>",
  "command": "/create-item",
  "action": "create | update | close | retire | status-change | sync",
  "artifact": "ITEM-000001",
  "targets": ["fw-STRUCTURE-003"],
  "intent": ["one or more sentences — the goal driving this change, not a label"],
  "files": [
    {"path": ".criterion/items/ITEM-000001-foo.md", "before": null, "after": "a1b2c3...(40 hex)"},
    {"path": ".criterion/items/items.md", "before": "d4e5f6...", "after": "g7h8i9..."}
  ],
  "writer": "catalyst/<version>",
  "tier": "chore | fix | feature (optional)"
}
```

- **`targets`** — the rule ID(s) this change relates to, when applicable;
  `[]` for non-rule-linked artifacts (users, roles, and any
  non-rule-linked entity type of the active module). This
  is the machine-readable half of the chain invariant (INV-5) — every
  entry either names the rule(s) it serves or explicitly carries none,
  never leaves it ambiguous. A chore's entry carries none by definition.
- **`tier`** — optional: the change's ceremony tier, `chore`, `fix` or
  `feature` (`CODE-OF-CONDUCT.md` §9); the active module says what each
  requires.
- **`intent`** — the *why*, as one or more full statements of purpose
  (what the actor was trying to achieve), not a terse label. Plural
  because one atomic change sometimes serves more than one goal (e.g.
  "close a gap found while retrofitting a different rule" *and* "satisfy
  the rule being retrofitted").
- **`files[].path`** — relative to the project root. A working-copy file
  is written `.criterion/<path>` and hashed into the working copy's own
  git repository; any other path is hashed into the project's. Never
  absolute (INV-1, INV-6). Older entries with bare (working-copy
  relative), `<repo>:path` or absolute paths are normalised on read and
  never rewritten.
- **`files[].before`/`files[].after`** — the git blob SHA-1 of that
  file's content immediately before and after this change, written to
  the object store so it is retrievable independent of whether anything
  was ever committed or staged (nothing is committed or staged,
  `INVARIANTS.md` INV-4). `null` means the file didn't exist before
  (create) or doesn't exist after (delete).
- **`writer`** — `catalyst/<version>` on every CLI-written entry;
  `catalyst journal verify` holds those to errors and only warns on
  entries without it.
- **Pinning** — every journaled blob is kept reachable under
  `refs/catalyst/journal` (a commit chain whose tree holds each blob) so
  `git gc` can never prune it; `catalyst journal pin` backfills older
  entries.

### Point-in-time restore

`catalyst journal restore <T> <side-dir>` (behind `/journal-restore`)
takes, for every path in any entry with `timestamp <= T`, the `after`
hash of its latest such entry (absent if `null`) and materialises it
into the side directory — **never the live working tree**; replacing it
is the user's call once they have reviewed the reconstruction.

### What must append an entry

Every command that creates, modifies, closes, or retires a rule-linked
artifact, rule, domain, or work item, or changes a `Status` field
(`CODE-OF-CONDUCT.md` §9): make the edit, then run
`catalyst journal append` covering every file the command touched, then
report the result. This is the last step of the command, after
everything else it already does — it does not replace any of a command's
existing steps. A chore (`CODE-OF-CONDUCT.md` §9) is journaled the same
way, with `--tier chore` and no target, though it touches no artifact.

### Complements, does not duplicate, `catalyst-git`

The `catalyst-git` plugin continuously audits a *deployed project* for
rule violations and writes pass/fail reports to `audits/` (INV-13: never
catalyst's own repository). This journal is kernel
infrastructure — it applies to catalyst's own self-deployment too — and
it records history for reconstruction, not violations for alerting. A
project may have both: the journal answers "what changed and why, and can
I get back to how it was," `catalyst-git` answers "did anything just
break a rule."

## 13. `rr-META-000013-Tc0nvEx1` Shared deployments on git: the `.criterion` submodule

A deployment is **local-only** by default: its working copy lives in
agent-owned space and the project reaches it through the gitignored
`.criterion` symlink (§14, INV-6). It becomes **shared** ("repoed") when
`catalyst criterion create <url>` publishes the working copy to a
dedicated **criterion repository** and makes `.criterion` a **git
submodule** of the product repository pointing there. From then on every
product commit pins, through its gitlink, the rules in force for that
commit, and every contributor lands work on one **shared branch**
(`criterion_branch`, default `criterion`) through pull requests. Sharing
is opt-in.

The protocol is the CLI: `CLI.md` "`catalyst criterion`" specifies every
step, refusal and exit code. This section records what it guarantees and
what stays judgment.

### What is recorded where

- **Product repository:** `.gitmodules` and the `.criterion` gitlink,
  plus `<app-name>.catalyst`'s `repoed: true`, `catalyst_repo_url` and
  `criterion_branch`. The tools read these; `create` writes them.
- **Working copy** (the criterion repository): a `.gitattributes` that
  merges the journal, `rules/rules.md` and every generated entity index
  by union (`merge=union`), and `.github/workflows/catalyst.yml`, which
  runs `catalyst --working-copy . check` and
  `catalyst --working-copy . criterion integrity` on every pull request
  against the shared branch.
- **Branches:** the shared branch, plus short-lived topic branches
  (`<user>/<UTC timestamp>`) that `push` creates and that a merged pull
  request retires. There are no long-lived per-user branches.

### Lifecycle

- **`create <url>`** turns a local-only deployment into a shared one.
  The remote repository must exist (empty, or already holding this
  working copy's history); creating it on a hosting service is an
  externally visible act that needs the user's assent. `create` stages
  the product repository's changes and commits nothing: the user
  commits them (INV-4).
- **`join`**, in a fresh clone of the product repository, checks out
  the shared working copy (submodule init, shared branch).
- **`push -m <message>`** is how a contributor lands work: commit,
  rebase onto the shared branch, regenerate the indexes the union merge
  touched and journal their merged state, `catalyst check`, integrity
  against the shared branch, push the topic branch with a lease, open a
  pull request. Any failing step pushes nothing.
- **`sync`** fast-forwards to the shared branch, and refuses while local
  work is uncommitted or unpushed. The product's gitlink then moves:
  committing it pins the new rules for the product.
- **`status`** reports where the working copy stands against the shared
  branch.
- **`protect --yes`** sets branch protection on the shared branch
  (GitHub): pull requests required, the `catalyst` check required, no
  force-push, no deletion. On another host, set the equivalent by hand.

### IDs across contributors

Two contributors allocating concurrently can draw the same `NNNNNN` for
one type. Both IDs are valid: the userid suffix (§20) keeps the full ID
unique, so numbers are unique per entity type and signer (§3, §6). Never
renumber. One signer working from two clones syncs between them, since
the same signer drawing the same number twice is a real duplicate
(`catalyst validate` reports `duplicate-id`).

### Conflicts: AI never applies a merge

Union merge settles the append-only journal and the regenerated indexes.
Any other conflict (two contributors changed the same artifact) stops
the push: the rebase is aborted, nothing is pushed, the conflicting
files are listed. The contributor resolves it by hand, or the agent
records its proposed resolution as a `RECON-` case (§16: `Trigger`
`merge-conflict`, `Baseline` the shared branch's version, `Proposed` the
resolution) for a human to accept through `/reconcile`. The agent never
applies a resolution of its own and never picks a side.

### Identity and the real controls

A contributor must be registered (`/user-add`, with a userid — INV-26)
before signing anything; the registration is itself a change that lands
through a pull request. `Signed-off-by` resolves a user by `name`,
`git_username` or `userid`, so signatures already written are never
rewritten when a contributor joins. `push` commits, and names its topic
branch, under the signer's `git_username` when the entry has one, else
their `name`.

Identity is still self-declared: catalyst cannot verify who is typing
(§11). The real controls are the hosting service's: who may merge into
the shared branch, pull-request review, and the required `catalyst`
check that branch protection enforces. Without protection, anyone with
write access can push to the shared branch directly, and the gates in
this section are agent courtesy only.

### What this is not

Not a replacement for `/sync-framework`, which brings the framework into
a deployment; this shares one deployment's own state across its
contributors. Not a substitute for the journal (§12): every change a
pull request carries was journaled when it was made, and the merged
state `push` produces is journaled too.

### `/dogfood` is catalyst-development-only

`/check-rules` plus a four-eyes drift check is available as a standalone
command, `/dogfood` — but only when developing catalyst itself, never as
part of what an ordinary deployment exposes. It isn't listed in
`CODE-OF-CONDUCT.md` §4 and `INSTANTIATION-GUIDE.md`/`SYNCHRONIZE.md`
never materialize a `.claude/commands/dogfood.md` for a deployed project;
it exists only in catalyst's own repository, for verifying catalyst's
own rules against catalyst's own actual state. `/commands list` (§4)
surfaces it when running in that context, and stays silent about it
everywhere else.

**After every `/dogfood` run that ends clean, or ends with fixes applied
and reverified**, offer to share the result — `/criterion push` if this
deployment is shared, `/criterion create` if it isn't. Never run either
automatically (INV-4: no push without explicit assent).

## 14. `rr-META-000014-Tc0nvEx1` Agent-owned working copy, the tracked pointer, and project lifecycle

INV-6 (revised): the working copy — a directory always named
`.criterion/` — is not built inside the target project's own tree. It
takes one of two shapes:

- **Local-only** (the default): it builds in **agent-owned space**, a
  per-project data location the running agent already maintains,
  outside the project being governed. Its location is computed per
  machine by the running agent from its own conventions (`BOOTSTRAP.md`
  §1; each agent's shim says how) and is never written into a tracked
  file.
- **Shared** (§13): it is a **git submodule** of the product repository
  at `.criterion`, checked out from the criterion repository. The
  product repository tracks only `.gitmodules` and the gitlink, never
  the working copy's content.

Either way the target project tracks one pointer at its root:
**`<app-name>.catalyst`** (JSON, from
`templates/catalyst-pointer.template.json`), which holds no path — small,
safe to commit, no rule/artifact/journal content in it, identical on
every machine.

**One access path.** `<project root>/.criterion` is how everything —
agents, tools, the project's own `Taskfile.yml` — reaches the working
copy. Local-only, it is a **symlink** to the agent-owned `.criterion/`,
always gitignored (`/.criterion` in the project's `.gitignore`); the
agent creates or repairs it at install, at `/project import`, and at
every session start (`BOOTSTRAP.md` §1.1). Shared, it is the submodule
checkout, which `catalyst criterion join` initialises in a fresh clone;
the agent never replaces it with a symlink. Every document path written
`.criterion/...` therefore means the same thing on every machine and for
every agent. Tools resolve the working copy in this order: (1)
`<project root>/.criterion` (symlink followed, submodule, or a real
directory); (2) legacy — a pointer's `agent-source` field, if present
and an existing directory (pre-0.37.0 pointers may still carry
`agent-source`; tools honor it until migrated); (3) any tool-specific
extra fallback. The project root is the directory holding the
`*.catalyst` pointer.

`.criterion/DEPLOYMENT.md` stays the source of record for the
deployment's own metadata (versions, module) inside the working copy.
Sharing is recorded in the product repository, where the tools read it:
`.gitmodules`, plus the pointer's `repoed`, `catalyst_repo_url` and
`criterion_branch`, written by `catalyst criterion create` (§13).
`catalyst_repo` and `created_by` are informational and gate nothing.

**No agent owned-space concept available, or no symlinks on this
platform:** fall back to building `.criterion/` directly inside the
target project as a real directory, gitignored there, never committed.
`<app-name>.catalyst` still gets written at the project root, unchanged.
Every mechanism below (migration, export, import) treats this fallback
as just another shape of `<project root>/.criterion`, not a special case.
To share such a deployment, move the directory out of the project and
symlink it first: `catalyst criterion create` starts from the symlink
shape.

### Migration from the pre-pointer-file model

A deployment installed before this section existed has `.criterion/`
sitting directly in the project root, with no `<app-name>.catalyst`
anywhere. Detect this (a `.criterion/` dir at the project root and no
`*.catalyst` pointer file beside it) and offer the migration — it is a
structural change, so confirm with the user before proceeding, the same
courtesy as `/criterion create`:

1. Resolve the agent-owned location per `BOOTSTRAP.md` §1. If the
   running agent has no owned-space concept, there is nothing to move —
   stop here; the in-project fallback shape already **is** the target
   shape, it just still needs its `<app-name>.catalyst` pointer written
   (step 3 below, skipping step 2).
2. **Move**, not copy, the entire existing `.criterion/` tree from
   the project root to the resolved agent-owned location, then create
   the `.criterion` symlink at the project root pointing at it.
3. Write `<app-name>.catalyst` at the project root (no path in it);
   `repoed`/`catalyst_repo`/`catalyst_repo_url`/`created_by` carried over
   from the existing `.criterion/DEPLOYMENT.md` if one exists, else
   left at their unset defaults.
4. Make sure `/.criterion` is in that project's `.gitignore` — the
   symlink (or the fallback directory) is never committed.
5. Append one journal entry, in the working copy's new location, for the
   migration itself (`action: "sync"`, `intent` describing the move,
   `files` covering the old and new `DEPLOYMENT.md`/pointer locations by
   content hash) — this is exactly what the journal (§12) exists to
   record, and its immutability means the pre-migration history stays
   readable at its old hashes regardless of where the tree now lives.
6. Report the result. Per hard rule 4, nothing is committed
   automatically — but note explicitly that `<app-name>.catalyst` is now
   something the user will want tracked, unlike anything that came before
   it.

### Agent switching procedure

When a session starts or an agent assumes governance of a project previously managed by another agent (detected when the running agent's identity differs from the `agent` field in `<app-name>.catalyst`):
1. Resolve the running agent's own owned location per `BOOTSTRAP.md` §1 (or the in-project fallback `.criterion/`).
2. If the `.criterion/` working copy existed at a previous location (the current `.criterion` symlink's target, or a legacy pointer's `agent-source`), mirror it into the new location: the new location ends up an exact copy of the old one — every file the old one had, none it didn't — overwriting anything already at the new location that conflicts, and removing anything at the new location the old one doesn't have. Never a partial merge.
3. Repoint the `.criterion` symlink at the project root to the new location (skip on the in-project fallback), keeping `/.criterion` in the project's `.gitignore`. A shared deployment's `.criterion` is a submodule inside the project (§13): skip steps 2–3 for it.
4. Update `<app-name>.catalyst`: set `agent` to the current agent's identifier and `updated` to the current date string (`YYYY-MM-DD`) — nothing else; the pointer holds no path, and the project's `Taskfile.yml` needs no edit.
5. Update persistent framework memory (and deployment notes) with the current agent name, resolved working-copy location, and update timestamp.

`/switch-agent [agent-id]` runs this same procedure on demand, unconditionally
(steps 1–5 above, without first checking whether identity actually differs)
— the manual escape hatch for when the automatic per-session check above is
skipped (e.g. dropped by a compacted session) or only partially applies (one
field updated, another left stale). Full command spec: `CODE-OF-CONDUCT.md`
§4.

### `/project create`/`remove`/`export`/`import`

The lifecycle commands for this model (full command spec:
`CODE-OF-CONDUCT.md` §4).

- **`create <name>`** is the explicit, named entry point for the
  instantiation procedure (`INSTANTIATION-GUIDE.md`, INV-2) — resolves the
  agent-owned location and runs `catalyst init`, which builds a fresh
  working copy there, writes
  `<app-name>.catalyst` (no path in it), creates the `.criterion`
  symlink, and adds `/.criterion` to the project's `.gitignore`. Refuses if a pointer file or an in-project
  `.criterion/` already exists here — that's `/project import
  --force`'s job, not `create`'s.
- **`remove <name>`** un-links locally only: deletes the project's
  `<app-name>.catalyst` and the `.criterion` symlink (on the fallback,
  it stops treating the in-project `.criterion/` as active). The working copy itself, this
  agent's memory note, and any `criterion` repo are all left exactly as
  they are — never delete, retire in place (`rr-META-000004-Tc0nvEx1`), same
  principle as user retirement (§11).
- **`remove <name> force`** additionally deletes the working copy (agent-owned,
  or the in-project fallback) and this agent's memory note for the project. This is
  the one genuinely destructive path here — confirm explicitly before
  proceeding, the same as creating a criterion repository for
  `/criterion create`. It never touches a `criterion` repo: that's a
  separate, externally-hosted, possibly multi-contributor artifact, well
  outside the blast radius of a local removal.
- **`export <name> [file]`** reads every file under the working copy and
  writes one JSON bundle — relative path → file content, plus the
  pointer fields (never a path, which is meaningless outside the
  exporting machine — a legacy `agent-source` is dropped). Default
  filename when omitted: `<name>-catalyst-export-<UTC timestamp>.json`,
  written to the current directory.
- **`import <file>`** installs a bundle into the current project — same
  refusal condition as `create` if a deployment already exists here.
  Resolves this agent's own owned location on this machine (never the
  exporting machine's), writes every bundled file there, creates the
  `.criterion` symlink (with `/.criterion` gitignored), writes
  `<app-name>.catalyst` with the bundle's pointer fields carried over
  as-is, and appends one journal entry for the import.
- **`import <file> force`** is the one case allowed to proceed even when
  a deployment already exists here — it overwrites it. Warn what's about
  to be replaced and confirm explicitly first, same tier of
  destructiveness as `remove ... force`.

## 15. `rr-META-000015-Tc0nvEx1` Every artifact type has the same directory shape

Hard rule, no exception: **every artifact-type directory carries a
versioned, catalogued `templates/` subdirectory**, and both it and the
artifact-type directory itself always have a `README.md`.

```
<artifact-type>/
  templates/
    README.md
    templates-<type>.md      # catalog: Version | File | Timestamp | Notes
    TEMPLATE-<TYPE>-v1.md
    TEMPLATE-<TYPE>-v2.md    # a new version when the template's content
    ...                      # changes meaningfully — never overwritten in place
  README.md
  <type>.md                  # catalog of actual artifact instances
  [...]                      # actual artifact files/folders — free-form,
                              # any depth, this artifact type's own choice
                              # of sub-organization
```

`templates/` accepts **files only** — a new template version is a new
file (`TEMPLATE-<TYPE>-v2.md`, never an edit to `v1`), never a
subdirectory. The artifact-type root above it accepts files *and*
folders at arbitrary depth, precisely because different artifact types
need different sub-organization (e.g. rule documents nested by domain,
one file per named instance of some module entity type) — this rule fixes the *shape*
`templates/` + `README.md` + `<type>.md` provide, not how the actual
artifacts underneath are arranged.

**Versioned and timestamped**, per the hard rule this section exists to
satisfy: `TEMPLATE-<TYPE>-vN.md`'s `N` is the version; the *timestamp*
lives in `templates-<type>.md`'s catalog table — one row per version,
recording when it was introduced and what changed, so template history
is inspectable without diffing file content. The **current** version is
always the highest `N` present; nothing below `templates/` ever gets
edited in place once a newer version exists — that would defeat the
point of versioning it at all.

**Exactly one exception to "everything nests under an artifact-type
folder": documents that govern the artifact type itself** —
`Rules-of-Rules.md`, `rules-of-work-items.md`, and each artifact type's
own `templates-<type>.md` catalog — sit flat alongside `README.md` and
the instance catalog, siblings to `templates/`, not inside it and not
inside the free-form `[...]` area. This is already the existing shape of
`rules/Rules-of-Rules.md`; §15 generalizes it, it doesn't change it. A
`work-items/` folder, if a project-management plugin deploys one, uses
the same shape for its own `rules-of-work-items.md` (§8, INV-22).

### Where every artifact type actually sits

- `rules/` — `templates/`, `domains/` (itself shaped exactly like an
  artifact type: `templates/`, `README.md`, `domains.md` catalog,
  free-form domain files — nested here because a domain exists only to
  group rules, never as a top-level sibling), `README.md`,
  `Rules-of-Rules.md`, `rules.md`, free-form rule documents (`[...]`,
  typically nested by domain, e.g. `business/business-rules.md`).
- The active module's artifact-type folders (`<folder>/`, one per entity
  type, from each entity type's ETD `folder`) — top-level siblings of
  `rules/` unless the module places them under `development/`, each with
  the full `templates/` treatment. Where each one sits is the active
  module's meta-rules (`MODULE-SPECIFICATION.md` §6.1).
- `reconciliations/` — top-level folder, sibling of the module's
  artifact-type folders, not nested under `work-items/`: `RECON-NNNNNN`
  cases record diverging versions — such as a conflict that stopped
  `/criterion push` (§13) — not agile process (§8), and are never themselves work (§16).
- `workflows/` — top-level folder, sibling of `reconciliations/`:
  `WORKFLOW-NNNNNN` process-definition documents, core (not gated behind
  any plugin) and never themselves work (§19).
- `IAM/` — new top-level folder replacing bare
  `development/users.json`/`roles.json`; holds `users/` and `roles/`,
  each shaped exactly like any other artifact type (§11), including the
  `templates/` treatment. `TEMPLATE-USERS-v1.json`/`TEMPLATE-ROLES-v1.json`
  version the registry's *seed shape* (the array a fresh deployment
  starts from), not a per-instance document — `users.json`/`roles.json`
  are each one JSON array, not one-file-per-instance, so there is
  exactly one live instance per type, versioned the same way any other
  type's template is.
- `plugins/` — unchanged (INV-10..13): `<type>/<name>/`, each activated
  plugin's own install, sourced from its own repository. Not subject to
  the `templates/`+catalog shape — a plugin owns its own internal
  structure.
- `development/` — `meta-tags/` promoted to a full artifact-type folder
  (previously meta-tags lived as loose files directly under
  `development/`), plus any module artifact-type folders the active
  module places here; `README.md`, `journal.jsonl` (and any generated
  report the module adds) stay flat, cross-cutting, not artifact types
  themselves.
- `work-items/` — **not part of the core layout** (§8, INV-22). Only
  exists once a project-management-type plugin extending
  `plugins/_prototyping/project-management/agile/`'s schema is
  activated; that plugin's own `## Contributes` section then defines
  which of `boards/`/`epics/`/`spikes/`/`sprints/`/`stories/`/`tasks/`/
  `tickets/` it deploys, alongside `README.md` and
  `rules-of-work-items.md`.

See `INSTANTIATION-GUIDE.md` §1 for the full deployed layout tree and
`INSTANTIATION-CHECKLIST.md` for the tickable deploy-skeleton steps.

## 16. `rr-META-000016-Tc0nvEx1` Reconciliation of diverging entity versions

Two versions of the same entity can disagree — most often when
`/criterion push` stops on a rebase conflict (§13), or when an actor's
change falls outside their role (`rr-META-000011-Tc0nvEx1`). `RECON-NNNNNN` is the
durable, chainable record of that disagreement and how it got settled,
instead of the resolution living only in an ephemeral proposal. A human
decides it; the agent may propose but never applies a resolution of its
own.

**Never itself work.** Like `WORKFLOW-` (§19), a `RECON-` carries no
`Targets` rule field and is exempt from the chain invariant's
epic→story→task→active-module artifact→rule path — its chain
runs sideways, via an `Entity` field naming the artifact actually in
dispute, not downward to a rule.

**May optionally name a guiding workflow.** A `Workflow` field can cite
a `WORKFLOW-NNNNNN` (§19) whose `## Steps`/`## Gates / exit criteria`
describe how this specific, recurring kind of conflict should be
resolved — read it before choosing a `/reconcile` verb, when present.
Most cases won't have one: the fixed verb set below already *is* the
procedure for the ordinary case.

**Opened** by the agent when `/criterion push` stops on a conflict and
it has a resolution to propose (§13), or manually by any actor who wants
a second opinion recorded before landing a change. `Trigger` records
which: `merge-conflict`, `rights-mismatch`, or `manual`. `Baseline`
captures the shared branch's current content for the entity at open
time; `Proposed` captures the version being contested (for a conflict,
the proposed resolution). Nothing is applied until a human accepts it.

**Revised, not re-filed.** Each round of back-and-forth (a counter-edit,
a clarifying question, a revised proposal) is a new row appended to the
same file's `## Revisions` section — never a new file per round, unlike
`templates/`'s own `TEMPLATE-<TYPE>-vN.md` versioning. The file is
edited in place across its lifecycle the same way the active module's
living artifacts already are, and every edit is journaled with its before/after content hash
(INV-17) — that already gives the audit trail; no second versioning
scheme is needed on top.

**Resolved** via `/reconcile <id> accept|accept-with-edits|reject|propose
<text>`: `accept` merges `Proposed` into the `Entity` as-is;
`accept-with-edits` merges the latest `## Revisions` row's content
instead; `reject` leaves the shared branch's version unchanged and the
proposer drops or reworks their change; `propose <text>`
appends `<text>` as a new `## Revisions` row without resolving anything.
`Status` moves `Open` → `Under Review` → one of `Resolved-Accepted` /
`Resolved-Accepted-with-Edits` / `Resolved-Rejected` → `Closed`.

**Who can do what is genuinely gated by role — the one deliberate
exception to `rr-META-000011-Tc0nvEx1`'s advisory-only principle.** Each role in
`IAM/roles/roles.json` carries a `reconciliation` field: `full` may use
every verb, including the three resolving ones; `propose` may only use
`propose <text>` — moving `Status` to `Under Review` — and is refused
outright on `accept`/`accept-with-edits`/`reject`, told a `full`-level
actor must finish it; `none` is refused on every verb immediately, told
to ask a `full` or `propose` actor to act on their behalf. This differs
from every other role check in the framework in that the command
genuinely stops rather than asking for confirmation and proceeding
anyway. The trust boundary is unchanged — catalyst still can't verify
who's typing — but letting anyone finish a reconciliation regardless of
role would defeat the reason `RECON-` exists: the `Resolver` field and
the journal entry it produces are only meaningful as a record of *who
was actually allowed to decide*, not just who happened to type the
command.

**Layout and ID**: `reconciliations/`, top-level, sibling to
the active module's artifact-type folders (§15's "Where every artifact type actually
sits"), full `templates/`+catalog treatment (INV-20). ID format
`RECON-(NNNNNN)`, 6 digits, its own sequence, never reused — unique per
signer, the same scheme as every other numbered type (§6).

## 17. `rr-META-000017-Tc0nvEx1` Content-contributing plugins

Every `repository`-type plugin only *observes* the deployed project —
it reads the project's own repository and writes its own output (e.g.
an audit trail), but never adds a core artifact type or a slash
command (INV-13). A **content-contributing plugin** is the other shape:
on activation, it
materializes deployable content — an artifact-type folder (with the
standard `templates/`+catalog treatment, INV-20) and/or slash-command
files — into the target project; on deactivation, it removes exactly
that same content.

**Declared via `## Contributes`**, a new optional section in
`working-contract.md` (`TEMPLATE-WORKING-CONTRACT.md`), naming:

- the artifact-type folder(s) it deploys, and where their templates
  resolve from (its own repository, or — while still under
  `plugins/_prototyping/` — a shared prototype schema there, never
  vendored as a stale local copy);
- the slash-command file(s) it deploys into `.claude/commands/`.

**`/catalyzer activate <name> <version>` materializes this content**,
the same mechanism instantiation already uses to copy core
templates into a fresh deployment (`INSTANTIATION-GUIDE.md` §1): create
the named artifact-type folder(s) with their `templates/`+catalog+
`README.md`, and copy the named command file(s) into `.claude/commands/`.
**`/catalyzer deactivate <name>` removes exactly what activation
added** — the templates/ scaffolding and the command files — and
**never touches artifact instances the deployment already created**
with them (real `EPIC-NNNNNN`/etc. files, and their index entries, are
deployment content, not plugin content, the same non-destructive
posture `/project remove` already uses for the working copy, §14). A
deployment with existing instances but no active plugin simply can't
create *more* until reactivated.

**Two or more content-contributing plugins of the same category must
not both be active** if their `## Contributes` sections would deploy
the same artifact-type folder — that's a content conflict, not
additive; refuse the second activation and point at deactivating the
first.

**Plugins under `plugins/_prototyping/`** are exempt from INV-11's
"every plugin has its own repository" — a prototyping plugin's content
lives in catalyst's own repository until it graduates into a top-level
plugin-type directory (e.g. `repository/`, `project-management/`), at
which point INV-11 applies to it like any other plugin.

## 18. `rr-META-000018-Tc0nvEx1` Recreation drift check

`/dogfood`'s base procedure (§13's `### /dogfood` subsection) verifies
that catalyst's actual state still matches what its own rule document
*claims* — for an existing rule, is the cited evidence still accurate.
It cannot catch a different failure: an invariant gets added to
`INVARIANTS.md` but never actually gets retrofitted into any rule at
all, so there is nothing existing there for the base check to evaluate
in the first place. This section defines a second, opt-in mode that
catches exactly that — independently re-deriving `INV-N` coverage from
`INVARIANTS.md` and the actual codebase, blind to the live deployment's
rule document, then comparing. Both checks keep running; neither
replaces the other.

### Trigger: `/dogfood recreate`

Opt-in, not part of the default `/dogfood` run — this spawns a full,
careful codebase read, expensive relative to the base check. Suggested
cadence: before cutting a release, not on every invocation. Because the
isolation mechanism below operates on a git worktree, this audits the
last **committed** state, not uncommitted working-tree edits — a
non-issue at the suggested cadence, where the tree should already be
clean.

### The isolated agent

Spawned via the `Agent` tool with `isolation: "worktree"` — one agent,
not a four-eyes pair (see "Why not four-eyes" below). Since
`.criterion/` lives entirely outside this repository, in agent-owned
space reached only through the gitignored `.criterion` symlink at the
repository root (INV-6), a worktree checkout has no path to it — the
symlink is untracked, so absent there, though `catalyst.catalyst` itself
is a tracked file and will still be present in the checkout. The agent's
prompt must therefore state explicit, forceful prohibitions, not rely on
the worktree's isolation alone: never compute the agent-owned location,
never resolve any `*.catalyst` pointer's legacy `agent-source` field, and
never read anything under a path so resolved; never read anything named
`.criterion/` under any form it might be reached; never consult `git
log` or commit messages, which narrate exactly what changed in the
live deployment — current file content only.

**The prompt handed to this agent must be hand-authored and
self-contained, never `/dogfood`'s own text forwarded verbatim** — the
base procedure above names
`.criterion/rules/framework/fw-framework-rules.md` by literal path;
reusing that text would leak exactly what blindness is meant to hide.

**Deliverable**: for each `INV-N` in `INVARIANTS.md`, found or
not-found, plus evidence — a `file:line` citation, or "behavioral, not
machine-checkable" for something no script can verify. Not a full
retrofit-quality rewritten rule document; the comparison below only
needs a coverage judgment per invariant, not finished prose, IDs, or
domain assignment.

### Why not four-eyes

`ANALYSIS-PLAYBOOK.md`'s own stated principle is that four-eyes matters
most for exactly this kind of extract-what-exists-in-code work — this
section is a deliberate, reasoned departure from that principle, not an
oversight. The second opinion this whole check exists to provide
already comes from comparing the isolated agent's findings against the
live deployment; pairing the isolated agent with a second one on top of
that duplicates cost for a periodic drift check, unlike a one-time
bootstrap (`INSTANTIATION-GUIDE.md` §4), where the playbook's full
four-eyes remains the right tool.

### Comparison

Done by the orchestrating session itself, after the isolated agent
returns — unlike the generation/research side, comparing two
already-produced documents doesn't need blindness. **This is a
judgment-based read, never a literal string search for `INV-N`.** Many
existing rules cite only an `INVARIANTS.md:<line>` pointer and never
spell out the bare `INV-N` label in their own text, and cited line
numbers drift as `INVARIANTS.md` grows without the underlying rule
being wrong — matching requires reading each rule's content and its
cited evidence, not grepping for a label or trusting an exact line
number.

Two flat-severity outcomes per `INV-N`, neither weighted above the
other regardless of whether the invariant is machine-checkable or
behavioral:

- the isolated agent found supporting evidence, but the live deployment
  has no rule covering that `INV-N` at all;
- the live deployment claims coverage for an `INV-N`, but the isolated
  agent's independent read found no supporting evidence for it.

### Reporting only

Never fix anything automatically, same as the base `/dogfood` policy —
this surfaces drift for the user's or a follow-up command's call, it
does not resolve it.

### Out of scope

Stays catalyst-development-only, the same boundary §13 already draws
for `/dogfood` itself. Not a mechanism any other deployed project gains
access to.

## 19. `rr-META-000019-Tc0nvEx1` Workflow entity for guided procedures

`WORKFLOW-NNNNNN` (`templates/workflow.template.md`) is a
process-definition document, not a unit of work: it documents a
repeatable multi-step procedure (e.g. how one of the active module's
artifacts moves from triage to resolution, or how to work through a particular recurring kind of
reconciliation). It carries `Status` (`Active`/`Deprecated`) reflecting
whether the process is currently in use, never a work-tracking
lifecycle, and is never itself "done." Used to live inside
`work-items/`'s plugin-territory schema (§8); it's core now — its own
top-level `workflows/` folder, sibling of `reconciliations/`, always
present, full INV-20 treatment, no plugin required (`INVARIANTS.md`
INV-24).

**Its purpose is to be referenced, not just filed.** A core entity may
optionally name a `WORKFLOW-` by ID to guide its own process — `RECON-`
reconciliation is the first to do this (§16's optional `Workflow`
field): when a case names one, the resolver reads its `## Steps`/
`## Gates / exit criteria` before choosing a `/reconcile` verb, the same
way a documented procedure guides a human through an otherwise
ambiguous judgment call. Most reconciliations won't need one — `/reconcile`'s
fixed verb set already *is* the procedure for the ordinary case; a
`Workflow` is for a project that wants a documented, repeatable
escalation path for a specific recurring kind of conflict.

No dedicated creation command (no `/create-workflow` in core) — like
`RECON-`, a workflow is authored occasionally, not through a frequent,
form-driven flow; an agent creates one ad hoc from
`templates/workflow.template.md` and registers it in `workflows/workflows.md`
the same way any other artifact type's instance gets registered.

## 20. `rr-META-000020-Tc0nvEx1` Entity IDs carry their signer's userid

Once a registered user has a `userid` (§11, INV-26), every rule,
`WORKFLOW-`, `RECON-`, and active-module `<PREFIX>-` ID carries that
user's `userid` as a trailing `-XXXXXXXX` segment — always the final segment of the id, after any type-specific suffix a section
above already defines (a rule's `[-parent-id]`, §3). Assigned once, at
the same moment the entity's `Signed-off-by` (or, for a rule, the
authorship resolved below) is determined; never reassigned, never
changed if the signer is later deactivated or their role changes — the
same immutability posture `Signed-off-by` itself already has (§11).

**Hard ordering.** No entity may be assigned a suffixed id until its
signer already has a `userid`. Never generate a userid and an entity
suffix in the same breath if the signer isn't already registered with
one — register the user first, confirm the `userid` exists, then
proceed.

**For a type with a resolvable signer** (every type above except
rules): the `userid` is exactly that resolved signer's — the same
person `rules-of-development.md` §2's signer-resolution procedure names
in `Signed-off-by`. No separate lookup, no separate decision.

**For a rule** (and, by extension, a domain's own code, which is
never suffixed — see below): no rule or domain template carries an
authorship field of any kind, so there is nothing today recording who
added a given rule. Until a dedicated field is designed, use the sole
registered active user; if more than one is active, use whichever was
most recently registered. **This is a known, documented limitation**,
not a permanent design choice — a deployment with real multi-author
rule authorship will get an inaccurate attribution under this fallback,
and should treat adding a real per-rule authorship field as its own
future tracked maintenance item once that limitation actually bites.

**Domains are out of scope.** A domain has no numeric sequence — it's
identified by its `CODE` alone (§7), embedded as a substring inside
every rule id that cites it. There is no id to suffix.

**Cross-reference impact.** Renaming an id (retroactive migration, or
the initial rollout of this rule) means updating every place that id is
cited by exact string: its own heading/field, its type's index/catalog
row, every structured cross-reference field (`Targets`, `Entity`,
`Workflow`, and every `ref` field the active module's ETDs define), and
every free-text citation in `## Related`/`## Notes`/prose — there is no
dedicated cross-reference-checking script today (`/check-rules` and
`/audit` are agent-judgment procedures), so this is the agent's
responsibility to verify by direct search, not something CI catches
automatically. A rename must never touch `development/journal.jsonl`
(INV-17 — append-only; historical entries correctly keep citing the
pre-rename form forever), nor hand-edit any machine-regenerated report
(INV-14) — regenerate it with its own command after the rename instead.

## 21. `rr-META-000021-Tc0nvEx1` — owned by the active module

`rr-META-000021-Tc0nvEx1` — owned by the active module (`MODULE-SPECIFICATION.md`
§6.1); never reused.

## 22. `rr-META-000022-Tc0nvEx1` — owned by the active module

`rr-META-000022-Tc0nvEx1` — owned by the active module (`MODULE-SPECIFICATION.md`
§6.1); never reused.

## 23. `rr-META-000023-Tc0nvEx1` Artifact updates happen atomically, as work happens

Every catalyst artifact — an active-module artifact's own record, a
`Status` field, a journal entry — is updated **as the work it describes
actually happens**, at the smallest atomic unit practical, not
reconstructed retroactively in one batch once work is already done. This
applies to every artifact update, whether the agent or a user is
narrating their own manual work: an artifact recording a unit of work is
opened when that work starts and closed when it finishes, not
backfilled after the fact (the active module's meta-rules may state
this narrowly for its own entity types); a journal entry is appended as each
qualifying action completes (§12), never accumulated and appended in
bulk at session end; a `Status` field moves the moment the real-world
state it tracks moves.

**Delayed, batched updating is allowed — but only when explicitly
stated before the work begins.** Whoever is about to do the work (agent
or human) says so up front — "I'll batch these updates and record them
afterward" — before starting, not as a retroactive justification once
the work is already underway or finished. Absent that explicit
statement, real-time, atomic updating is the default; silently
batching bookkeeping for later convenience is not a judgment call left
to the agent.

**Added 2026-09-20**
(`framework/kernel/migrations/0.32.0/atomic-artifact-updates.md`).
Behavioural only — no existing artifact's shape or content changes;
nothing here to retroactively backfill.

---

### From module software-engineering

## Addendum to §6 (`rr-META-000006-Tc0nvEx1`): the development-artifact ID scheme

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

## Addendum to §7 (`rr-META-000007-Tc0nvEx1`): domains proposed by development work

A bug or requirement is not required to fit an existing domain — it may
propose a new one, but only by following the kernel's §7 standard, in
every rule document.

## 9. `rr-META-000009-Tc0nvEx1` Feature entries have their own, non-rule-linked scheme

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

- §1 (`rr-META-000001-Tc0nvEx1`)'s conflict check,
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

## 10. `rr-META-000010-Tc0nvEx1` Roadmap items have their own, source-tracked scheme

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

- §1 (`rr-META-000001-Tc0nvEx1`)'s conflict check,
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

## Addendum to §11 (`rr-META-000011-Tc0nvEx1`): signed module entities

Every development artifact (`BUG-`/`REQ-`/`HK-`/`TEST-`), feature entry,
roadmap item and step carries a `Signed-off-by` field recording the
outcome of the kernel's advisory signer check (§11), and its signer's
`userid` as its id suffix (§20). A named roadmap is retired in place,
never deleted (§10) — the same "never delete, retire in place" principle
§11 applies to `/user-remove`.

## Addendum to §12 (`rr-META-000012-Tc0nvEx1`): journal entries for module entities

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

## Addendum to §13 (`rr-META-000013-Tc0nvEx1`): module artifacts in a shared deployment

- **Union-merged indexes.** The indexes of this module's per-file types —
  `requirements.md`, `bugs.md`, `house-keeping.md`, `tests.md`,
  `steps.md` and `features.md` — merge by union and are regenerated by
  `catalyst criterion push`.
- **Not union-merged.** Roadmap files and `roadmaps.md` (free-form
  tables) and `development/BACKLOG.md` merge normally: concurrent edits
  to the same lines stop the push for a human to resolve.
  `/show-backlog` regenerates `BACKLOG.md` after a sync.

## Addendum to §15 (`rr-META-000015-Tc0nvEx1`): where this module's artifact types sit

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

## Addendum to §16 (`rr-META-000016-Tc0nvEx1`): reconciliation and module artifacts

A `RECON-` is exempt from the chain invariant's
epic→story→task→`REQ`/`BUG`/`HK`→rule requirement. Its file is edited in
place across its lifecycle the same way `BUG-`/`REQ-` files already are.

## Addendum to §19 (`rr-META-000019-Tc0nvEx1`): workflows for module processes

A typical module workflow documents, for example, how a bug moves from
triage to resolution.

## Addendum to §20 (`rr-META-000020-Tc0nvEx1`): module IDs carry their signer's userid

- Every `BUG-`/`REQ-`/`HK-`/`TEST-`, `FEAT-`, `RM-` and `STEP-` ID
  carries its signer's `userid` as the trailing segment, exactly like the
  kernel's own entities; each has a resolvable signer.
- The rule-authorship limitation §20 documents should be tracked as its
  own future `HK-` item once it actually bites.
- A rename also updates this module's structured cross-reference fields:
  `Feature`, `Roadmap`, `Requirement(s)`, `Steps`, `Tests`, `Linked`.
- A rename never hand-edits `development/BACKLOG.md` (INV-14 —
  machine-regenerated); run `/show-backlog` after the rename instead.

## 21. `rr-META-000021-Tc0nvEx1` Steps record a requirement's or bug's actual implementation work

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

- §1 (`rr-META-000001-Tc0nvEx1`)'s conflict check,
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

## 22. `rr-META-000022-Tc0nvEx1` Tests are development artifacts that may verify requirements and/or steps

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

## Addendum to §23 (`rr-META-000023-Tc0nvEx1`): steps are recorded as work happens

A step (§21) is opened when its unit of work starts and closed when it
finishes, not backfilled after the fact — `STEP-NNNNNN`'s own definition
states this narrowly ("opened as work on its parent actually starts, not
in advance of it"); the kernel's §23 generalizes the same posture to
every artifact update.
