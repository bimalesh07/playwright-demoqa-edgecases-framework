
from pages_objects.base_page import BasePage

class BookStorePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self._search_box = "#searchBox"
        self._table_rows = ".rt-tr-group"
        self._book_store_menu = '//span[text()="Book Store"]'

    def navigate_to_book_store_via_ui(self):
        self.logger.info("Navigating to Book Store Page via UI...")
        self.click_element('h5:has-text("Book Store Application")')
        self.click_element(self._book_store_menu)

    def search_book(self, book_title: str):
        self.logger.info(f"Searching for book: '{book_title}'")
        self.fill_text(self._search_box, book_title)

    def select_book_by_title(self, book_title: str):
        self.logger.info(f"Clicking on book: '{book_title}'")
        book_link = f'//a[text()="{book_title}"]'
        self.click_element(book_link)

    def verify_book_title_link(self, book_title: str):
        return self.assert_element(f'//a[text()="{book_title}"]')