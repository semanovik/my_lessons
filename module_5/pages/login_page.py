from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'There is no login in URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password.send_keys('fakepassword')
        password_check = self.browser.find_element(*LoginPageLocators.PASSWORD_CHECK_INPUT)
        password_check.send_keys('fakepassword')
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        submit_button.click()
