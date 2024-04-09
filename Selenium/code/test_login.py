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
        value = about.get_attribute("value")

        about.clear()
        about.send_keys(info)
        self.click(self.lk_page_locators.SUBMIT)

        about = self.find(self.lk_page_locators.ABOUT)
        
        about.clear()
        about.send_keys(value)
        self.click(self.lk_page_locators.SUBMIT)

        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source

    def update_first_name(self, first_name):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        first_name_field = self.find(self.lk_page_locators.FIRST_NAME)
        value = first_name_field.get_attribute("value")

        first_name_field.clear()
        first_name_field.send_keys(first_name)
        self.click(self.lk_page_locators.SUBMIT)

        first_name_field = self.find(self.lk_page_locators.FIRST_NAME)

        first_name_field.clear()
        first_name_field.send_keys(value)
        self.click(self.lk_page_locators.SUBMIT)

        return 'Вы успешно отредактировали свое имя' in self.driver.page_source

    def update_last_name(self, last_name):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        last_name_field = self.find(self.lk_page_locators.LAST_NAME)
        value = last_name_field.get_attribute("value")

        last_name_field.clear()
        last_name_field.send_keys(last_name)
        self.click(self.lk_page_locators.SUBMIT)

        last_name_field = self.find(self.lk_page_locators.LAST_NAME)

        last_name_field.clear()
        last_name_field.send_keys(value)
        self.click(self.lk_page_locators.SUBMIT)

        return 'Вы успешно отредактировали свою фамилию' in self.driver.page_source


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
    def test_updating_first_name(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        first_name = 'Гироскоп'
        self.lk_page.update_first_name(first_name)

    def test_updating_last_name(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        last_name = 'Гироскопыч'
        self.lk_page.update_last_name(last_name)
        
    def test_updating_info(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        info = 'люблю гироскопы'
        self.lk_page.update_info(info)