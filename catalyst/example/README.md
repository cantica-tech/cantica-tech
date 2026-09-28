# catalyst example: `tempconv`

A small temperature converter, governed by catalyst end to end. It shows the
one thing catalyst is for: **every line of behaviour answers "why does this
exist?" — from the code, to a documented rule, to the work that delivered it,
to the exact history of each change.**

- `app/` — the program before catalyst (source, tests).
- `snapshot/` — the same program after catalyst: the pointer
  (`tempconv.catalyst`) and the working copy (`.criterion/`), for reading. In a
  real project `.criterion` is gitignored or a submodule; here it is committed so
  you can read it. It has no git history, so run the commands below on a copy
  built with `build.py`, not on `snapshot/`.
- `build.py` — rebuilds `snapshot/` from scratch with the catalyst CLI, so you
  can run every command below against real history.

## Why does this line exist?

`snapshot/tempconv.py`, line 16:

```python
return round(celsius * 9 / 5 + 32, 1)
```

1. **The code names its rule** (line 15): `cv-CONV-000001-Tc0nvEx1`. The IDs
   are the same in every rebuild (`build.py` registers a fixed userid).
2. **The rule says what, and where it's implemented and tested**:
   `.criterion/rules/conversion-rules.md` — "F = C × 9/5 + 32 … rounded to one
   decimal place. Implemented: `tempconv.py` … Tested: `tests/test_tempconv.py`."
3. **The rule's Quick Index names the work that touched it**: the feature
   `REQ-000001-Tc0nvEx1` (with its step and test) and the fix `BUG-000001-Tc0nvEx1`.
4. **The fix explains the `round`**:
   `.criterion/development/bugs/BUG-000001-celsius-to-fahrenheit-not-rounded.md` —
   `tempconv 36.6C` printed `97.88000000000001F`.
5. **The journal records each change exactly** — who, why, and the content
   hash of every file before and after:

   ```
   catalyst init        the deployment
   feature /create-req  REQ-000001  rules, requirement, step, test, tempconv.py, tests
   fix     /create-bug  BUG-000001  tempconv.py: c_to_f now rounds
   chore   chore        README wording (no rule affected, no artifact)
   ```

## Try it

```sh
python3 build.py /tmp/tempconv          # needs catalyst 0.40.0+ releases next to this folder
cd /tmp/tempconv
python3 .criterion/bin/catalyst.pyz check                 # structure, chain, journal, indexes
python3 .criterion/bin/catalyst.pyz validate              # every reference resolves
python3 .criterion/bin/catalyst.pyz journal verify        # hash chain intact
# the code before the fix, straight from the journal (the fix entry's "before" hash)
python3 -c "import json; print([json.loads(l) for l in open('.criterion/development/journal.jsonl')][2]['files'][0]['before'])" | xargs git cat-file -p
T=$(python3 -c "import json; print([json.loads(l) for l in open('.criterion/development/journal.jsonl')][2]['timestamp'])")
python3 .criterion/bin/catalyst.pyz journal restore "$T" /tmp/after-fix   # every file as recorded by the fix
python3 .criterion/bin/catalyst.pyz spec create-bug       # what the agent reads for /create-bug
```

With a catalyst checkout instead of releases:
`python3 build.py /tmp/tempconv --kernel <catalyst>/framework/kernel --module
<catalyst-software-engineering> --cli <catalyst>/dist/catalyst.pyz`.

## Three tiers of ceremony

| Change | Tier | What it costs |
|---|---|---|
| The converter itself | feature | a requirement, a step, a test, rules |
| `c_to_f` didn't round | fix | one bug report targeting the rule |
| README wording | chore | one journal entry — no artifact |
