import time

import pytest
import yaml
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from ui.locators import basic_locators


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
    with open('../creds.yaml', 'r') as file:
        data = yaml.safe_load(file)
    return {'username': data['username'], 'password': data['password']}


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(
            basic_locators.BasePageLocators.LOGIN_BUTTON_LOCATOR, timeout=2
        )
        login_input = (By.NAME, 'login')
        password_input = (By.NAME, 'password')
        time.sleep(1)
        self.find(login_input).send_keys(user)
        self.find(password_input).send_keys(password)
        self.click(
            basic_locators.BasePageLocators.SUBMIT_LOGIN_BUTTON_LOCATOR, timeout=2
        )
        time.sleep(5)

        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'
    settings_url = 'https://park.vk.company/cabinet/settings/'

    def settings(self):
        self.driver.get(self.settings_url)
        return SettingsPage(self.driver)

    def go_to_section(self, title):
        section = self.driver.find_element(By.LINK_TEXT, title)
        time.sleep(1)
        section.click()
        time.sleep(5)


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    def change_profile(self, locator, new_info):
        field = self.find(locator)
        field.clear()
        field.send_keys(new_info)
        time.sleep(1)
        self.click(
            basic_locators.BasePageLocators.SUBMIT_PROFILE_EDIT_LOCATOR, timeout=2
        )
        time.sleep(5)


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        page = self.login_page.login(credentials['username'], credentials['password'])
        assert page.url == self.driver.current_url


class TestLK(BaseCase):

    def test_change_about_info(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])
        settings_page = main_page.settings()
        new_info_text = 'о себе'
        textarea_locator = (By.ID, 'profile_about')
        settings_page.change_profile(textarea_locator, new_info_text)
        assert settings_page.find(textarea_locator).get_attribute("value") == new_info_text

    def test_change_section_blogs_to_people(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])
        main_page.go_to_section('Блоги')
        assert 'Все блоги' in self.driver.page_source
        main_page.go_to_section('Люди')
        assert 'Сообщество проекта' in self.driver.page_source

    def test_change_section_programm_to_alumni(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])
        main_page.go_to_section('Программа')
        assert 'Мои учебные программы' in self.driver.page_source
        main_page.go_to_section('Выпуски')
        assert 'Наши выпускники' in self.driver.page_source

