import pytest
import time
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.locators import basic_locators


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)

class Credentials:
     def __init__(self, login, password):
          self.login = login
          self.password = password

@pytest.fixture(scope='session')
def credentials(request):
        login = request.config.getoption('--login')
        password = request.config.getoption('--password')
        
        return Credentials(login, password)


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    locators = basic_locators.TechnoParkLocators()

    def login(self, credentials: Credentials):
        self.click(self.locators.DIV_LOGIN_LOCATOR, timeout=5)

        login_input = self.find(self.locators.LOGIN_INPUT_LOCATOR, timeout=5)
        login_input.send_keys(credentials.login)

        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR, timeout=5)
        password_input.send_keys(credentials.password)

        self.click(self.locators.INPUT_BUTTON_IN_LOGIN_LOCATOR, timeout=5)

        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials)
        assert isinstance(main_page, MainPage)


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
