# `REQ-000001-Tc0nvEx1` — Convert temperatures between Celsius and Fahrenheit

| Field | Value |
|---|---|
| **ID** | `REQ-000001-Tc0nvEx1` |
| **Name** | `convert-temperatures` |
| **Filename** | `REQ-000001-convert-temperatures.md` |
| **Status** | Completed |
| **Opened** | 2026-09-28 |
| **Targets** | `cv-CONV-000001-Tc0nvEx1`, `cv-CONV-000002-Tc0nvEx1` |
| **Domain** | `CONV` |
| **Feature** | *(none)* |
| **Steps** | `STEP-000001-Tc0nvEx1` |
| **Tests** | `TEST-000001-Tc0nvEx1` |
| **Signed-off-by** | Example Maintainer |

## Summary

A command-line converter: `tempconv 100C` prints `212.0F`; `tempconv 212F` prints `100.0C`.

## Vetted against existing rules

No existing rule covers conversions; proposes `cv-CONV-000001-Tc0nvEx1` and `cv-CONV-000002-Tc0nvEx1` in the new `CONV` domain.
