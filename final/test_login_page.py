from pages.login_page import LoginPage

login_page_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


class TestLoginPage:

    def test_need_to_login(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()

        # Assert
        page.should_be_to_login_in()

    #Тут добавить проверки, что пользователь реально вошел
    def login_in_account(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()

        # Assert
        page.correct_fill_inputs()

    #Тут добавить, что пользователь зареган
    def reg_test_user(self, browser):

        page = LoginPage(browser, login_page_link)

        page.open()
        page.reg_new_user()
