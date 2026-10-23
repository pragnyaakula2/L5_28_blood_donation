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


## Known Issue Table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Hardcoded password | Security | 4 | Password `"bloodbank-demo"` was stored directly in the source code. | Replaced the hardcoded value with the `OFFICER_PASSWORD` environment variable. |
| Assertion used for validation | Security | 18 | `assert bloodGroup in stock` was used for blood group validation. Assertions can be disabled under optimization. | Replaced the assertion with an explicit conditional check and `ValueError`. |
| Insecure temporary file | Security | 60 | `tempfile.mktemp()` generated a filename without securely creating the file. | Replaced it with `tempfile.NamedTemporaryFile()`. |
| Shell command execution | Security | 65 | `os.system()` executed an SMS command through a shell, potentially exposing the program to command injection. | Removed shell command construction. The helper now reports the recipient count without sending SMS. |
| Mutable default argument | Bug | 17 | `notes=[]` could cause multiple function calls to share the same list. | Changed the default to `None` and initialized a new list inside the function. |
| Missing module docstring | Code quality | 1 | The Python module lacked a descriptive docstring. | Added a module-level docstring describing the program. |
| Missing function docstrings | Code quality | 17, 27, 33, 42, 49, 53, 58, 63, 68 | Several functions lacked documentation. | Added descriptive docstrings to the functions. |
| Invalid naming conventions | Code style | 17, 27, 33, 42, 49, 53, 58, 63 | Function names and parameters used camelCase instead of snake_case. | Renamed identifiers, for example, `registerDonor` to `register_donor`. |
| Broad exception handling | Bug / Code quality | 45 | `except Exception` could catch unrelated errors and hide unexpected problems. | Removed broad exception handling and explicitly validated the blood group. |
| Excessive line length (E501) | Formatting | 78 | A line exceeded Flake8's 79-character limit. | Split the long line across multiple lines. |
| Excessive blank lines (E303) | Formatting | 58 | Too many blank lines appeared in the source code. | Removed unnecessary blank lines. |
| Inline comment spacing (E261) | Formatting | 43 | Insufficient spacing appeared before an inline comment. | Added the required spaces before the comment. |
| Operator whitespace (E225) | Formatting | 13 | An operator did not have the required surrounding whitespace. | Corrected the spacing around the operator. |


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


