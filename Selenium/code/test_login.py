import json
import time
import random

import pytest
from _pytest.fixtures import FixtureRequest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from ui.locators.park_locators import LoginPageLocators, SettingsLocators, HeaderLocators


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.lk_page = LkPage(driver)

        if self.authorize:
            print('Do something for login')
            creds = request.getfixturevalue('credentials')
            self.main_page = self.login_page.login(**creds)


@pytest.fixture(scope='session')
def credentials():
    with open('./Selenium/code/files/userdata') as file:
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

    def login(self, user, password):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.click(LoginPageLocators.LOGIN_BUTTON_VK)
        self.find(LoginPageLocators.LOGIN).send_keys(user)
        self.click(LoginPageLocators.CONTINUE_BUTTON)
        self.find(LoginPageLocators.PASSWORD).send_keys(password)
        self.click(LoginPageLocators.CONTINUE_BUTTON)
        self.click(LoginPageLocators.SUBMIT)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def go_to_menu_items(self, first_item_name, second_item_name):
        self.find((By.LINK_TEXT, first_item_name)).click()
        time.sleep(2)

        self.find((By.LINK_TEXT, second_item_name)).click()
        time.sleep(2)


class LkPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    def update_last_name(self, last_name):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        time.sleep(2)

        last_name_en = self.find(SettingsLocators.LAST_NAME)
        last_name_en.clear()
        last_name_en.send_keys(last_name)
        self.click(SettingsLocators.SUBMIT)


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        assert 'Блоги' in self.driver.page_source
        assert 'Люди' in self.driver.page_source
        assert 'Программа' in self.driver.page_source
        assert 'Выпуски' in self.driver.page_source
        assert 'Расписание' in self.driver.page_source
        assert 'Вакансии' in self.driver.page_source


class TestLk(BaseCase):
    # @pytest.mark.skip('skip')
    def test_blogs(self):
        self.main_page.find(HeaderLocators.BLOGS).click()
        assert 'Все блоги' in self.driver.page_source
        assert 'Прямой эфир' in self.driver.page_source

    def test_people(self):
        self.main_page.find(HeaderLocators.PEOPLE).click()
        assert 'Сообщество проекта' in self.driver.page_source
        assert 'Статистика' in self.driver.page_source
        assert 'Фильтры' in self.driver.page_source

    def test_program(self):
        self.main_page.find(HeaderLocators.PROGRAM).click()
        assert 'Мои учебные программы' in self.driver.page_source
        assert 'Основные программы' in self.driver.page_source
        assert 'Открытые курсы' in self.driver.page_source
        assert 'Архив видео' in self.driver.page_source

    def test_graduates(self):
        self.main_page.find(HeaderLocators.GRADUATES).click()
        assert 'Наши выпускники' in self.driver.page_source

    def test_schedule(self):
        self.main_page.find(HeaderLocators.SCHEDULE).click()
        assert 'Показывать' in self.driver.page_source
        assert 'Дисциплина' in self.driver.page_source
        assert 'Тип события' in self.driver.page_source
        assert 'Группа' in self.driver.page_source

    def test_vacancy(self):
        self.main_page.find(HeaderLocators.VACANCY).click()
        assert 'Вакансии' in self.driver.page_source
        assert 'Прямой эфир' in self.driver.page_source


class TestLK(BaseCase):

    # @pytest.mark.skip('skip')
    def test_settings(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        assert 'Фамилия [рус]' in self.driver.page_source
        assert 'Имя [рус]' in self.driver.page_source
        assert 'Фамилия [eng]' in self.driver.page_source
        assert 'Имя [eng]' in self.driver.page_source
        assert 'Дата рождения' in self.driver.page_source
        assert 'Номер телефона' in self.driver.page_source
        assert 'О себе' in self.driver.page_source
        assert 'Фотография' in self.driver.page_source
        assert 'Пол' in self.driver.page_source
        assert 'Размер одежды' in self.driver.page_source

    def test_change_last_name(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        assert 'О себе' in self.driver.page_source
        assert 'Вы успешно отредактировали поле' not in self.driver.page_source

        last_name = 'Тест'
        self.lk_page.update_last_name(last_name)
        time.sleep(2)
        assert 'Вы успешно отредактировали поле: Фамилия [рус]' in self.driver.page_source
        assert last_name in self.driver.page_source
