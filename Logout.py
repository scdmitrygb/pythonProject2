import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Locators
from Core import by_locator, url, browser, web_driver_wait
from selenium.webdriver.support import expected_conditions as EC


def logout():
    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.icon)))
    except:
        by_locator(Locators.icon).click()
        by_locator(Locators.logout).click()
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, Locators.icon)))
        if url().endswith("login"):
            print("Logout complete")
        else:
            print("Error logout")
