from playwright.sync_api import Page, expect
from utils.custom_logger import CustomLogger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = CustomLogger.get_logger()

    def navigate_to(self, url: str):
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url, wait_until="load")

    def click_element(self, selector: str):
        self.logger.info(f"Clicking on element: {selector}")
        self.page.locator(selector).click()

    def fill_text(self, selector: str, value: str):
        self.logger.info(f"Entering '{value}' into element: {selector}")
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        text = self.page.locator(selector).text_content()
        self.logger.info(f"Retrieved text '{text}' from element: {selector}")
        return text.strip() if text else ""
    
    #assertion
    def assert_element(self, selector: str):
        """Logs the action and returns the Playwright Locator object."""
        self.logger.info(f"Getting locator for assertion on element: {selector}")
        return self.page.locator(selector)


    # def assert_element_has_text(self, selector: str, expected_text: str):
    #     self.logger.info(f"Asserting element '{selector}' contains text: '{expected_text}'")
    #     expect(self.page.locator(selector)).to_have_text(expected_text)

    # def assert_url_contains(self, expected_url_part: str):
    #     self.logger.info(f"Asserting current URL contains: '{expected_url_part}'")
    #     expect(self.page).to_have_url(lambda url: expected_url_part in url)