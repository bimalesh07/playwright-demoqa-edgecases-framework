import pytest
from pages_objects.book_store.register_page import RegisterPage
from playwright.sync_api import expect

class TestRegisterPage:

    def test_register_via_ui_navigation(self, ui_page):
        register_page = RegisterPage(ui_page)

        # Updated to match your exact method name
        register_page.navigate_to_register_page_via_ui()

        register_page.fill_registration_form(
            first_name="John",
            last_name="Doe",
            username="jhndoe123o",
            password="Password@123"
        )
        ui_page.wait_for_timeout(5000)
        expect(register_page.verify_registration()).to_be_visible()
        expect(register_page.verify_registration()).to_have_text("Please verify reCaptcha!")
