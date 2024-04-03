from contextlib import contextmanager

import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.login_page import LoginPage

CLICK_RETRY = 3


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            self.main_page = self.login_page.login(self.config.get("login"), self.config.get("password"))
