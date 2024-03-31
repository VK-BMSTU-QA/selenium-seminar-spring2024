import json

import pytest
from _pytest.fixtures import FixtureRequest

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

        if self.authorize:
            print('Do something for login')
            creds = request.getfixturevalue('credentials')
            self.login_page.login(**creds)


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
    locators = locators.LoginPageLocators()

    def login(self, user, password):
        self.click(self.locators.LOGIN_BUTTON)
        self.find(self.locators.LOGIN).send_keys(user)
        self.find(self.locators.PASSWORD).send_keys(password)
        self.click(self.locators.SUBMIT)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        print('test login')
        assert 1 == 1


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
