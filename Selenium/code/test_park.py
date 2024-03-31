import pytest
import json
import time
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.locators.park_locators import LoginPageLocators, MainPageLocators, SettingsLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def credentials():
    with open('./Selenium/code/files/userdata') as file:
        return json.load(file)


class BaseCase:
    authorize = True
    open_settings = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            creds = credentials()
            self.login_page.login(**creds)
            self.main_page = MainPage(self.driver)
            if self.open_settings:
                self.settings_page = self.main_page.open_settings()



@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.find(LoginPageLocators.LOGIN_INPUT).send_keys(user)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(Keys.ENTER)


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    def change_about(self, text):
        about_field = self.find(SettingsLocators.ABOUT_FIELD)
        about_field.clear()
        about_field.send_keys(text)
        self.click(SettingsLocators.SUBMIT_BUTTON)

    def get_about_value(self):
        about_field = self.find(SettingsLocators.ABOUT_FIELD)
        return about_field.get_attribute('value')

    def get_save_message(self):
        return self.find(SettingsLocators.SAVE_MESSAGE).text



class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def is_navigation_active(self, url):
        button = self.find(MainPageLocators.navButtonByUrl(url))
        parent = button.find_element(By.XPATH, '..')
        return "active" in parent.get_attribute('class')

    def go_to_section(self, url):
        self.click(MainPageLocators.navButtonByUrl(url))

    def open_settings(self):
        self.click(MainPageLocators.DROPDOWN_MENU)
        self.click(MainPageLocators.COG_BTN)
        return SettingsPage(self.driver)


class TestLogin(BaseCase):
    authorize = False

    def test_login_wrong(self):
        self.login_page.login('123', '123')
        time.sleep(5)
        assert 'Учётные данные неверны' in self.driver.page_source

    def test_login_correct(self):
        self.login_page.login(**(credentials()))
        time.sleep(5)
        assert 'Блоги' in self.driver.page_source



class TestNavigation(BaseCase):
    authorize = True

    @pytest.mark.parametrize(
        'url,testStrings',
        [
            pytest.param(
                '/blog/',
                [ 'Все блоги', 'Читатели']
            ),
            pytest.param(
                '/people/',
                ['Сообщество проекта']
            ),
            pytest.param(
                '/alumni/',
                ['Наши выпускники']
            ),
            pytest.param(
                '/curriculum/program/',
                ['Мои учебные программы']
            ),
            pytest.param(
                '/schedule/',
                ['Ближайшие две недели', 'Дисциплина', 'Тип события']
            ),
            pytest.param(
                '/career/',
                ['Мои резюме']
            )
        ]
    )
    def test_navigation(self, url, testStrings):
        self.main_page.go_to_section(url)
        time.sleep(2)
        assert self.main_page.is_navigation_active(url)
        for s in testStrings:
            assert s in self.driver.page_source


class TestSettings(BaseCase):
    open_settings = True

    def test_settings(self):
        assert "Настройки" in self.driver.title
        old_value = self.settings_page.get_about_value()
        self.settings_page.change_about("очень умный и красивый")
        time.sleep(5)
        assert 'О себе' in self.settings_page.get_save_message()
        assert "очень умный и красивый" in self.driver.page_source
        self.settings_page.change_about(old_value)


