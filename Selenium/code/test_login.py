import os
import random
import time

from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators import basic_locators

from ui.pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')
            self.main_page = self.login_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
            self.lk_page = LKPage(driver)


@pytest.fixture(scope='session')
def credentials():
    return os.getenv("USERNAME"), os.getenv("PASSWORD")


@pytest.fixture(scope='session')
def cookies(credentials, config):
    pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        login_button = self.driver.find_element(*basic_locators.LocatorsForParkPages.LOGIN_BUTTON)
        login_button.click()

        user_field = self.driver.find_element(*basic_locators.LocatorsForParkPages.USER_FIELD)
        password_field = self.driver.find_element(*basic_locators.LocatorsForParkPages.PASSWORD_FIELD)

        user_field.clear()
        user_field.send_keys(user)
        password_field.clear()
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://park.vk.company/feed/'))

        return MainPage(self.driver)


class BasePage(object):
    url = 'https://park.vk.company/'

    @allure.step('Click')
    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def __init__(self, driver):
        self.driver = driver

    def click_menu_item(self, item_name):
        menu_item = self.driver.find_element(By.LINK_TEXT, item_name)
        time.sleep(2)
        menu_item.click()


class TestTransition(BaseCase):
    def test_page_navigation_from_blogs_to_people(self):
        self.main_page.click_menu_item('Блоги')
        self.main_page.click_menu_item('Люди')

    def test_page_navigation_from_program_to_releases(self):
        self.main_page.click_menu_item('Программа')
        self.main_page.click_menu_item('Выпуски')


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        time.sleep(2)
        assert self.main_page.url == self.main_page.driver.current_url


class LKPage(MainPage):
    url = 'https://park.vk.company/feed/'

    def click_username(self):
        username_element = self.driver.find_element_by_class_name('username')
        username_element.click()

    def click_settings_link(self):
        settings_link = self.driver.find_element(*basic_locators.LocatorsForParkPages.SETTINGS_LINK)
        settings_link.click()

    def enter_about_information(self, about_info):
        input_field = self.driver.find_element(*basic_locators.LocatorsForParkPages.ABOUT_INPUT)
        input_field.clear()
        input_field.send_keys(about_info)

    def enter_eng_name_information(self, about_info):
        input_field = self.driver.find_element(*basic_locators.LocatorsForParkPages.ENG_NAME_INPUT)
        input_field.clear()
        input_field.send_keys(about_info)

    def enter_eng_surname_information(self, about_info):
        input_field = self.driver.find_element(*basic_locators.LocatorsForParkPages.ENG_SURNAME_INPUT)
        input_field.clear()
        input_field.send_keys(about_info)

    def click_submit_button(self):
        submit_button = self.driver.find_element(*basic_locators.LocatorsForParkPages.SUBMIT_BUTTON)
        submit_button.click()


class TestLK(BaseCase):
    def test_lk1(self):
        time.sleep(2)

        self.lk_page.click_username()
        time.sleep(2)

        self.lk_page.click_settings_link()
        time.sleep(2)

        information = '<' + str(random.randint(1, 1000))
        self.lk_page.enter_about_information(information)
        time.sleep(2)

        self.lk_page.click_submit_button()
        time.sleep(2)

        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source

    def test_lk2(self):
        time.sleep(2)

        self.lk_page.click_username()
        time.sleep(2)

        self.lk_page.click_settings_link()
        time.sleep(2)

        information = '<' + str(random.randint(1, 1000))
        self.lk_page.enter_eng_name_information(information)
        time.sleep(2)

        self.lk_page.click_submit_button()
        time.sleep(2)

        assert 'Вы успешно отредактировали поле: Имя [eng]' in self.driver.page_source

    def test_lk3(self):
        time.sleep(2)

        self.lk_page.click_username()
        time.sleep(2)

        self.lk_page.click_settings_link()
        time.sleep(2)

        information = '<' + str(random.randint(1, 1000))
        self.lk_page.enter_eng_surname_information(information)
        time.sleep(2)

        self.lk_page.click_submit_button()
        time.sleep(2)

        assert 'Вы успешно отредактировали поле: Фамилия [eng]' in self.driver.page_source
