import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import Locators
from Core import by_locator, web_driver_wait, browser


def create_message():
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.message)))
    by_locator(Locators.message).click()
    by_locator(Locators.btCreateMessage).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.listDrafr)))
    by_locator(Locators.admin).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.inputField)))
    by_locator(Locators.inputField).send_keys("SMS for Administrator")
    by_locator(Locators.btSendMessage).click()

