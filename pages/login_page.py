from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
       user_email_address = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
       user_email_address.send_keys(email)
       user_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
       user_password.send_keys(password)
       user_password_repeat = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
       user_password_repeat.send_keys(password)
       register_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
       register_btn.click()
    

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert login_form , "Login form not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        registration_form = self.browser.find_elements(*LoginPageLocators.REGISTRATION_FORM)
        assert registration_form , "Registration form not found"	        