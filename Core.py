from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locators

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 10)


def by_locator(locator):
    if locator.startswith("/"):
        return browser.find_element(By.XPATH, locator)
    else:
        return browser.find_element(By.CSS_SELECTOR, locator)


def url():
    print("URL is " + browser.current_url)
    return browser.current_url


def close_notification():
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, Locators.notification)))
    by_locator(Locators.close).click()
