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

    # Наличие необходимых элементов для логирования и регистрации
    def test_need_to_login(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()

        # Assert
        page.should_be_to_login_in()
        page.should_be_for_registration()

    # Вход в существующий аккаунт, проверка приветствия существующего пользователя
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

    # Регистрация нового аккаунта, проверка приветсвия нового пользователя
    def test_reg_test_user(self, browser, language):
        page = LoginPage(browser, login_page_link)

        page.open()
        page.reg_new_user()
        main_page = MainPage(browser, browser.current_url)

        welcome_message = main_page.get_text_from_welcome_message()
        main_page.should_be_correct_message(expected_welcome_text_reg[language], welcome_message)

    # Негативная проверка, что нет поздравления с регистрацией для старого пользователя
    def test_should_not_be_welcome_new_user_message_after_login_in(self, browser, language):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()
        page.correct_fill_inputs()
        main_page = MainPage(browser, browser.current_url)
        welcome_message = main_page.get_text_from_welcome_message()

        # Assert
        main_page.should_not_be_incorrect_message(expected_welcome_text_reg[language], welcome_message)

    # Негативная проверка, что нет приветствия старого пользователя для нового
    def test_should_not_be_welcome_back_message_after_registration(self, browser, language):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()
        page.correct_fill_inputs()
        main_page = MainPage(browser, browser.current_url)
        welcome_message = main_page.get_text_from_welcome_message()

        # Assert
        main_page.should_not_be_incorrect_message(expected_welcome_text_login, welcome_message)

    # Проверка появления алертов при указании неверных данных
    def test_login_in_with_wrong_password(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()
        page.incorrect_fill_inputs()

        # Assert
        page.should_be_login_alerts()