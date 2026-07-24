# Playwright Python Pytest Test Automation Framework

A production-ready UI Test Automation Framework engineered in **Python** using **Playwright** and **Pytest**. Designed to validate dynamic web components, UI edge cases, and browser interactions with automated logging, assertions, and screenshot capture on test failure.

---

## Key Features

- **Built-in Pytest Fixtures:** Powered by `pytest-playwright` for automated browser lifecycle and context management.
- **Custom Logging Utility:** Dual-output logging system printing formatted execution logs to both terminal console and log files (`logs/automation.log`).
- **Failure Screenshot Capture:** Automatic screenshot capture attached to `logs/screenshots/` upon test failure.
- **Complex UI Edge-Case Coverage:**
  - Dynamic JavaScript Alerts, Confirmations, and Prompts.
  - Multi-window / Tab switching and context handling.
  - Nested iFrames and Frame navigation.
  - File Uploads and Dynamic Downloads.
  - Modal Dialogs and dynamic DOM overlays.
- **HTML Reporting:** Automated execution test reports generation using `pytest-html`.

---

## Tech Stack & Dependencies

- **Language:** Python 3.10+
- **Test Runner:** Pytest
- **Browser Automation:** Playwright (Python Sync API)
- **Reporting:** pytest-html
- **API Utilities:** Requests

---

## Framework Structure

````text
├── utilities/
│   ├── __init__.py
│   └── custom_logger.py          # Centralized Custom Logging Utility
├── logs/                         # Execution log files & Failure screenshots
│   ├── automation.log
│   └── screenshots/
├── tests/
│   ├── conftest.py               # Pytest hooks, fixtures & auto screenshot capturing
│   └── test_demoqa.py            # Edge-case test suites (Alerts, Windows, iFrames)
├── pytest.ini                    # Pytest CLI & Logging configurations
├── requirements.txt              # Project dependencies
└── README.md                     # Framework Documentation

## Project structure

- `tests/` - Playwright test files
- `pages/` - Page object models
- `utils/` - helper utilities and shared functions
- `results/` - test output and reports

## Setup
1.Create and activate a Python virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
````

2. Install dependencies:

```bash
pip install -r requirements.txt
python -m playwright install
```

3. Run tests:

```bash
pytest
```

4. Generate an HTML report:

```bash
pytest --html=results/report.html
```
