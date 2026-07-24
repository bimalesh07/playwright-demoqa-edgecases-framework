from playwright.sync_api import Page


def navigate_to(page: Page, url: str) -> None:
    page.goto(url)


def page_title_contains(page: Page, text: str) -> bool:
    return text in page.title()
