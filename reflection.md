# Lab 5: Static Code Analysis - Reflection

## 1. What is the purpose of static code analysis?

Static code analysis examines source code to identify potential bugs, security risks, and style violations without executing the program. Pylint focuses on code quality and maintainability, Flake8 checks formatting and coding conventions, and Bandit identifies potentially unsafe coding patterns. Using these tools helps developers detect problems early.

## 2. What issues did you identify and fix?

The analysis identified problems including missing docstrings, long lines, inconsistent function naming, global state modification, and broad exception handling. I improved the code by adding documentation, following Python naming conventions, removing unnecessary global state, and simplifying the archive demonstration. I also improved SQL query handling by using parameterized statements.

## 3. How did static analysis improve the program?

Static analysis helped make the program easier to read, maintain, and review. The final Pylint score was 10.00/10, Flake8 passed, and Bandit reported no issues. These results indicate that the program meets the checks performed by the tools, although they do not guarantee that every possible logical error has been eliminated.

## 4. What are the limitations of static analysis?

Static analysis cannot guarantee that a program behaves correctly in every situation. Some logical errors depend on runtime inputs or application requirements and may not be detected by these tools. Therefore, static analysis should be combined with execution tests, code review, and appropriate functional testing.
