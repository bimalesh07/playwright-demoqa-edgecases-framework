import pytest

from playwright.sync_api import Page


def test_basic_demoqa_page_loads(page: Page) -> None:
    page.goto("https://demoqa.com")
    assert "ToolsQA" in page.title()
