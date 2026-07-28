from pages_objects.base_page import BasePage
class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #Navigation Locators
        self._home_book_store_card = 'h5:has-text("Book Store Application")'
        self._login_menu_item = '//span[text()="Login"]'
        self._new_user_button = "#newUser"

        #Form Input Locators
        self._firstname_input = "#firstname"
        self._lastname_input = "#lastname"
        self._username_input = "#userName"
        self._password_input = "#password"
        self._register_button = "#register"
        self._back_to_login_button = "#gotologin"

    def navigate_to_register_page_via_ui(self):
        self.logger.info("Navigating to Register Page via UI...")
        self.click_element(self._home_book_store_card)
        self.click_element(self._login_menu_item)
        self.click_element(self._new_user_button)

    def fill_registration_form(self, first_name, last_name, username, password):
        self.logger.info("Filling registration form...")
        self.fill_text(self._firstname_input, first_name)
        self.fill_text(self._lastname_input, last_name)
        self.fill_text(self._username_input, username)
        self.fill_text(self._password_input, password)
        self.click_element(self._register_button)

    def click_back_to_login(self):
        self.click_element(self._back_to_login_button)


    def verify_registration(self):
        return self.assert_element(self._captcha_error_msg)