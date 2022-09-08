from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()


def by_locator(locator):
    if locator.startswith("/"):
        return browser.find_element(By.XPATH, locator)
    else:
        return browser.find_element(By.CSS_SELECTOR, locator)



