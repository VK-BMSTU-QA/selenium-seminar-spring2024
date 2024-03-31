import pytest
import time
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.locators import techno_park_locators as tp_locators


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
    locators = tp_locators.LoginLocators()

    def login(self, credentials: Credentials):
        self.click(self.locators.DIV_LOGIN_LOCATOR, timeout=5)

        login_input = self.find(self.locators.LOGIN_INPUT_LOCATOR, timeout=5)
        login_input.clear()
        login_input.send_keys(credentials.login)

        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR, timeout=5)
        password_input.clear()
        password_input.send_keys(credentials.password)

        self.click(self.locators.INPUT_BUTTON_IN_LOGIN_LOCATOR, timeout=5)

        self.mainPage = MainPage(self.driver)

        return self.mainPage


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'


class TestLogin(BaseCase):

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials)
        assert isinstance(main_page, MainPage)
        assert "Прямой эфир" in self.driver.page_source

class TestLK(BaseCase):

    @pytest.mark.parametrize(
        'locator,sign',
        [
            pytest.param(
                tp_locators.MainLocators.BLOG_LOCATOR, 'Все блоги'
            ),
            pytest.param(
                tp_locators.MainLocators.PEOPLE_LOCATOR, 'Сообщество проекта'
            ),
            pytest.param(
                tp_locators.MainLocators.PROGRAM_LOCATOR, 'Основные программы'
            ),
            pytest.param(
                tp_locators.MainLocators.ALUMNI_LOCATOR, 'Наши выпускники'
            ),
            pytest.param(
                tp_locators.MainLocators.SCHEDULE_LOCATOR, 'Дисциплина'
            ),
            pytest.param(
                tp_locators.MainLocators.CAREER_LOCATOR, 'Вакансии'
            ),
        ],
    )
    def test_one_step_navigation(self, credentials, locator, sign):
        main_page = self.login_page.login(credentials)
        main_page.click(locator, timeout=5)
        assert sign in self.driver.page_source

    @pytest.mark.parametrize(
        'locators,signs',
        [
            pytest.param(
                [tp_locators.MainLocators.BLOG_LOCATOR, tp_locators.MainLocators.PEOPLE_LOCATOR],
                  ['Все блоги', 'Сообщество проекта']
            ),
            pytest.param(
                [tp_locators.MainLocators.ALUMNI_LOCATOR, tp_locators.MainLocators.CAREER_LOCATOR],
                  ['Наши выпускники', 'Вакансии']
            ),
        ],
    )
    def test_two_step_navigation(self, credentials, locators, signs):
        main_page = self.login_page.login(credentials)

        for idx in range (len(locators)):
            main_page.click(locators[idx], timeout=5)
            assert signs[idx] in self.driver.page_source
