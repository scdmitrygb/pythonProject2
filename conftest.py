import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from Core import by_locator, browser, wait
import Locators


@pytest.fixture(scope="function")
def login_client():
    browser.get(Locators.link)
    by_locator(Locators.login).send_keys("2")
    by_locator(Locators.password).send_keys("must2", Keys.ENTER)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Locators.icon)))
    assert by_locator(Locators.icon).text == "К"
    yield
    browser.quit()
