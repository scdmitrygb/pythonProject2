import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from Core import by_locator, browser, wait
import Locators
from datetime import date


# @pytest.fixture(scope="function")
# def login_client():
#     browser.get(Locators.link)
#     by_locator(Locators.login).send_keys("2")
#     by_locator(Locators.password).send_keys("must2", Keys.ENTER)
#     wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, Locators.icon)))
#     assert by_locator(Locators.icon).text == "К"
#     yield
#     browser.quit()


@pytest.fixture(scope="function")
@pytest.mark.parametrize('login, password, icon', Locators.my_list)
def test_login(login, password, icon):
    browser.get(Locators.link)
    by_locator(Locators.login).send_keys(login)
    by_locator(Locators.password).send_keys(password, Keys.ENTER)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Locators.icon)))
    assert by_locator(Locators.icon).text == icon, "Не совпадает текст на иконке пользователя"
    browser.quit()

@pytest.fixture(autouse=True)
def check_open_menu(login_client):
    visibility_menu = by_locator(Locators.menu).get_attribute("data-menuvisible")
    if visibility_menu == "false":
        by_locator(Locators.menu_arrow).click()
    elif visibility_menu == "true" or "None":
        print("Menu is open")


@pytest.fixture(autouse=True)
def check_copyright(login_client):
    copyright_year = by_locator(Locators.copyright_year).text[-4:]
    current_year = date.today().year
    assert copyright_year == str(current_year), "Год в копирайте не верен"
    print("Copyright OK")
