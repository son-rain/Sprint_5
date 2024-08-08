from helpers import Helpers as helpers
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data


class TestLoginStellarBurgers:

    def test_login_by_order_button(self, driver):
        driver.get(Data.STELLAR_BURGER_URL)
        login_button = driver.find_element(*BurgerLocators.HOME_LOGIN_BUTTON)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BurgerLocators.HOME_LABEL))
        login_button.click()
        helpers.login(driver)
        assert driver.current_url == Data.STELLAR_BURGER_LOGIN_URL
        order_button = driver.find_element(*BurgerLocators.HOME_ORDER_BUTTON)
        assert order_button.text == 'Оформить заказ'

    def test_login_by_account_button(self, driver):
        driver.get(Data.STELLAR_BURGER_URL)
        driver.find_element(*BurgerLocators.HOME_ACCOUNT_BUTTON).click()

        assert driver.current_url == Data.STELLAR_BURGER_LOGIN_URL

        helpers.login(driver)

        driver.find_element(*BurgerLocators.HOME_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(
            BurgerLocators.NAME_INPUT))

        assert driver.current_url == Data.STELLAR_BURGER_ACCOUNT_PROFILE_URL

    def test_login_on_forgot_password_page(self, driver):
        driver.get(Data.STELLAR_BURGER_FORGOTTEN_PWD_URL)
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(
            BurgerLocators.FORGOTTEN_LABEL))
        driver.find_element(*BurgerLocators.FORGOTTEN_PWD_LINK).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(
            BurgerLocators.LOGIN_LABEL))

        helpers.login(driver)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BurgerLocators.HOME_LABEL))

        assert driver.current_url == Data.STELLAR_BURGER_URL

    def test_login_on_registration_page(self, driver):
        driver.get(Data.STELLAR_BURGER_REGISTRATION_URL)
        driver.find_element(*BurgerLocators.REGISTRATION_LOGIN_LINK).click()

        helpers.login(driver)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BurgerLocators.HOME_LABEL))

        assert driver.current_url == Data.STELLAR_BURGER_URL


