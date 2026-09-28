"""tempconv — convert temperatures between Celsius and Fahrenheit.

A deliberately small program, governed by catalyst: every behaviour below
is a documented rule (see .criterion/rules/conversion-rules.md), so
"why does this line exist?" always has an answer.
"""
from __future__ import annotations

import sys

ABSOLUTE_ZERO_C = -273.15


def c_to_f(celsius: float) -> float:
    # cv-CONV-000001-Tc0nvEx1: F = C x 9/5 + 32, rounded to one decimal place.
    return round(celsius * 9 / 5 + 32, 1)


def f_to_c(fahrenheit: float) -> float:
    # cv-CONV-000001-Tc0nvEx1 (inverse): C = (F - 32) x 5/9, rounded to one decimal place.
    return round((fahrenheit - 32) * 5 / 9, 1)


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1][-1:].upper() not in ("C", "F"):
        print("usage: tempconv <value>C|<value>F", file=sys.stderr)
        return 1
    value, unit = float(argv[1][:-1]), argv[1][-1].upper()
    celsius = value if unit == "C" else f_to_c(value)
    if celsius < ABSOLUTE_ZERO_C:
        # cv-CONV-000002-Tc0nvEx1: below absolute zero is rejected with exit code 2.
        print("below absolute zero", file=sys.stderr)
        return 2
    print(f"{c_to_f(value)}F" if unit == "C" else f"{f_to_c(value)}C")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
