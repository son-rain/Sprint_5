from locators import *
from data import Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTabsStellarBurgers:
    def test_tab_toppings(self, driver):
        driver.get(Data.STELLAR_BURGER_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.HOME_LABEL))
        toppings_tab = driver.find_element(*BurgerLocators.HOME_TOPPINGS_TAB)
        toppings_tab.click()
        assert "current" in toppings_tab.get_attribute("class")

    def test_tab_buns(self, driver):
        driver.get(Data.STELLAR_BURGER_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.HOME_LABEL))
        driver.find_element(*BurgerLocators.HOME_TOPPINGS_TAB).click()
        buns_tab = driver.find_element(*BurgerLocators.HOME_BUNS_TAB)
        buns_tab.click()
        assert "current" in buns_tab.get_attribute("class")

    def test_tab_sauces(self, driver):
        driver.get(Data.STELLAR_BURGER_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.HOME_LABEL))
        driver.find_element(*BurgerLocators.HOME_TOPPINGS_TAB).click()
        sauces_tab = driver.find_element(*BurgerLocators.HOME_SAUCES_TAB)
        sauces_tab.click()
        assert "current" in sauces_tab.get_attribute("class")
