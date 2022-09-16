from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import Locators
from Core import by_locator, wait


def about_system():
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, Locators.sc_emporium))).click()
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, Locators.about_system))).click()
    assert by_locator(Locators.link_about_system).text == Locators.text_about_system, "The text doesn't match"
    print("The text about the system is correct")

