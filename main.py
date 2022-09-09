import unittest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from Core import by_locator, browser, url
import Locators


def test_registration1():
    link = "https://192.168.253.40:7770/#/login"
    browser.get(link)
    by_locator(Locators.login).send_keys("2")
    by_locator(Locators.password).send_keys("must2", Keys.ENTER)
    # ждем загрузки страницы
    time.sleep(1)
    assert by_locator(Locators.icon).text == "К", "Клиент"
    by_locator(Locators.icon).click()
    by_locator(Locators.logout).click()
    time.sleep(1)
    if url().endswith("login"):
        print("Разлогинивание")
    else:
        print("нет")
    # находим элемент, содержащий текст
    # welcome_text_elt = by_locator("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    # assert (welcome_text, "Congratulations! You have successfully registered!",
    # "Удачное выполнение теста")
    time.sleep(5)
    browser.quit()
