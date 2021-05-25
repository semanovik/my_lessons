from selenium import webdriver

login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_login_logout():
    # Data
    login = 'semasema@gmail.com'
    password = '328225328225'

    login_email_locator = '[id="id_login-username"]'
    login_password_locator = '[id="id_login-password"]'
    login_button_locator = '[name="login_submit"]'
    welcome_message = '[class="alertinner wicon"]'
    logout_button_locator = '[id="logout_link"]'
    back_to_login_page_button_locator = '[id="login_link"]'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)

        input_login = browser.find_element_by_css_selector(login_email_locator)
        input_login.clear()

        input_password = browser.find_element_by_css_selector(login_password_locator)
        input_login.clear()

        login_button = browser.find_element_by_css_selector(login_button_locator)

        # Act
        input_login.send_keys(login)
        input_password.send_keys(password)
        login_button.click()
        browser.find_element_by_css_selector(welcome_message)
        browser.find_element_by_css_selector(logout_button_locator).click()
        browser.find_element_by_css_selector(back_to_login_page_button_locator).click()

        # Assert
        assert login_page_link in browser.current_url, 'Wrong login page URL'

    finally:
        browser.quit()


test_login_logout()
