from locators import *
from data import Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestAccountPageStellarBurgers:
    def test_click_on_logo_from_account_page(self, driver):
        driver.get(Data.STELLAR_BURGER_ACCOUNT_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.LOGIN_LABEL))
        driver.find_element(*BurgerLocators.LOGIN_NAME_INPUT).send_keys('zeleboba387@yandex.ru')
        driver.find_element(*BurgerLocators.LOGIN_PWD_INPUT).send_keys('Zelebobba')
        driver.find_element(*BurgerLocators.LOGIN_ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.HOME_LABEL))
        driver.find_element(*BurgerLocators.HOME_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.HOME_LOGO))
        driver.find_element(*BurgerLocators.HOME_LOGO).click()
        assert driver.current_url == Data.STELLAR_BURGER_URL

    def test_click_on_constractor_link_from_account_page(self,driver):
        driver.get(Data.STELLAR_BURGER_ACCOUNT_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.LOGIN_LABEL))
        driver.find_element(*BurgerLocators.LOGIN_NAME_INPUT).send_keys('zeleboba387@yandex.ru')
        driver.find_element(*BurgerLocators.LOGIN_PWD_INPUT).send_keys('Zelebobba')
        driver.find_element(*BurgerLocators.LOGIN_ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.HOME_LABEL))
        driver.find_element(*BurgerLocators.HOME_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.HOME_LOGO))
        driver.find_element(*BurgerLocators.CONSTRUCTOR_BUTTON).click()

        assert driver.current_url == Data.STELLAR_BURGER_URL

    def test_quit_account(self, driver):
        driver.get(Data.STELLAR_BURGER_ACCOUNT_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.LOGIN_LABEL))
        driver.find_element(*BurgerLocators.LOGIN_NAME_INPUT).send_keys('zeleboba387@yandex.ru')
        driver.find_element(*BurgerLocators.LOGIN_PWD_INPUT).send_keys('Zelebobba')
        driver.find_element(*BurgerLocators.LOGIN_ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            BurgerLocators.HOME_LABEL))
        driver.find_element(*BurgerLocators.HOME_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            BurgerLocators.ACCOUNT_PROFILE_LINK))
        driver.find_element(*BurgerLocators.ACCOUNT_QUIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            BurgerLocators.LOGIN_LABEL))
        assert driver.current_url == Data.STELLAR_BURGER_LOGIN_URL
        driver.find_element(*BurgerLocators.HOME_LOGO).click()
        assert driver.find_element(*BurgerLocators.HOME_LOGIN_BUTTON).is_displayed()



