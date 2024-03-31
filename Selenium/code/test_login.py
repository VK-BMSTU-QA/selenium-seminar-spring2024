import json
import time
import pytest
from _pytest.fixtures import FixtureRequest

from ui.locators.park_locators import (
    LoginPageLocators,
    HeaderLocators,
    SettingsLocators,
)
from ui.pages.base_page import BasePage


@pytest.fixture(scope='session')
def credentials():
    with open('./Selenium/code/files/userdata') as file:
        return json.load(file)


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.login_setup(request)

    def login_setup(self, request):
        pass


class LogedCase(BaseCase):
    def login_setup(self, request):
        credentials = request.getfixturevalue('credentials')
        self.main_page = self.login_page.login(**credentials)


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(LoginPageLocators.LOGIN_BUTTON, timeout=5)

        login_input = self.find(LoginPageLocators.LOGIN, timeout=5)
        login_input.clear()
        login_input.send_keys(user)

        password_input = self.find(LoginPageLocators.PASSWORD, timeout=5)
        password_input.clear()
        password_input.send_keys(password)

        self.click(LoginPageLocators.SUBMIT, timeout=5)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def switch_sections(self, section_locator1, section_locator2):
        self.go_to_section(section_locator1)
        self.go_to_section(section_locator2)

    def go_to_section(self, section_locator):
        self.find(section_locator, timeout=5).click()

    def update_profile_about(self, new_info: str) -> str:
        text_area = self.find(SettingsLocators.PROFILE_ABOUT, timeout=5)
        old_info = text_area.text
        text_area.clear()
        text_area.send_keys(new_info)
        self.find(SettingsLocators.SUBMIT, timeout=5).click()
        return old_info


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        main_page = self.login_page.login(**credentials)
        assert 'Блоги' in self.driver.page_source
        assert 'Люди' in self.driver.page_source
        assert 'Программа' in self.driver.page_source
        assert 'Выпуски' in self.driver.page_source
        assert 'Расписание' in self.driver.page_source
        assert 'Вакансии' in self.driver.page_source


class TestLK(LogedCase):
    @pytest.mark.parametrize(
        'locator_from,expected_from,locator_to,expected_to',
        [
            pytest.param(
                HeaderLocators.BLOGS, ['Все блоги', 'Прямой эфир'],
                HeaderLocators.PEOPLE, [
                    'Сообщество проекта', 'Статистика', 'Фильтры'
                ],
            ),
            pytest.param(
                HeaderLocators.PROGRAM, [
                    'Мои учебные программы',
                    'Основные программы',
                    'Открытые курсы',
                    'Архив видео',
                ],
                HeaderLocators.GRADUATES, [
                    'Наши выпускники',
                    'Осень 2023',
                    'Весна 2023',
                ],
            ),
        ]
    )
    def test_switch_sections(
        self,
        locator_from,
        expected_from,
        locator_to,
        expected_to,
    ):
        self.main_page.go_to_section(locator_from)
        for item in expected_from:
            assert item in self.driver.page_source

        self.main_page.go_to_section(locator_to)
        for item in expected_to:
            assert item in self.driver.page_source

    def test_change_profile_about(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')
        assert 'О себе' in self.driver.page_source
        assert 'Вы успешно отредактировали поле: О себе' not in self.driver.page_source

        old_info = self.main_page.update_profile_about('updated info')
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source
        assert 'updated info' in self.driver.page_source

        self.main_page.update_profile_about(old_info)
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source
        assert old_info in self.driver.page_source
