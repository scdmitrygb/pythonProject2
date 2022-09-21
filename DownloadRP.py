import time
import Locators
from Core import by_locator, wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_download_rp(login_client):
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, Locators.sc_emporium))).click()
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, Locators.help_menu))).click()
    by_locator(Locators.download_rp).click()
    time.sleep(2)
