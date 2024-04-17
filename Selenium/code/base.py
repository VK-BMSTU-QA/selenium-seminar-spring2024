import json

import pytest

from ui.pages.lk_page import LkPage
from ui.pages.login_page import LoginPage

CLICK_RETRY = 3


def credentials():
    with open('./Selenium/code/files/userdata') as file:
        return json.load(file)


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.lk_page = LkPage(driver)

        if self.authorize:
            self.main_page = self.login_page.login(**credentials())
