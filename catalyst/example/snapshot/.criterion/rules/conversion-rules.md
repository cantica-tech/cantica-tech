# Conversion rules

Prefix: `cv`. How tempconv converts temperatures.

## Contents

- [`CONV`](#conv) — `cv-CONV-000001-Tc0nvEx1`, `cv-CONV-000002-Tc0nvEx1`

## `CONV`

> **Domain:** `CONV` — see [domains/cv-CONV-conversions.md](domains/cv-CONV-conversions.md).

### `cv-CONV-000001-Tc0nvEx1` Celsius and Fahrenheit convert with one decimal

✅ working. F = C × 9/5 + 32 and C = (F − 32) × 5/9, each rounded to one
decimal place. Implemented: `tempconv.py` (`c_to_f`, `f_to_c`). Tested:
`tests/test_tempconv.py` (`test_c_to_f_rounds_to_one_decimal`,
`test_f_to_c_is_the_inverse`).

### `cv-CONV-000002-Tc0nvEx1` Below absolute zero is refused

✅ working. An input below −273.15 °C (in either unit) is refused with exit
code 2. Implemented: `tempconv.py` (`main`). Tested:
`tests/test_tempconv.py` (`test_below_absolute_zero_is_rejected`).

## Linked Artifacts — Quick Index

- `REQ-000001-Tc0nvEx1` → `cv-CONV-000001-Tc0nvEx1`, `cv-CONV-000002-Tc0nvEx1`
- `BUG-000001-Tc0nvEx1` → `cv-CONV-000001-Tc0nvEx1`
