import json
import time
import pytest
from _pytest.fixtures import FixtureRequest

from ui.locators.park_locators import LoginPageLocators
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

    @pytest.mark.skip('skip')
    def test_lk1(self):
        pass

    @pytest.mark.skip('skip')
    def test_lk2(self):
        pass

    @pytest.mark.skip('skip')
    def test_lk3(self):
        pass
