from selenium import webdriver
from sys import argv
import time


script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name_field = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
    name_field.send_keys("Sema")
    last_name_field = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    last_name_field.send_keys("Novik")
    email_field = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    email_field.send_keys("Sema@sema.com")



    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта

    # закрываем браузер после всех манипуляций
    browser.quit()