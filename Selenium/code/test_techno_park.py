import pytest
from _pytest.fixtures import FixtureRequest

from ui.locators import techno_park_locators as tp_locators
from ui.pages.main_page_techno_park import MainPage
from ui.pages.login_page_techno_park import LoginPage
from ui.pages.settings_page_techno_park import SettingsPage

class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup_base_case(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)

        return self.login_page

@pytest.mark.usefixtures('setup_base_case')
class LoggedCase(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, setup_base_case, credentials):
        self.main_page = setup_base_case.login(credentials)

class TestLogin(BaseCase):

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials)
        assert isinstance(main_page, MainPage)
        assert "Прямой эфир" in self.driver.page_source

class TestLK(LoggedCase):
    @pytest.mark.parametrize(
        'locator,sign_expected',
        [
            pytest.param(
                tp_locators.MainLocators.BLOG_BUTTON, 'Все блоги'
            ),
            pytest.param(
                tp_locators.MainLocators.PEOPLE_BUTTON, 'Сообщество проекта'
            ),
            pytest.param(
                tp_locators.MainLocators.PROGRAM_BUTTON, 'Основные программы'
            ),
            pytest.param(
                tp_locators.MainLocators.ALUMNI_BUTTON, 'Наши выпускники'
            ),
            pytest.param(
                tp_locators.MainLocators.SCHEDULE_BUTTON, 'Дисциплина'
            ),
            pytest.param(
                tp_locators.MainLocators.CAREER_BUTTON, 'Вакансии'
            ),
        ],
    )
    def test_one_step_navigation(self,  locator, sign_expected):
        self.main_page.click(locator, timeout=5)
        assert sign_expected in self.driver.page_source

    @pytest.mark.parametrize(
        'locators,signs_expected',
        [
            pytest.param(
                [tp_locators.MainLocators.BLOG_BUTTON, tp_locators.MainLocators.PEOPLE_BUTTON],
                  ['Все блоги', 'Сообщество проекта']
            ),
            pytest.param(
                [tp_locators.MainLocators.ALUMNI_BUTTON, tp_locators.MainLocators.CAREER_BUTTON],
                  ['Наши выпускники', 'Вакансии']
            ),
        ],
    )
    def test_two_step_navigation(self, locators, signs_expected):
        for idx in range (len(locators)):
            self.main_page.click(locators[idx], timeout=5)
            assert signs_expected[idx] in self.driver.page_source
    
    @pytest.mark.parametrize(
        'about_info,sign_expected',
        [
            pytest.param(
                'Я тестирую настройки', 'Я тестирую настройки'
            ),
            pytest.param(
                'Проверка xss “”></script><img src onerror=alert()>', 'Проверка xss'
            ),
        ],
    )
    def test_settings_change_about(self, about_info, sign_expected):
        settings_page = SettingsPage(self.driver)

        original_text = settings_page.update_about_info(about_info)
        assert original_text not in self.driver.page_source
        assert sign_expected in self.driver.page_source

        settings_page.update_about_info(original_text)
        assert original_text in self.driver.page_source
        assert sign_expected not in self.driver.page_source
