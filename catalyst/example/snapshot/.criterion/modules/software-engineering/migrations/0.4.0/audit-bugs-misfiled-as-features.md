# Migration: audit `BUG-` items that were actually feature requests

> Target version: `0.4.0` — this is the migration that produces the shape
> `0.4.0` introduced. Triggered by `SYNCHRONIZE.md`'s "Version-specific
> one-time migrations" (`From 0.3.1`), applied together with the kernel's
> migrations in version order. Applies once, the first time a deployment's
> `version.txt` advances past `0.3.1`. Never re-run on a later sync once
> applied. (Moved here from the kernel's `SYNCHRONIZE.md` in kernel
> `0.36.0`.)

## What changed

This version introduced `features/` and made explicit that new feature
work belongs in a `REQ-NNNNNN` requirement, never a `BUG-NNNNNN` bug. A
project synchronized from a version at or below `0.3.1` may already contain
`BUG-` items that were filed for what was actually new/desired behavior
rather than an existing rule failing to hold.

## Steps

1. Read every file in `bugs/` (or the project's equivalent bugs directory).
2. For each one, judge whether its `Description`/`Root cause` describes
   behavior that used to work and regressed (a real bug) versus behavior
   that was never specified or built at all (a feature gap misfiled as a
   bug). A strong signal: a `Targets` rule whose status marker is ❌ "not
   implemented" rather than a regression from a previously ✅ rule.
3. Report every flagged item to the user rather than silently
   reclassifying it. For each one the user confirms, convert it to a
   `REQ-NNNNNN` using this module's `templates/requirement.template.md`
   (the deployed `requirements/templates/TEMPLATE-REQUIREMENT-vN.md`),
   preserving its original content and `Opened` date, then retire the
   `BUG-NNNNNN` in place per `Rules-of-Rules.md` §4 with a note pointing at
   the new `REQ-NNNNNN`.
4. Do not repeat this audit on later syncs once the deployed project's
   `version.txt` already reflects a version past `0.3.1`.
