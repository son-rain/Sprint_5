import pytest
from selenium.webdriver.support.wait import WebDriverWait

from locators import *
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()

    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    # Найди поле "Email" и заполни его
    driver.find_element(*BurgerLocators.LOGIN_NAME_INPUT).send_keys('sobaka777@mail.ru')

    # Найди поле "Пароль" и заполни его
    driver.find_element(*BurgerLocators.LOGIN_PWD_INPUT).send_keys('barabaka')

    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(*BurgerLocators.LOGIN_ENTER_BUTTON).click()
