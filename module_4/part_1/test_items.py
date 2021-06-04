import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_login_link(browser):
    # Arrange
    browser.get(link)

    # Act
    basket_button = browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    lang_of_page = browser.find_element_by_css_selector('[class="no-js"]').get_attribute("lang")

    # Assert
    # Не уверен, что такой вид assert является приемлимым, буд благодарен за совет как это можно улучшить:)
    if lang_of_page == 'ru':
        assert basket_button.text in 'Добавить в корзину', 'Неверное содержание текста кнопки'

    if lang_of_page == 'en-gb':
        assert basket_button.text in 'Add to basket', 'Неверное содержание текста кнопки'

    if lang_of_page == 'es':
        assert basket_button.text in 'Añadir al carrito', 'Неверное содержание текста кнопки'

    if lang_of_page == 'fr':
        assert basket_button.text in 'Ajouter au panier', 'Неверное содержание текста кнопки'
