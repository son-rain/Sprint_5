import pytest
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from locators import *
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()

    yield chrome_driver
    chrome_driver.quit()



