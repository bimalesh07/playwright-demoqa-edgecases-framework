# DemoQA Playwright Framework (Python)

## Project structure

- `tests/` - Playwright test files
- `pages/` - Page object models
- `utils/` - helper utilities and shared functions
- `results/` - test output and reports

## Setup

1. Create and activate a Python virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

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

## Notes

- `conftest.py` provides Playwright fixtures for browser and page objects.
- Use `tests/` for test cases, `pages/` for POM classes, and `utils/` for shared helpers.
