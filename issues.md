# Static Code Analysis - Issues and Fixes

## Issue Table

| Issue | Type | Line(s) Before Fix | Description | Fix Approach |
|---|---|---|---|---|
| Missing module docstring | Code Quality (Pylint C0114) | 1 | The Python module did not explain its purpose. | Added a module-level docstring describing the scholarship disbursement program. |
| Long lines | Style (Pylint C0301) | 5, 10 | Some lines exceeded the recommended maximum length. | Reformatted long SQL statements and split expressions across multiple lines. |
| SQL string formatting | Code Quality (Pylint C0209) | 10 | SQL statements used string formatting instead of parameterized queries. | Replaced string formatting with SQL placeholders and parameter tuples. |
| Global statement | Maintainability (Pylint W0603) | 14 | The disbursement function modified a global variable, making state harder to manage. | Removed the global accumulator and returned the disbursed amount directly. |
| Broad exception handling | Code Quality (Pylint W0718) | 27 | A broad exception handler could hide unexpected errors. | Removed the unnecessary exception-handling demonstration and replaced the unsafe archive operation with a simple completion message. |
| Inconsistent function naming | Style (Pylint C0103) | 31 | The function name bySchemeCount did not follow Python naming conventions. | Renamed the function to by_scheme_count. |
| Incorrect None comparison | Code Quality (Pylint C0121) | 32 | The code compared a value with None using equality. | Changed the comparison to use the identity check: is None. |
| Missing function docstrings | Maintainability (Pylint C0116) | Multiple | Functions did not adequately describe their purpose. | Added docstrings to explain each function's responsibility. |

## Verification Summary

- Pylint final score: 10.00/10.
- Flake8: Passed with no reported violations.
- Bandit: No issues identified.
- Git whitespace check: Passed.

The original line numbers refer to the code before the fixes. The final line numbers may differ because the code was reformatted and refactored.
