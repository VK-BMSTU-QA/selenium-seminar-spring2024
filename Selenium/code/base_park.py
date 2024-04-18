import pytest
import json
from _pytest.fixtures import FixtureRequest

from ui.pages.park_pages import LoginPage, MainPage, SettingsPage

def credentials():
    with open('./Selenium/code/files/userdata') as file:
        return json.load(file)


class BaseCase:
    authorize = True
    open_settings = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            creds = credentials()
            self.login_page.login(**creds)
            self.main_page = MainPage(self.driver)
            if self.open_settings:
                self.settings_page = self.main_page.open_settings()