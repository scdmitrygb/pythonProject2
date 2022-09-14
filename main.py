import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Core import by_locator, browser, web_driver_wait
from CreateMessage import create_message
import Locators
from Logout import logout


def test_registration1():
    browser.get(Locators.link)
    by_locator(Locators.login).send_keys("2")
    by_locator(Locators.password).send_keys("must2", Keys.ENTER)
    web_driver_wait()(
        EC.presence_of_element_located((By.CSS_SELECTOR, Locators.icon)))
    assert by_locator(Locators.icon).text == "К"
    create_message()
    logout()
    browser.quit()

