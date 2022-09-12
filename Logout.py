import Locators
from Core import by_locator, browser, url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def logout():
    by_locator(Locators.icon).click()
    by_locator(Locators.logout).click()
    WebDriverWait(browser, 5).until(
        EC.staleness_of(by_locator(Locators.icon)))
    if url().endswith("login"):
        print("Logout complete")
    else:
        print("Error logout")
