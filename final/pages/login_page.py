from .main_page import MainPage
from .locators import LoginPageLocators
import time


class LoginPage(MainPage):

    # Авторизация с валидными данными
    def correct_fill_inputs(self):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)

        email_input.send_keys('semasema@gmail.com')
        password_input.send_keys('328225328225')
        submit_button.click()

    # Авторизация с невалидным паролем
    def incorrect_fill_inputs(self):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)

        email_input.send_keys('semasema@gmail.com')
        password_input.send_keys('3282253282251234')
        submit_button.click()

    # Регистрация с допустимыми данными
    def reg_new_user(self):
        reg_email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        reg_password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        reg_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_SUBMIT_INPUT)
        reg_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)

        reg_email_input.send_keys(str(time.time()) + "@sema.ru")
        reg_password_input.send_keys('328225328225')
        reg_password_confirm.send_keys('328225328225')
        reg_submit_button.click()

    # Наличие формы для логирования
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    # Наличие формы для регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Register form is not presented'

    # Кнопка восстановления пароля
    def should_be_forgot_pass_link(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_LINK), 'Forgot password' \
                                                                                 'link is not ' \
                                                                                 'presented '

    # Кнопка подтверждения входа в аккаунт
    def should_be_submit_button(self):
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), 'Submit button is not presented'

    # Кнопка подтверждения регистрации
    def should_be_submit_registration_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), 'Submit registration ' \
                                                                                       'button is not ' \
                                                                                       'presented '

    # Наличие поля ввода пароля при регистрации
    def should_be_password_input(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), 'Password input is not presented'

    # Наличие всех элементов, необходимых для входа
    def should_be_to_login_in(self):
        self.should_be_login_form()
        self.should_be_forgot_pass_link()
        self.should_be_submit_button()
        self.should_be_login_form()
        self.should_be_password_input()

    # Наличие всех элеменов, необходимых для регистрации
    def should_be_for_registration(self):
        self.should_be_register_form()
        self.should_be_reg_pass_input()
        self.should_be_reg_email_input()
        self.should_be_submit_registration_button()

    # Наличие поля ввода email для регистрации
    def should_be_reg_email_input(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_INPUT), 'Reg email input is not presented'

    # Наличие формы регистрации
    def should_be_reg_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Reg form is not presented'

    # Наличие полей для ввода пароля и его подстверждения
    def should_be_reg_pass_input(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT), 'No pass1 inp'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_SUBMIT_INPUT), 'No pass2 inp'

    # Проверка соответствия url
    def should_be_login_url(self, language):
        current_url = self.browser.current_url
        language = language.lower()
        assert current_url == f'https://selenium1py.pythonanywhere.com/{language}/accounts/login/', f"Wrong login " \
                                                                                                    f"page url "

    # Проверка появления окон с валидацией при неверном вводе пароля
    def should_be_login_alerts(self):
        self.is_element_present(*LoginPageLocators.FIRST_ALERT), '"Try again" alert is not presented'
        self.is_element_present(*LoginPageLocators.SECOND_ALERT), '"Fields can be case sensitive" is not presented'
