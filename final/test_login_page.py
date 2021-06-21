import pytest

from pages.login_page import LoginPage

login_page_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


class TestLoginPage:

    @pytest.mark.skip
    def test_need_to_login(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()

        # Assert
        page.should_be_to_login_in()

    @pytest.mark.skip
    # Тут добавить проверки, что пользователь реально вошел
    def test_login_in_account(self, browser):
        # Arrange
        page = LoginPage(browser, login_page_link)

        # Act
        page.open()

        # Assert
        page.correct_fill_inputs()

    def test_reg_test_user(self, browser):

        page = LoginPage(browser, login_page_link)

        page.open()
        page.reg_new_user()

    def test_need_to_register(self,browser):
        page = LoginPage(browser,login_page_link)

        page.open()

        page.should_be_register_form()
        page.should_be_register_form()
        page.should_be_reg_email_input()
        page.should_be_reg_pass_input()