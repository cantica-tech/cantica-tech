"""Rebuild the tempconv example — a small program governed by catalyst —
entirely through the catalyst CLI, into a fresh directory.

    python3 build.py <empty-dir> [--kernel DIR] [--module DIR] [--cli catalyst.pyz]

By default it uses the newest kernel and software-engineering module
releases next to this folder (../kernel/, ../modules/); catalyst 0.40.0 or
later is required (catalyst init, ceremony tiers). With a catalyst checkout,
pass --kernel <catalyst>/framework/kernel --module <module checkout>
--cli <catalyst>/dist/catalyst.pyz.
"""
import argparse, glob, os, re, shutil, subprocess, sys, tempfile, textwrap, datetime, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("out", type=Path)
ap.add_argument("--kernel", type=Path)
ap.add_argument("--module", type=Path)
ap.add_argument("--cli", type=Path)
args = ap.parse_args()
for name in ("kernel", "module", "cli"):           # relative to where the user ran us
    if getattr(args, name):
        setattr(args, name, getattr(args, name).resolve())


def newest(pattern):
    found = sorted(glob.glob(str(HERE.parent / pattern)),
                   key=lambda p: [int(x) for x in re.findall(r"v(\d+)\.(\d+)\.(\d+)", p)[-1]])
    if not found:
        raise SystemExit(f"no release matching {pattern}; pass --kernel/--module/--cli")
    return Path(found[-1])


def unzip(z):
    d = Path(tempfile.mkdtemp())
    zipfile.ZipFile(z).extractall(d)
    return d


KERNEL = args.kernel or unzip(newest("kernel/v*/kernel-v*.zip"))
MOD = args.module or unzip(newest("modules/software-engineering/v*/software-engineering-v*.zip"))
CLI = args.cli or (KERNEL / "bin" / "catalyst.pyz")
if not Path(CLI).is_file():
    raise SystemExit("this example needs catalyst 0.40.0 or later (catalyst init, ceremony tiers); the "
                     f"release found has no CLI ({CLI}). Pass --kernel/--module/--cli from a checkout.")
E = args.out.resolve()
E.mkdir(parents=True, exist_ok=True)
if any(E.iterdir()):
    raise SystemExit(f"{E} is not empty")
# before catalyst: just the project skeleton; the converter arrives as the feature
shutil.copy2(HERE / "app" / "pyproject.toml", E / "pyproject.toml")
os.chdir(E)
env = dict(os.environ)

def cat(*args):
    r = subprocess.run([sys.executable, str(CLI), *args], env=env, capture_output=True, text=True)
    if r.returncode: raise SystemExit(f"catalyst {' '.join(args[:3])}: {r.stdout}{r.stderr}")
    return r.stdout.strip()

def git(*a): subprocess.run(["git", *a], check=True, capture_output=True)
def w(p, t): Path(p).parent.mkdir(parents=True, exist_ok=True); Path(p).write_text(textwrap.dedent(t).lstrip())
def journal(cmd, action, art, tier, intent, files, targets=()):
    a = ["journal", "append", "--command", cmd, "--action", action, "--artifact", art, "--tier", tier,
         "--intent", intent]
    for t in targets: a += ["--target", t]
    for f in files: a += ["--file", f]
    cat(*a)

git("init", "-q"); git("config", "user.name", "Example Maintainer"); git("config", "user.email", "maintainer@example.invalid")
w("README.md", "# tempconv\n\nConvert temperatures: `python3 tempconv.py 100C`.\n")
git("add", "-A"); git("commit", "-q", "-m", "tempconv: project skeleton")
src = (HERE / "app" / "tempconv.py").read_text()

print(cat("init", "--name", "tempconv", "--module", "software-engineering", "--user", "Example Maintainer",
          "--git-username", "maintainer", "--rule-doc", "conversion-rules:cv", "--test-locations", "`tests/`",
          "--agent", "claude-code", "--kernel", str(KERNEL), "--module-dir", str(MOD),
          "--userid", "Tc0nvEx1"))   # a fixed userid so the IDs in README.md match every rebuild
C = Path(".criterion")
uid = __import__("json").loads((C / "IAM/users/users.json").read_text())["users"][0]["userid"]
today = datetime.date.today().isoformat()

# --- rules: the domain and two rules (tier: feature — new documented behaviour)
w(C / "rules/domains/cv-CONV-conversions.md", f"""
    # `CONV` — Temperature conversions

    **Document:** rules/conversion-rules.md
    **Name:** conversions
    **Defined:** {today}
    **Parent:** none
    **Sub-domains:** none

    ## Scope

    How tempconv converts between Celsius and Fahrenheit, and which inputs it refuses.
    """)
dom = C / "rules/domains/domains.md"
dom.write_text(dom.read_text() + f"| [`CONV`](cv-CONV-conversions.md) | rules/conversion-rules.md | {today} |\n")
R1, R2 = f"cv-CONV-000001-{uid}", f"cv-CONV-000002-{uid}"
w(C / "rules/conversion-rules.md", f"""
    # Conversion rules

    Prefix: `cv`. How tempconv converts temperatures.

    ## Contents

    - [`CONV`](#conv) — `{R1}`, `{R2}`

    ## `CONV`

    > **Domain:** `CONV` — see [domains/cv-CONV-conversions.md](domains/cv-CONV-conversions.md).

    ### `{R1}` Celsius and Fahrenheit convert with one decimal

    ✅ working. F = C × 9/5 + 32 and C = (F − 32) × 5/9, each rounded to one
    decimal place. Implemented: `tempconv.py` (`c_to_f`, `f_to_c`). Tested:
    `tests/test_tempconv.py` (`test_c_to_f_rounds_to_one_decimal`,
    `test_f_to_c_is_the_inverse`).

    ### `{R2}` Below absolute zero is refused

    ✅ working. An input below −273.15 °C (in either unit) is refused with exit
    code 2. Implemented: `tempconv.py` (`main`). Tested:
    `tests/test_tempconv.py` (`test_below_absolute_zero_is_rejected`).

    ## Linked Artifacts — Quick Index

    - `REQ-000001-{uid}` → `{R1}`, `{R2}`
    - `BUG-000001-{uid}` → `{R1}`
    """)
rules_md = C / "rules/rules.md"
rules_md.write_text(rules_md.read_text().replace("## Rule IDs\n\n*(none yet)*\n",
    f"## Rule IDs\n\n- `{R1}` — Celsius and Fahrenheit convert with one decimal\n- `{R2}` — Below absolute zero is refused\n")
    .replace("| `cv` | [`conversion-rules.md`](conversion-rules.md) | |", "| `cv` | [`conversion-rules.md`](conversion-rules.md) | `CONV` |"))

# --- feature: the converter itself (first version: c_to_f doesn't round yet)
Path("tempconv.py").write_text(src.replace("return round(celsius * 9 / 5 + 32, 1)", "return celsius * 9 / 5 + 32"))
Path("tests").mkdir(exist_ok=True)
shutil.copy2(HERE / "app" / "tests" / "test_tempconv.py", "tests/test_tempconv.py")
REQ, STEP, TEST = cat("id", "next", "REQ"), cat("id", "next", "STEP"), cat("id", "next", "TEST")
def table(rows): return "\n".join(f"| **{k}** | {v} |" for k, v in rows)
w(C / f"requirements/REQ-000001-convert-temperatures.md", f"""
    # `{REQ}` — Convert temperatures between Celsius and Fahrenheit

    | Field | Value |
    |---|---|
    {table([("ID", f"`{REQ}`"), ("Name", "`convert-temperatures`"), ("Filename", "`REQ-000001-convert-temperatures.md`"),
            ("Status", "Completed"), ("Opened", today), ("Targets", f"`{R1}`, `{R2}`"), ("Domain", "`CONV`"),
            ("Feature", "*(none)*"), ("Steps", f"`{STEP}`"), ("Tests", f"`{TEST}`"), ("Signed-off-by", "Example Maintainer")]).replace(chr(10), chr(10)+"    ")}

    ## Summary

    A command-line converter: `tempconv 100C` prints `212.0F`; `tempconv 212F` prints `100.0C`.

    ## Vetted against existing rules

    No existing rule covers conversions; proposes `{R1}` and `{R2}` in the new `CONV` domain.
    """)
w(C / f"steps/STEP-000001-implement-the-converter.md", f"""
    # `{STEP}` — Implement the converter

    | Field | Value |
    |---|---|
    {table([("ID", f"`{STEP}`"), ("Name", "`implement-the-converter`"), ("Filename", "`STEP-000001-implement-the-converter.md`"),
            ("Parent", f"`{REQ}`"), ("Status", "done"), ("Opened", today), ("Closed", today), ("Tests", f"`{TEST}`"),
            ("Signed-off-by", "Example Maintainer")]).replace(chr(10), chr(10)+"    ")}

    Wrote `tempconv.py` (`c_to_f`, `f_to_c`, `main`).
    """)
w(C / f"tests/TEST-000001-conversion-and-refusal.md", f"""
    # `{TEST}` — Conversion and refusal

    | Field | Value |
    |---|---|
    {table([("ID", f"`{TEST}`"), ("Name", "`conversion-and-refusal`"), ("Filename", "`TEST-000001-conversion-and-refusal.md`"),
            ("Status", "Passing"), ("Opened", today), ("Targets", f"`{R1}`, `{R2}`"), ("Domain", "`CONV`"),
            ("Requirements", f"`{REQ}`"), ("Steps", f"`{STEP}`"), ("Signed-off-by", "Example Maintainer")]).replace(chr(10), chr(10)+"    ")}

    `tests/test_tempconv.py`: one decimal both ways, and refusal below absolute zero.
    """)
cat("index", "regen")
journal("/create-req", "create", REQ, "feature",
        "Document the converter's behaviour as rules (CONV domain) and deliver it as a feature: requirement, "
        "its implementation step and its test.",
        [str(C / p) for p in ["rules/conversion-rules.md", "rules/rules.md", "rules/domains/domains.md",
         "rules/domains/cv-CONV-conversions.md", "requirements/REQ-000001-convert-temperatures.md",
         "requirements/requirements.md", "steps/STEP-000001-implement-the-converter.md", "steps/steps.md",
         "tests/TEST-000001-conversion-and-refusal.md", "tests/tests.md"]] + ["tempconv.py", "tests/test_tempconv.py"],
        targets=[R1, R2])

# --- fix: the test shows c_to_f doesn't round (rule R1): BUG, fixed
BUG = cat("id", "next", "BUG")
Path("tempconv.py").write_text(src)
w(C / "development/bugs/BUG-000001-celsius-to-fahrenheit-not-rounded.md", f"""
    # `{BUG}` — Celsius to Fahrenheit is not rounded

    | Field | Value |
    |---|---|
    {table([("ID", f"`{BUG}`"), ("Name", "`celsius-to-fahrenheit-not-rounded`"),
            ("Filename", "`BUG-000001-celsius-to-fahrenheit-not-rounded.md`"), ("Status", "Closed"),
            ("Severity", "Low"), ("Opened", today), ("Targets", f"`{R1}`"), ("Domain", "`CONV`"),
            ("Area", "`tempconv.py`"), ("Steps", "*(none — a fix needs no step)*"), ("Signed-off-by", "Example Maintainer")]).replace(chr(10), chr(10)+"    ")}

    `tempconv 36.6C` printed `97.88000000000001F`; `{R1}` requires one decimal.
    Fixed: `c_to_f` now rounds. `test_c_to_f_rounds_to_one_decimal` covers it.
    """)
cat("index", "regen")
journal("/create-bug", "create", BUG, "fix", f"Restore {R1}: c_to_f returned unrounded values.",
        ["tempconv.py", str(C / "development/bugs/BUG-000001-celsius-to-fahrenheit-not-rounded.md"),
         str(C / "development/bugs/bugs.md")], targets=[R1])

# --- chore: README wording — no artifact, one journal entry
Path("README.md").write_text("# tempconv\n\nConvert temperatures between Celsius and Fahrenheit: `python3 tempconv.py 100C`.\n")
journal("chore", "update", "README wording", "chore", "Clarify the README; no rule's behaviour changes.", ["README.md"])
print(cat("check"))
