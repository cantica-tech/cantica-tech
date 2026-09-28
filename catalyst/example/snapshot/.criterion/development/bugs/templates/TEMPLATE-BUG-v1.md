# `BUG-NNNNNN` — descriptive title

| Field | Value |
|---|---|
| **ID** | `BUG-NNNNNN-<userid>` — the userid suffix is the resolved signer's (`Rules-of-Rules.md` §20) |
| **Name** | short descriptive summary of the entity's purpose/impact, e.g. `password-reset-link-expired` — follows Rules of Rules naming conventions |
| **Filename** | descriptive kebab-case filename, e.g. `BUG-000012-Ab3xR9pQ-password-reset-link-expired.md` — prefer specific problem/context over generic labels like `bug.md` or `auth-issue.md` |
| **Status** | exactly one of `Open` / `Under Review` / `Fixed` / `Closed` / `WontFix` (the bug ETD's `allowed_values`; starts `Open`; `Closed` and `WontFix` are its closed states). A duplicate is closed `WontFix`, naming the original `BUG-` under Related |
| **Severity** | exactly one of `Critical` / `High` / `Medium` / `Low` — a closed list, no other value; see scale below. **Required.** |
| **Opened** | YYYY-MM-DD |
| **Targets** | one or more rule IDs this bug violates — **required, never empty** (see `CODE-OF-CONDUCT.md` §1) |
| **Domain** | the `DOMAIN` code(s) of the targeted rule(s), from `rules/domains/` |
| **Area** | short free-text area label |
| **Steps** | `STEP-NNNNNN` list, in creation order, opened against this bug (`Rules-of-Rules.md` §21) — optional for a bug (fix tier, `CODE-OF-CONDUCT.md` §3); if any are listed, the bug does not move to a closed state (`Closed`/`WontFix`) until every listed step is `done` or `abandoned` (`Rules-of-Rules.md` §21) |
| **Signed-off-by** | name of the registered user (`IAM/users/users.json`) who signed this bug — see `CODE-OF-CONDUCT.md` §2 |

## Severity scale

Pick exactly one of these four values:

- **Critical** — data loss/corruption (silent or irreversible), a
  security exposure, or a failure that permanently disables a whole
  subsystem for the rest of the process's uptime (no self-recovery).
- **High** — a functional break with no workaround, or silent data
  divergence/staleness that looks healthy but isn't.
- **Medium** — validation/UX gap with a workaround, or a functional
  break confined to an edge case.
- **Low** — cosmetic, or test-coverage/tech-debt with no observed user
  impact yet.

## Description

What's wrong, in terms of the targeted rule(s) — not just symptoms.

## Reproduction

Concrete steps or inputs that trigger it. Cite a failing/missing test if
one exists.

## Expected vs actual

- **Expected** (per the targeted rule): …
- **Actual**: …

## Root cause

`file:line` pointer(s) once known.

## Fix plan

Whether the fix changes the implementation (rule stays as-is) or the rule
itself (subject to `Rules-of-Rules.md` §1 conflict check first).

## Test plan

The specific test (existing or new) that will cover this once fixed.
Guidance, not a tool-enforced closing condition: name the test here
before moving the bug to `Closed`, per the module's test rules
(`CODE-OF-CONDUCT.md` §3).

## Related

Other `BUG-`/`REQ-`/`HK-`/`STEP-`/`TEST-` IDs, or rule IDs.
