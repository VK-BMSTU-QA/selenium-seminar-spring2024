import time
import json

import pytest
from _pytest.fixtures import FixtureRequest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from ui.pages.base_page import BasePage
from ui.locators import park_locators


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
    locators = park_locators.LoginPageLocators()

    def login(self, user, password):
        self.click(self.locators.LOGIN_BTN_LOCATOR)
        
        login_input = self.find(self.locators.LOGIN_INPUT_LOCATOR)
        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR)
        
        login_input.clear()
        password_input.clear()
        
        login_input.send_keys(user)
        password_input.send_keys(password)
        
        self.click(self.locators.LOGIN_SUBMIT_BTN_LOCATOR)
        
        return MainPage(self.driver)

class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'
    locators = park_locators.HeaderLocators()
    
    def is_active_section(self, section):
        section = self.find(self.locators.get_locator_by_section(section))
        return "active" in section.get_attribute('class')
    
    def move_to(self, section):
        self.click(self.locators.get_locator_by_section(section))
    
    def go_to_menu_items(self, first_item_name, second_item_name):
        self.find((By.LINK_TEXT, first_item_name)).click()
        time.sleep(2)

        self.find((By.LINK_TEXT, second_item_name)).click()
        time.sleep(2)
    
    def open_settings(self):
        self.click(self.locators.DROPDOWN_BTN_LOCATOR)
        self.click(self.locators.SETTINGS_BTN_LOCATOR)
        return SettingsPage(self.driver)

class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    locators = park_locators.SettingsPageLocators()

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

class LKPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    lk_page_locators = park_locators.LKPageLocators()

    def update_info(self, info):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        time.sleep(2)

        about = self.find(self.lk_page_locators.ABOUT)
        about.clear()
        about.send_keys(info)
        self.click(self.lk_page_locators.SUBMIT)

    def update_last_name(self, last_name):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        time.sleep(2)

        last_name_en = self.find(self.lk_page_locators.LAST_NAME_EN)
        last_name_en.clear()
        last_name_en.send_keys(last_name)
        self.click(self.lk_page_locators.SUBMIT)

class TestLogin(BaseCase):
    authorize = True

    def test_login_success(self, credentials):
        self.main_page.click((By.ID, 'dropdown-user-trigger'))
        time.sleep(2)
        assert 'Программа' in self.driver.page_source
        assert 'Успеваемость' in self.driver.page_source
        assert 'Мои аккаунты' in self.driver.page_source

class TestLK(BaseCase):
    authorize = True

    @pytest.mark.parametrize(
        'src,dst',
        [
            pytest.param(
                park_locators.HeaderSections.BLOGS,
                park_locators.HeaderSections.PEOPLE
            ),
            pytest.param(
                park_locators.HeaderSections.PROGRAMS,
                park_locators.HeaderSections.GRADUATES
            )
        ]
    )
    def test_header(self, src, dst):
        self.main_page.move_to(src)
        assert self.main_page.is_active_section(src)
        
        time.sleep(5)
        
        self.main_page.move_to(dst)
        assert self.main_page.is_active_section(dst)

    def test_about_change(self):
        self.settings_page = self.main_page.open_settings()
        assert self.driver.current_url == self.settings_page.url
        assert "Настройки" in self.driver.title
        
        time.sleep(5)
        
        self.settings_page.update_about('test')
        assert self.settings_page.get_about() == 'test'
        assert "О себе" in self.settings_page.get_success_msg()
        
        time.sleep(5)
        self.settings_page.update_about('')
    
    def update_info(self, info):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        time.sleep(2)

        about = self.find(self.lk_page_locators.ABOUT)
        about.clear()
        about.send_keys(info)
        self.click(self.lk_page_locators.SUBMIT)
        assert "О себе" in self.settings_page.get_success_msg()

    def update_last_name(self, last_name):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        time.sleep(2)

        last_name_en = self.find(self.lk_page_locators.LAST_NAME_EN)
        last_name_en.clear()
        last_name_en.send_keys(last_name)
        self.click(self.lk_page_locators.SUBMIT)
        assert "Фамилия [eng]" in self.settings_page.get_success_msg()
