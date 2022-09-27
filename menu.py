import Locators
from Core import by_locators, wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_get_menu():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "menu>menu-item>ul>li")))
    menu = by_locators(Locators.menu_item)
    for i in menu:
        menu_item = i.text
        print(menu_item)
