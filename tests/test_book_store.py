import re
import pytest
from playwright.sync_api import expect
from pages_objects.book_store.book_store_page import BookStorePage

class TestBookStorePage:

    def test_search_and_verify_book(self, ui_page):
        book_store_page = BookStorePage(ui_page)
        book_store_page.navigate_to_book_store_via_ui()

        target_book = "Git Pocket Guide"
        book_store_page.search_book(target_book)
        expect(book_store_page.verify_book_title_link(target_book)).to_be_visible()


    def test_search_non_existing_book(self, ui_page):
        book_store_page = BookStorePage(ui_page)
        book_store_page.navigate_to_book_store_via_ui()

        invalid_book = "NonExistentBook999"
        book_store_page.search_book(invalid_book) 

        expect(book_store_page.verify_book_title_link(invalid_book)).not_to_be_visible()



    def test_navigate_to_book_details(self, ui_page):
        book_store_page = BookStorePage(ui_page)
        book_store_page.navigate_to_book_store_via_ui()

        target_book = "Learning JavaScript Design Patterns"
        book_store_page.select_book_by_title(target_book)

        expect(ui_page).to_have_url(re.compile(r".*books\?(book|search)=.*"))