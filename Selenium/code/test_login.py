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
            creds = request.getfixturevalue('credentials')
            self.main_page = self.login_page.login(**creds)


@pytest.fixture(scope='session')
def credentials():
    with open('./files/userdata') as file:
        return json.load(file)


@pytest.fixture(scope='session')
def cookies(credentials, config):
    pass


class BasePage(object):
    url = 'https://park.vk.company/'

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
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

        login = self.find(self.login_locators.LOGIN)
        login.clear()
        login.send_keys(user)

        passwd = self.find(self.login_locators.PASSWORD)
        passwd.clear()
        passwd.send_keys(password)

        self.click(self.login_locators.SUBMIT)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def go_to_menu_items(self, first_item_name, second_item_name):
        self.find((By.LINK_TEXT, first_item_name)).click()
        time.sleep(2)

        self.find((By.LINK_TEXT, second_item_name)).click()
        time.sleep(2)


class LKPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    lk_page_locators = locators.LKPageLocators()

    def update_info(self, info):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        time.sleep(2)

        about = self.find(self.lk_page_locators.ABOUT)
        old = about.text
        about.clear()
        about.send_keys(info)
        self.click(self.lk_page_locators.SUBMIT)

        return old

    def update_last_name(self, last_name):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        time.sleep(2)

        last_name_en = self.find(self.lk_page_locators.LAST_NAME_EN)
        old = last_name_en.get_attribute('value')
        last_name_en.clear()
        last_name_en.send_keys(last_name)
        self.click(self.lk_page_locators.SUBMIT)

        return old


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.main_page.click((By.ID, 'dropdown-user-trigger'))
        time.sleep(2)
        assert 'Программа' in self.driver.page_source
        assert 'Успеваемость' in self.driver.page_source
        assert 'Мои аккаунты' in self.driver.page_source


class TestMainPage(BaseCase):
    def test_main_page(self):
        self.main_page.go_to_menu_items('Блоги', 'Люди')
        assert 'Сообщество проекта' in self.driver.page_source
        assert 'Рейтинг' in self.driver.page_source

        self.main_page.go_to_menu_items('Программа', 'Выпуски')
        assert 'Наши выпускники' in self.driver.page_source


class TestLK(BaseCase):

    def test_updating_profile_info(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        info = 'selenium seminar ' + str(random.randint(1, 100))
        old = self.lk_page.update_info(info)
        time.sleep(3)
        assert info in self.driver.page_source
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source

        self.lk_page.update_info(old)
        time.sleep(3)
        assert old in self.driver.page_source
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source

    def test_updating_last_name(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        last_name = 'selenium' + str(random.randint(1, 100))
        old = self.lk_page.update_last_name(last_name)
        time.sleep(3)
        assert last_name in self.driver.page_source
        assert 'Вы успешно отредактировали поле: Фамилия [eng]' in self.driver.page_source

        self.lk_page.update_last_name(old)
        time.sleep(3)
        assert old in self.driver.page_source
        assert 'Вы успешно отредактировали поле: Фамилия [eng]' in self.driver.page_source
