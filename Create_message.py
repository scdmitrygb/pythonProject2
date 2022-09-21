from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
import Locators
from typing import List
from Core import by_locator, wait, close_notification, browser


def test_create_message(login_client):
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, Locators.message))).click()
    by_locator(Locators.btCreateMessage).click()
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, Locators.listDrafr)))
    my_list: List[WebElement] = browser.find_elements(By.CSS_SELECTOR, Locators.usersDraft)
    messages = ["Администратору", "Дилеру"]
    for i in my_list:
        if i.text in messages:
            i.click()
            name = i.text
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, Locators.inputField))).send_keys(f"SMS for {name}")
            by_locator(Locators.btSendMessage).click()
            close_notification()
            if name != (messages[-1]):
                by_locator(Locators.btCreateMessage).click()
            close_notification()
