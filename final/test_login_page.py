import time
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage

login_page_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'

# Ожидаемый текст приветствия пользователя, который зашел вновь
expected_welcome_text_login = {
    'ru': 'Рады видеть вас снова',
    'en-GB': 'Welcome back',
    'es': 'Bienvenido de nuevo',
    'fr': 'Bienvenue'
}

# Ожидаемый текст приветствия нового пользователя
expected_welcome_text_reg = {
    'ru': 'Спасибо за регистрацию!',
    'en-GB': 'Thanks for registering!',
    'es': 'Gracias por registrarse!',
    'fr': 'Merci de vous être enregistré !'
}


class TestLoginPage:

    # Наличие необходимых элементов для логирования
    def test_need_to_login(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()

        # Assert
        page.should_be_to_login_in()

    #   Наличие необходимых элементов для регистрации
    def test_need_to_register(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()

        # Assert
        page.should_be_register_form()
        page.should_be_register_form()
        page.should_be_reg_email_input()
        page.should_be_reg_pass_input()

    # Вход в существующий аккаунт
    def test_login_in_account(self, browser, language):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()
        page.correct_fill_inputs()
        main_page = MainPage(browser, browser.current_url)

        # Assert
        main_page.should_be_welcome_message()
        welcome_message = main_page.get_text_from_welcome_message()
        main_page.should_be_correct_message(expected_welcome_text_login[language], welcome_message)

    # Регистрация нового аккаунта
    def test_reg_test_user(self, browser, language):
        page = LoginPage(browser, login_page_link)

        page.open()
        page.reg_new_user()
        main_page = MainPage(browser, browser.current_url)

        welcome_message = main_page.get_text_from_welcome_message()
        main_page.should_be_correct_message(expected_welcome_text_reg[language], welcome_message)
