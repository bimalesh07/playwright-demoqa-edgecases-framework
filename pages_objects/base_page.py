# page_objects/base_page.py
from playwright.sync_api import Page, Locator
from utils.custom_logger import CustomLogger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = CustomLogger.get_logger()

    def navigate_to(self, url: str):
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url, wait_until="load")

    def click_element(self, selector: str):
        self.logger.info(f"Clicking element with locator: '{selector}'")
        self.page.locator(selector).click()

    def fill_text(self, selector: str, value: str):
        self.logger.info(f"Entering text '{value}' into field: '{selector}'")
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        text = self.page.locator(selector).text_content()
        self.logger.info(f"Retrieved text '{text}' from locator: '{selector}'")
        return text.strip() if text else ""

    def is_visible(self, selector: str) -> bool:
        visible = self.page.locator(selector).is_visible()
        self.logger.info(f"Element '{selector}' visibility state: {visible}")
        return visible

    def handle_iframe(self, frame_selector: str) -> Page:
        self.logger.info(f"Switching context to iFrame: {frame_selector}")
        return self.page.frame_locator(frame_selector)