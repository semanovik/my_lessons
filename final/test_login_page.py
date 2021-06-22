import time
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage

login_page_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
expected_welcome_text = {
    'ru': 'Рады видеть вас снова',
    'en': 'Welcome back',
    'es': 'Bienvenido de nuevo',
    'fr': 'Bienvenue'
}


class TestLoginPage:

    # Наличие важных элементов на странице логирования, блок входа
    def test_need_to_login(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()

        # Assert
        page.should_be_to_login_in()

    # Вход в существующий аккаунт
    def test_login_in_account(self, browser, language):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()
        page.correct_fill_inputs()
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_welcome_message()
        welcome_message = main_page.get_text_from_welcome_message()

        # Assert
        assert welcome_message in expected_welcome_text[language], 'Wrong welcome text'

    #   Наличие важных элементов на странице логирования, блок регистрации
    def test_need_to_register(self, browser):
        page = LoginPage(browser, login_page_link)

        page.open()

        page.should_be_register_form()
        page.should_be_register_form()
        page.should_be_reg_email_input()
        page.should_be_reg_pass_input()

    # Регистрация нового аккаунта
    def test_reg_test_user(self, browser):
        page = LoginPage(browser, login_page_link)

        page.open()
        page.reg_new_user()
