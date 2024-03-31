import pytest
import time
import os

from _pytest.fixtures import FixtureRequest
from urllib.parse import urlparse
from ui.pages.base_page import BasePage
from ui.pages.settings_page import SettingsPage
from ui.locators.technopark_locators import LoginPageLocators, BasePageLocators, SettingsLocators
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            user, password = request.getfixturevalue('credentials')
            self.main_page = self.login_page.login(user, password)
            self.settings_page = SettingsPage(driver)

    
@pytest.fixture(scope='session')
def credentials():
    user = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    return user, password


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(LoginPageLocators.LOGIN_BUTTON_LOCATOR_CLASS)
        loginInput = self.find(LoginPageLocators.LOGIN_FORM_INPUT)
        loginInput.send_keys(user)

        passwordInput = self.find(LoginPageLocators.PASSWORD_FORM_INPUT)
        passwordInput.send_keys(password)

        self.click(LoginPageLocators.SUBMIT_FORM_INPUT)
        time.sleep(4)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def go_to_events_handler(self, link):
        events_button = self.find(link)
        # self.click(events_button)
        self.find()

    def check_active(self, swch_elem):
        return "active" in swch_elem.get_attribute("class").split()


class TestLogin(BaseCase):
    authorize = True
    
    @pytest.mark.skip('skip')
    def test_login(self, credentials):
        current_url = self.driver.current_url
        parsed_url = urlparse(current_url)
        assert parsed_url.path == '/feed/', f"Unexpected URL: {current_url}"

        username_element = self.login_page.find(LoginPageLocators.PROFILE_USERNAME_LOCATOR)
        assert username_element is not None, "Username element is not found"
        assert username_element.text.strip() != "", "Username is empty"

class TestSwith(BaseCase):
    authorize = True

    @pytest.mark.parametrize(
        'swch1,swch2',
        [
            pytest.param(
                BasePageLocators.BLOG_LOCATOR_LINK,
                BasePageLocators.PEOPLE_LOCATOR_LINK
            ),
            pytest.param(
                BasePageLocators.PROGRAM_LOCATOR_LINK,
                BasePageLocators.GRADUATES_LOCATOR_LINK
            )
        ]
    )   

    @pytest.mark.skip('skip')
    def test_switch(self, swch1, swch2):
        self.main_page.click(swch1)
        swch1_elem = self.main_page.find(swch1)
        assert self.main_page.check_active(swch1_elem), f"{swch1} doesn't have the 'activate' class"
        
        self.main_page.click(swch2)
        swch2_elem = self.main_page.find(swch2)
        assert self.main_page.check_active(swch2_elem), f"{swch2} doesn't have the 'activate' class"

class TestUpdate(BaseCase):
    authorize = True

#    @pytest.mark.skip('skip')
    def test_update_info(self):
        self.click(SettingsLocators.DROPDOWN_BTN_LOCATOR)
        self.click(SettingsLocators.SETTINGS_BTN_LOCATOR)        
        time.sleep(2)

        assert 'О себе' in self.driver.page_source
        assert 'Вы успешно отредактировали поле: О себе' not in self.driver.page_source

        old_info = self.settings_page.update_about('test text')
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source
        assert 'test text' in self.driver.page_source

        self.settings_page.update_about(old_info)
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source
        assert old_info in self.driver.page_source

