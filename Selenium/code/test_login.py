import json
import time
import pytest
from _pytest.fixtures import FixtureRequest

from ui.locators.park_locators import LoginPageLocators, HeaderLocators
from ui.pages.base_page import BasePage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')
            credentials = request.getfixturevalue('credentials')
            self.main_page = self.login_page.login(**credentials)


@pytest.fixture(scope='session')
def credentials():
    with open('./Selenium/code/files/userdata') as file:
        return json.load(file)


@pytest.fixture(scope='session')
def cookies(credentials, config):
    pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(LoginPageLocators.LOGIN_LOCATOR)
        self.find(LoginPageLocators.LOGIN).send_keys(user)
        self.find(LoginPageLocators.PASSWORD).send_keys(password)
        self.click(LoginPageLocators.LOGIN_SUBMIT)
        time.sleep(3)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def switch_sections(self, section_locator1, section_locator2):
        self.go_to_section(section_locator1)
        self.go_to_section(section_locator2)

    def go_to_section(self, section_locator):
        self.find(section_locator).click()
        time.sleep(3)


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        assert 'Блоги' in self.driver.page_source
        assert 'Люди' in self.driver.page_source
        assert 'Программа' in self.driver.page_source
        assert 'Выпуски' in self.driver.page_source
        assert 'Расписание' in self.driver.page_source
        assert 'Вакансии' in self.driver.page_source


class TestLK(BaseCase):

    def test_switch_blogs_to_people(self):
        self.main_page.go_to_section(HeaderLocators.BLOGS_LOCATOR)
        assert 'Все блоги' in self.driver.page_source
        assert 'Прямой эфир' in self.driver.page_source

        self.main_page.go_to_section(HeaderLocators.PEOPLE_LOCATOR)
        assert 'Сообщество проекта' in self.driver.page_source
        assert 'Статистика' in self.driver.page_source
        assert 'Фильтры' in self.driver.page_source

    def test_switch_program_to_graduates(self):
        self.main_page.go_to_section(HeaderLocators.PROGRAM_LOCATOR)
        assert 'Мои учебные программы' in self.driver.page_source
        assert 'Основные программы' in self.driver.page_source
        assert 'Открытые курсы' in self.driver.page_source
        assert 'Архив видео' in self.driver.page_source

        self.main_page.go_to_section(HeaderLocators.GRADUATES_LOCATOR)
        assert 'Наши выпускники' in self.driver.page_source
        assert 'Осень 2023' in self.driver.page_source
        assert 'Весна 2023' in self.driver.page_source

    @pytest.mark.skip('skip')
    def test_lk2(self):
        pass
