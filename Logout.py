from selenium.webdriver.common.by import By
import Locators
from Core import by_locator, url, wait
from selenium.webdriver.support import expected_conditions as EC


def test_logout():
    by_locator(Locators.icon).click()
    by_locator(Locators.logout).click()
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.login)))
    if url().endswith("login"):
        print("Logout complete")
    else:
        print("Error logout")
