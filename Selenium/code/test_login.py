import pytest
from ui.pages.base_page import PageNotOpenedExeption
from base import BaseCase
from ui.locators.basic_locators import SectionLocators
from ui.fixtures import settings_page


@pytest.fixture(scope='session')
def credentials():
        pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        self.main_page = self.login_page.login(self.config.get("login"), self.config.get("password"))
        assert self.driver.current_url == "https://park.vk.company/feed/"

    def test_invalid_login(self, credentials):
        with pytest.raises(PageNotOpenedExeption):
            self.main_page = self.login_page.login("test", "test_password")
        assert self.driver.current_url == "https://park.vk.company/"


class TestSections(BaseCase):
    authorize = True

    section_locators = SectionLocators()

    section_test_data = [
        ('feed/', section_locators.BLOGS, 'blog/'),
        ('blog/', section_locators.PEOPLE, 'people/'),
        ('people/', section_locators.PROGRAM, 'curriculum/program/mine/')
    ]

    @pytest.mark.parametrize('original_url,section_locator,target_url', section_test_data)
    def test_section_changing(self, main_page, original_url, section_locator, target_url):
        self.driver.get('https://park.vk.company/' + original_url)
        main_page.click(section_locator)
        assert self.driver.current_url == 'https://park.vk.company/' + target_url


class TestSettings(BaseCase):
    authorize = True
    url = 'https://park.vk.company/cabinet/settings/'

    information = [
        'Студентка кафедры ИУ6',
        'Группа ИУ6-61Б'
    ]

    @pytest.mark.parametrize('new_information', information)
    def test_settings(self, settings_page, new_information):
        old_value = settings_page.get_about_value()
        settings_page.update_about_input(new_information)

        assert settings_page.get_about_value() == new_information

        settings_page.update_about_input(old_value)
