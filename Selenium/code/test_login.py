import json
import time
import pytest
from _pytest.fixtures import FixtureRequest

from ui.locators.park_locators import LoginPageLocators, HeaderLocators, SettingsLocators
from ui.pages.base_page import BasePage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')
            credentials = request.getfixturevalue('credentials')
            self.main_page = self.login_page.login(**credentials)


@pytest.fixture(scope='session')
def credentials():
    with open('./Selenium/code/files/userdata') as file:
        return json.load(file)


@pytest.fixture(scope='session')
def cookies(credentials, config):
    pass


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(LoginPageLocators.LOGIN_LOCATOR)
        self.find(LoginPageLocators.LOGIN).send_keys(user)
        self.find(LoginPageLocators.PASSWORD).send_keys(password)
        self.click(LoginPageLocators.SUBMIT)
        time.sleep(3)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def switch_sections(self, section_locator1, section_locator2):
        self.go_to_section(section_locator1)
        self.go_to_section(section_locator2)

    def go_to_section(self, section_locator):
        self.find(section_locator).click()
        time.sleep(3)

    def update_profile_about(self, new_info: str) -> str:
        text_area = self.find(SettingsLocators.PROFILE_ABOUT)
        old_info = text_area.text
        text_area.clear()
        text_area.send_keys(new_info)
        self.find(SettingsLocators.SUBMIT).click()
        time.sleep(3)
        return old_info


class TestLogin(BaseCase):
    authorize = True

    # @pytest.mark.skip('skip')
    def test_login(self, credentials):
        assert 'Блоги' in self.driver.page_source
        assert 'Люди' in self.driver.page_source
        assert 'Программа' in self.driver.page_source
        assert 'Выпуски' in self.driver.page_source
        assert 'Расписание' in self.driver.page_source
        assert 'Вакансии' in self.driver.page_source


class TestLK(BaseCase):

    # @pytest.mark.skip('skip')
    def test_switch_blogs_to_people(self):
        self.main_page.go_to_section(HeaderLocators.BLOGS)
        assert 'Все блоги' in self.driver.page_source
        assert 'Прямой эфир' in self.driver.page_source

        self.main_page.go_to_section(HeaderLocators.PEOPLE)
        assert 'Сообщество проекта' in self.driver.page_source
        assert 'Статистика' in self.driver.page_source
        assert 'Фильтры' in self.driver.page_source

    # @pytest.mark.skip('skip')
    def test_switch_program_to_graduates(self):
        self.main_page.go_to_section(HeaderLocators.PROGRAM)
        assert 'Мои учебные программы' in self.driver.page_source
        assert 'Основные программы' in self.driver.page_source
        assert 'Открытые курсы' in self.driver.page_source
        assert 'Архив видео' in self.driver.page_source

        self.main_page.go_to_section(HeaderLocators.GRADUATES)
        assert 'Наши выпускники' in self.driver.page_source
        assert 'Осень 2023' in self.driver.page_source
        assert 'Весна 2023' in self.driver.page_source

    # @pytest.mark.skip('skip')
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
