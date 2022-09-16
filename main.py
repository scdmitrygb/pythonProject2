from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from Core import by_locator, browser, wait
from CreateMessage import create_message
import Locators
from Logout import logout
from Emporium import about_system
from DownloadRP import test_download_rp


def test_registration1():
    browser.get(Locators.link)
    by_locator(Locators.login).send_keys("2")
    by_locator(Locators.password).send_keys("must2", Keys.ENTER)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Locators.icon)))
    assert by_locator(Locators.icon).text == "К"
    # download_rp()
    test_download_rp()
    create_message()
    logout()
    browser.quit()
