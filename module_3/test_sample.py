from selenium import webdriver

login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

# Data
enrty_to_login_page_button_locator = '[id="login_link"]'
login_email_locator = '[name="login-username"]'
login_password_locator = '[name="login-password"]'
login_button_locator = '[name="login_submit"]'
logout_button_locator = '[id="logout_link"]'

# Arrange
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(login_page_link)


login_email_input = browser.find_element_by_css_selector(login_email_locator)
login_email_input.clear()

login_password_input = browser.find_element_by_css_selector(login_password_locator)
login_password_input.clear()

login_button = browser.find_element_by_css_selector(login_button_locator)


# Act
login_email_input.send_keys('semasema@gmail.com')
login_password_input.send_keys('328225328225')
login_button.click()
browser.find_element_by_css_selector('[class="alertinner wicon"]')
browser.find_element_by_css_selector(logout_button_locator).click()
browser.find_element_by_css_selector(enrty_to_login_page_button_locator).click()



