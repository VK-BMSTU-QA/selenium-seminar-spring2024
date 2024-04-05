import pytest
import logging
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ui.locators.park_vk_company import LoginPageLocators, SettingsPageLocators, HeaderLocators
import time

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)
        if self.authorize:
            login, password = request.getfixturevalue("credentials")
            self.main_page = self.login_page.login(login, password)


@pytest.fixture(scope='session')
def credentials(config):
    return (config['login'], config['password']) 


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    locators = LoginPageLocators()

    def login(self, username, password):
        self.click(self.locators.LOGIN_BTN_LOCATOR)
        login_input = self.find(self.locators.LOGIN_INPUT_LOCATOR)
        login_input.send_keys(username)
        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR)
        password_input.send_keys(password)
        self.click(self.locators.LOGIN_SUBMIT_BTN_LOCATOR)

        return MainPage(self.driver)

class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    locators = SettingsPageLocators()
    def get_about(self):
        about_textarea = self.find(self.locators.ABOUT_TEXTAREA_LOCATOR)
        return about_textarea.text

    def get_success_msg(self):
        return self.find(self.locators.SUCCESS_MSG_LOCATOR).text

    def update_about(self, about):
        about_textarea = self.find(self.locators.ABOUT_TEXTAREA_LOCATOR)
        about_textarea.clear()
        about_textarea.send_keys(about)
        self.click(self.locators.SAVE_BTN_LOCATOR)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def is_active_section(self, locator):
        section = self.find(locator)
        return "active" in section.get_attribute('class')

    def move_to(self, locator):
        self.click(locator)

    def open_settings(self):
        self.click((By.ID, 'dropdown-user-trigger'))
        self.click((By.CLASS_NAME, 'item-settings'))
        return SettingsPage(self.driver)


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login, password = credentials
        self.main_page = self.login_page.login(login, password)
        assert "Лента" in self.driver.title
        assert self.driver.current_url == self.main_page.url

class TestLK(BaseCase):
    authorize = True

    @pytest.mark.parametrize(
        'src,dst',
        [
            pytest.param(
                (By.CLASS_NAME, 'technopark__menu__item_3'),
                (By.CLASS_NAME, 'technopark__menu__item_4')
            ),
            pytest.param(
                (By.CLASS_NAME, 'technopark__menu__item_41'),
                (By.CLASS_NAME, 'technopark__menu__item_42')
            )
        ]
    )
    def test_header(self, src, dst):
        self.main_page.move_to(src)
        assert self.main_page.is_active_section(src)
        time.sleep(3)
        self.main_page.move_to(dst)
        assert self.main_page.is_active_section(dst)

    def test_about_change(self):
        self.settings_page = self.main_page.open_settings()
        assert self.driver.current_url == self.settings_page.url
        assert "Настройки" in self.driver.title
        time.sleep(3)
        self.settings_page.update_about('test')
        assert self.settings_page.get_about() == 'test'
        assert "О себе" in self.settings_page.get_success_msg()
        time.sleep(5)
        self.settings_page.update_about('')
