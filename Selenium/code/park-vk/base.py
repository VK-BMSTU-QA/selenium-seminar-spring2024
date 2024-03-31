import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage

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