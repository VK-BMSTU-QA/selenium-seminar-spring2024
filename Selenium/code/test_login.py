import json
import random
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By

from vk_education_pages import LoginPage, LKPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.lk_page = LKPage(driver)

        if self.authorize:
            creds = request.getfixturevalue('credentials')
            self.main_page = self.login_page.login(**creds)


@pytest.fixture(scope='session')
def credentials():
    with open('./files/userdata') as file:
        return json.load(file)


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.main_page.click((By.ID, 'dropdown-user-trigger'), timeout=5)
        assert 'Программа' in self.driver.page_source
        assert 'Успеваемость' in self.driver.page_source
        assert 'Мои аккаунты' in self.driver.page_source


class TestMainPage(BaseCase):
    def test_main_page(self):
        self.main_page.go_to_menu_items('Блоги', 'Люди')
        assert 'Сообщество проекта' in self.driver.page_source
        assert 'Рейтинг' in self.driver.page_source

        self.main_page.go_to_menu_items('Программа', 'Выпуски')
        assert 'Наши выпускники' in self.driver.page_source


class TestLK(BaseCase):

    def test_updating_profile_info(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        info = 'selenium seminar ' + str(random.randint(1, 100))
        old = self.lk_page.update_info(info)
        assert info in self.driver.page_source
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source

        self.lk_page.update_info(old)
        assert old in self.driver.page_source
        assert 'Вы успешно отредактировали поле: О себе' in self.driver.page_source

    def test_updating_last_name(self):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        last_name = 'selenium' + str(random.randint(1, 100))
        old = self.lk_page.update_last_name(last_name)
        assert last_name in self.driver.page_source
        assert 'Вы успешно отредактировали поле: Фамилия [eng]' in self.driver.page_source

        self.lk_page.update_last_name(old)
        assert old in self.driver.page_source
        assert 'Вы успешно отредактировали поле: Фамилия [eng]' in self.driver.page_source
