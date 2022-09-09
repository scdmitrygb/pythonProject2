from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(chrome_options=options)


def by_locator(locator):
    if locator.startswith("/"):
        return browser.find_element(By.XPATH, locator)
    else:
        return browser.find_element(By.CSS_SELECTOR, locator)


def url():
    print("URL is " + browser.current_url)
    return browser.current_url
