from .main_page import MainPage
from .locators import LoginPageLocators
import time


class LoginPage(MainPage):

    def correct_fill_inputs(self):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)

        email_input.send_keys('semasema@gmail.com')
        password_input.send_keys('328225328225')
        submit_button.click()

    def reg_new_user(self):
        reg_email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        reg_password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        reg_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_SUBMIT_INPUT)
        reg_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)

        reg_email_input.send_keys(str(time.time()) + "@sema.ru")
        reg_password_input.send_keys('328225328225')
        reg_password_confirm.send_keys('328225328225')
        reg_submit_button.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Register form is not presented'

    def should_be_forgot_pass_link(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_LINK), 'Forgot password' \
                                                                                         'link is not ' \
                                                                                         'presented '

    def should_be_submit_button(self):
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), 'Submit button is not presented'

    def should_be_submit_registration_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), 'Submit registration ' \
                                                                                               'button is not ' \
                                                                                               'presented '

    def should_be_login_input(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_password_input(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), 'Password input is not presented'

    def should_be_to_login_in(self):
        self.should_be_login_form()
        self.should_be_forgot_pass_link()
        self.should_be_submit_button()
        self.should_be_login_input()
        self.should_be_password_input()

