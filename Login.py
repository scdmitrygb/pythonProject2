import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from Core import by_locator, browser, wait
import Locators


@pytest.mark.parametrize('login, password, icon', Locators.my_list)
def test_login(login, password, icon):
    browser.get(Locators.link)
    by_locator(Locators.login).send_keys(login)
    by_locator(Locators.password).send_keys(password, Keys.ENTER)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Locators.icon)))
    assert by_locator(Locators.icon).text == icon, "Не совпадает текст на иконке пользователя"
