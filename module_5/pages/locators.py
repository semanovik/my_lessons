from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '[id="register_form"]')


class ProductPageLocators():

    # Кнопка добавления книги в корзину
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')

    # Название книги
    BOOK_TITLE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')

    # Цена книги
    BOOK_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')

    # Сумма корзины
    CART_AMOUNT = (By.CSS_SELECTOR, '[class="basket-mini pull-right hidden-xs"]')

    # Название книги в сообщении о добавлении в корзину
    ADDED_BOOK_TITLE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
