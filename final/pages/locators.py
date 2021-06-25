from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, '[name="login-username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="login-password"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '[id="register_form"]')
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_PASSWORD_SUBMIT_INPUT = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//*[@id="login_form"]/p/a')

class MainPageLocators:
    LOGOUT_LINK = (By.CSS_SELECTOR, '[id="logout_link"]')
    ACCOUNT_LINK = (By.XPATH, '//*[@id="top_page"]/div[2]/div/ul/li[1]/a')
    WELCOME_MESSAGE = (By.CSS_SELECTOR, '[class="alertinner wicon"]')
    ALL_GOODS_CATALOGUE = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')

class CatalogPageLocators:

    ALL_GOODS_TITLE = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/div[1]/h1')
    SIDE_CATEGORIES = (By.CSS_SELECTOR, '[class="side_categories"]')
    SOME_FIRST_PRODUCT = (By.CSS_SELECTOR, '[class="product_pod"]')







