import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Core import by_locator, browser
import Locators
import Core
from Logout import logout


def test_registration1():
    browser.get(Locators.link)
    by_locator(Locators.login).send_keys("2")
    by_locator(Locators.password).send_keys("must2", Keys.ENTER)
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Locators.icon)))
    assert by_locator(Locators.icon).text == "К", "Клиент"
    WebDriverWait(browser, 5).until(EC.visibility_of(by_locator(Locators.menu)))
    by_locator(Locators.message).click()
    by_locator(Locators.btSendMessage)