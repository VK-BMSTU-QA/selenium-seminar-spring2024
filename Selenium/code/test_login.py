import pytest
import time
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
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
def credentials(request):
        login = request.config.getoption('--login')
        password = request.config.getoption('--password')
        
        return {"login":login, "password":password}


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    locators = basic_locators.TechnoParkLocators()

    def login(self, user, password):
        div_login = self.find(self.locators.DIV_LOGIN_LOCATOR, timeout=5)
        div_login.click()

        login_input = self.find(self.locators.LOGIN_INPUT_LOCATOR, timeout=5)
        login_input.send_keys(user)

        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR, timeout=5)
        password_input.send_keys(password)

        self.click(self.locators.INPUT_BUTTON_IN_LOGIN_LOCATOR, timeout=5)

        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials["login"], credentials["password"])
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
