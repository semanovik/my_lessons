import pytest
from selenium import webdriver

expected_button_lang = {
    'ru': 'Добавить в корзину',
    'en': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier'
}

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_login_link(browser, language):
    # Arrange
    browser.get(link)

    # Act
    basket_button = browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    lang_of_page = browser.find_element_by_css_selector('[class="no-js"]').get_attribute("lang")

    # Assert
    assert basket_button.text in expected_button_lang[language], "Wrong button language!"
    assert language in lang_of_page, 'Wrong page language!'
