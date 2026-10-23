# Lab 5: Static Code Analysis

## 1. Objective

The objective of this lab was to improve the code quality, security, and formatting of a Python program using three static analysis tools: Pylint, Bandit, and Flake8. The assigned program, `blood_donation.py`, simulates a basic blood donation management system.

## 2. Tools Used

- **Pylint:** Identifies code quality issues, naming convention violations, missing documentation, and potential programming problems.
- **Bandit:** Detects potentially insecure coding practices and common security vulnerabilities in Python programs.
- **Flake8:** Checks Python code formatting and compliance with style conventions, including whitespace, blank lines, and line length.
- **Git and GitHub:** Used for version control, committing changes, and uploading the completed work.
- **GitHub Actions:** Used to automate the execution of the program and static analysis tools.

## 3. Description of the Program

The `blood_donation.py` program simulates basic blood donation management operations. It provides functions to register donors, check donation eligibility, record donations, update blood stock, calculate available units for recipient blood groups, and identify blood groups with low stock.

The program uses Python lists and dictionaries to store donor information and blood stock during execution.

## 4. Initial Analysis

The three static analysis tools were run against the original Python source file.

### 4.1 Pylint Findings

The initial Pylint score was **4.81/10**.

Issues included:
- Missing module and function docstrings.
- Function and argument names that did not follow Python naming conventions.
- A mutable default argument (`notes=[]`).
- An overly broad exception handler.
- Unnecessary membership comparisons.

### 4.2 Bandit Findings

Bandit initially identified four findings:

1. **Hardcoded password:** A demo password was stored directly in the source code.
2. **Use of assert:** An assertion was used for blood group validation.
3. **Insecure temporary file creation:** The program used `tempfile.mktemp()`.
4. **Shell command execution:** The program used `os.system()` to construct an SMS command.

### 4.3 Flake8 Findings

The initial Flake8 report showed four violations:

- **E501:** Line exceeded the permitted length.
- **E303:** Too many blank lines.
- **E261:** Insufficient spacing before an inline comment.
- **E225:** Missing whitespace around an operator.

## 5. Issues Fixed

The source code was updated to address the findings identified by the tools.

| Issue | Fix applied |
|---|---|
| Hardcoded password | Changed password configuration to use an environment variable. |
| Assertion-based validation | Replaced `assert` with explicit validation and `ValueError`. |
| Unsafe temporary file creation | Replaced `tempfile.mktemp()` with `tempfile.NamedTemporaryFile()`. |
| Shell command execution | Removed shell command construction; the SMS helper now reports the recipient count without sending messages. |
| Mutable default argument | Changed the default from `[]` to `None` and initialized a new list inside the function. |
| Naming violations | Converted function and argument names to snake_case. |
| Missing docstrings | Added documentation to the module and functions. |
| Broad exception handling | Replaced broad exception handling with explicit input validation. |
| Formatting violations | Corrected line length, blank lines, comment spacing, and operator spacing. |

## 6. Final Analysis Results

After modifying the Python source file, the program and static analysis tools were executed again.

| Tool | Initial result | Final result |
|---|---|---|
| Pylint | 4.81/10 | 10.00/10 |
| Bandit | 4 findings | No issues identified |
| Flake8 | 4 reported violations | Successful GitHub Actions check |

The final Flake8 violation count should be verified using `reports/after/flake8_report.txt`.

## 7. Conclusion

This lab demonstrated how static analysis tools can help improve the quality, security, and maintainability of Python programs. Pylint helped identify code quality issues, Bandit identified potentially unsafe coding practices, and Flake8 identified formatting violations.

The code was modified based on the findings, and GitHub Actions was configured to automate the checks. The successful workflow run demonstrated that the configured analysis pipeline executed successfully.

---

# Reflection Questions and Answers

## 1. What is static code analysis?

Static code analysis is the process of examining source code without executing its normal functionality. It helps identify potential bugs, security vulnerabilities, poor programming practices, and formatting violations.

## 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint focuses on code quality, programming practices, naming conventions, and documentation. Bandit focuses on common security vulnerabilities in Python code. Flake8 checks coding style and formatting, including whitespace and line length.

## 3. What problems did you identify in the original program?

The original program contained missing docstrings, inconsistent naming conventions, a mutable default argument, broad exception handling, a hardcoded password, assertion-based validation, insecure temporary-file creation, shell command execution, and formatting violations.

## 4. Why is using a mutable default argument a problem?

A mutable default argument, such as `notes=[]`, is created once when the function is defined. If the list is modified, later calls may reuse the same list. Using `None` as the default and creating a new list inside the function avoids this problem.

## 5. Why should assertions not be used for input validation?

Assertions can be disabled when Python runs with optimization. Explicit conditional checks and exceptions, such as `ValueError`, are more appropriate for validating user input and handling invalid values.

## 6. Why is shell command execution potentially dangerous?

Functions such as `os.system()` execute commands through a shell. If variable input is incorporated into a command, an attacker may be able to inject unintended commands. Avoiding shell-based execution reduces this risk.

## 7. How did static analysis improve the program?

Static analysis identified issues that could affect code readability, maintainability, security, and consistency. Fixing the reported problems improved the Pylint score and removed the findings reported by Bandit in the final local scan.

## 8. What is the purpose of before-and-after reports?

Before-reports preserve the original findings, while after-reports document the results following code changes. Comparing them provides evidence of the improvements made.

## 9. What is GitHub Actions, and why was it used?

GitHub Actions is an automation platform that runs predefined workflows in response to events such as pushes and pull requests. It was used to automatically execute the Python program and the three static analysis tools and upload the reports.

## 10. What did you learn from this lab?

I learned how to use Pylint, Bandit, and Flake8 to identify different categories of issues in Python code. I also learned how to fix common programming and security problems, maintain before-and-after reports, use Git for version control, and automate code analysis with GitHub Actions.

