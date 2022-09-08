import unittest
import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from Core import by_locator, browser
from Locators import last_name, first_name, mail, button


def test_registration1():
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)
    by_locator(first_name).send_keys("Ivan")
    by_locator(last_name).send_keys("Popov")
    by_locator(mail).send_keys("popov@mail.ru")
    # Отправляем заполненную форму
    by_locator(button).click()
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = by_locator("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert (welcome_text, "Congratulations! You have successfully registered!",
            "Удачное выполнение теста")
    browser.quit()
