import pytest
from playwright.sync_api import expect
from pages_objects.book_store.login_page import LoginPage
import re

class TestLoginPage:

    def test_login_valid_credentials(self, ui_page):
        login_page = LoginPage(ui_page)

        login_page.navigate_to_login_page_via_ui()

        valid_username = "johndoe123"
        valid_password = "Password@123"
        
        login_page.login(username=valid_username, password=valid_password)
        expect(login_page.verify_logged_in_user()).to_have_text(valid_username)
        
        expect(login_page.verify_logout_button()).to_be_visible()



    def test_login_invalid_credentials(self, ui_page):
        login_page = LoginPage(ui_page)
        login_page.navigate_to_login_page_via_ui()
        login_page.login(username="invalid_user_xyz", password="WrongPassword123!")


        expect(login_page.verify_login_error()).to_be_visible()
        expect(login_page.verify_login_error()).to_have_text("Invalid username or password!")