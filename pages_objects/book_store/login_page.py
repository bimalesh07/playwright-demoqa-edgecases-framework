from pages_objects.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self._home_book_store_card = 'h5:has-text("Book Store Application")'
        self._login_menu_item = '//span[text()="Login"]'
        self._username_input = "#userName"
        self._password_input = "#password"
        self._login_button = "#login"
        self._error_msg = "#name"
        self._user_label = "#userName-value"
        self._logout_button = "//button[text()='Logout']"

    
    def navigate_to_login_page_via_ui(self):
        self.logger.info("Navigating to Login Page via UI...")
        self.click_element(self._home_book_store_card)
        self.click_element(self._login_menu_item)

    def login(self, username, password):
        self.logger.info(f"Attempting login for user: {username}")
        self.fill_text(self._username_input, username)
        self.fill_text(self._password_input, password)
        self.click_element(self._login_button)

    def verify_login_error(self):
        return self.assert_element(self._error_msg)

    def verify_logged_in_user(self):
        return self.assert_element(self._user_label)

    def verify_logout_button(self):
        return self.assert_element(self._logout_button)