import json
import time
import random

import pytest
from _pytest.fixtures import FixtureRequest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from ui.locators import locators


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.lk_page = LKPage(driver)

        if self.authorize:
            print('Do something for login')
            creds = request.getfixturevalue('credentials')
            self.main_page = self.login_page.login(**creds)


@pytest.fixture(scope='session')
def credentials():
    with open('./files/userdata') as file:
        return json.load(file)


class BasePage(object):
    url = 'https://park.vk.company/'

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    login_locators = locators.LoginPageLocators()

    def login(self, user, password):
        self.click(self.login_locators.LOGIN_BUTTON)
        self.find(self.login_locators.LOGIN).send_keys(user)
        self.find(self.login_locators.PASSWORD).send_keys(password)
        self.click(self.login_locators.SUBMIT)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def go_to_menu_items(self, first_item_name, second_item_name, third_item_name, fourth_item_name):
        self.find((By.LINK_TEXT, first_item_name)).click()
        self.find((By.LINK_TEXT, second_item_name)).click()
        self.find((By.LINK_TEXT, third_item_name)).click()
        self.find((By.LINK_TEXT, fourth_item_name)).click()


class LKPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    lk_page_locators = locators.LKPageLocators()

    def update_info(self, info):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        about = self.find(self.lk_page_locators.ABOUT)
        about.clear()
        about.send_keys(info)
        self.click(self.lk_page_locators.SUBMIT)


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.main_page.click((By.ID, 'dropdown-user-trigger'))
        assert 'Успеваемость' in self.driver.page_source


class TestMainPage(BaseCase):
    def test_main_page(self):
        self.main_page.go_to_menu_items('Блоги', 'Люди', 'Программа', 'Выпуски')
        assert 1 == 1


class TestLK(BaseCase):
    def test_lk1(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        info = 'лю блю гироскопы, гироскопы это класс'
        self.lk_page.update_info(info)
        assert info in self.driver.page_source
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source
