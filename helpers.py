import random
import string
from string import ascii_lowercase, digits

from locators import BurgerLocators


class Helpers:
    @staticmethod
    def login(driver):
        driver.find_element(*BurgerLocators.LOGIN_NAME_INPUT).send_keys('sobaka777@mail.ru')

        # Найди поле "Пароль" и заполни его
        driver.find_element(*BurgerLocators.LOGIN_PWD_INPUT).send_keys('barabaka')

        # Найди кнопку "Войти" и кликни по ней
        driver.find_element(*BurgerLocators.LOGIN_ENTER_BUTTON).click()

    @staticmethod
    def generate_user_name():
        user_name = f'test_user{random.randint(12, 1000)}'
        return user_name

    @staticmethod
    def generate_email(user_name):
        email = f'{user_name}@ya.ru'
        return email

    @staticmethod
    def generate_pwd():
        pwd = ''.join(random.choices(digits + string.ascii_letters, k=6))
        return pwd