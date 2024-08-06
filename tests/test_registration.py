import random

from locators import *
from data import Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationStellarBurgers:

    def test_registration_by_order_button(self, driver):
        driver.get(Data.STELLAR_BURGER_REGISTRATION_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            BurgerLocators.REGISTRATION_LABEL))
        user_name = f'test_user{random.randint(12, 1000)}'
        driver.find_element(*BurgerLocators.NAME_INPUT).send_keys(user_name)
        driver.find_element(*BurgerLocators.EMAIL_INPUT).send_keys(f'{user_name}@ya.ru')
        driver.find_element(*BurgerLocators.PWD_INPUT).send_keys('test12345')
        driver.find_element(*BurgerLocators.REGISTRATION_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            BurgerLocators.LOGIN_LABEL))
        assert driver.current_url == Data.STELLAR_BURGER_LOGIN_URL

    def test_incorrect_pwd_on_registration(self, driver):
        driver.get(Data.STELLAR_BURGER_REGISTRATION_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            BurgerLocators.REGISTRATION_LABEL))
        user_name = f'test_user{random.randint(12, 1000)}'
        driver.find_element(*BurgerLocators.NAME_INPUT).send_keys(user_name)
        driver.find_element(*BurgerLocators.EMAIL_INPUT).send_keys(f'{user_name}@ya.ru')
        driver.find_element(*BurgerLocators.PWD_INPUT).send_keys('test1')
        driver.find_element(*BurgerLocators.REGISTRATION_SUBMIT_BUTTON).click()
        error_label = driver.find_element(*BurgerLocators.REGISTRATION_PWD_ERR_LABEL)
        assert error_label.text == "Некорректный пароль"





