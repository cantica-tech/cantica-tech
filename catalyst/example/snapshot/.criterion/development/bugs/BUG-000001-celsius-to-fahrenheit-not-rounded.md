# `BUG-000001-Tc0nvEx1` — Celsius to Fahrenheit is not rounded

| Field | Value |
|---|---|
| **ID** | `BUG-000001-Tc0nvEx1` |
| **Name** | `celsius-to-fahrenheit-not-rounded` |
| **Filename** | `BUG-000001-celsius-to-fahrenheit-not-rounded.md` |
| **Status** | Closed |
| **Severity** | Low |
| **Opened** | 2026-09-28 |
| **Targets** | `cv-CONV-000001-Tc0nvEx1` |
| **Domain** | `CONV` |
| **Area** | `tempconv.py` |
| **Steps** | *(none — a fix needs no step)* |
| **Signed-off-by** | Example Maintainer |

`tempconv 36.6C` printed `97.88000000000001F`; `cv-CONV-000001-Tc0nvEx1` requires one decimal.
Fixed: `c_to_f` now rounds. `test_c_to_f_rounds_to_one_decimal` covers it.
