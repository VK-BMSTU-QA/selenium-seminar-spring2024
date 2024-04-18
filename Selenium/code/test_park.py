import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_park import *
from ui.locators.park_locators import LoginPageLocators, MainPageLocators, SettingsLocators


class TestLogin(BaseCase):
    authorize = False

    def test_login_wrong(self):
        self.login_page.login('123', '123')
        self.login_page.wait(5).until(   # Ждем 5с пока нас либо не перекинет на другую страницу или не покажет ошибку
            EC.any_of(EC.title_contains("Лента"),   
            EC.text_to_be_present_in_element(LoginPageLocators.LOGIN_FORM_ERROR, 'Учётные данные неверны')))
        assert 'Учётные данные неверны' in self.driver.page_source

    def test_login_correct(self):
        self.login_page.login(**(credentials()))
        self.login_page.wait(5).until(
            EC.any_of(EC.title_contains("Лента"),   
            EC.text_to_be_present_in_element(LoginPageLocators.LOGIN_FORM_ERROR, 'Учётные данные неверны')))
        assert 'Блоги' in self.driver.page_source



class TestNavigation(BaseCase):
    authorize = True

    @pytest.mark.parametrize(
        'url,testStrings',
        [
            pytest.param(
                '/blog/',
                [ 'Все блоги', 'Читатели']
            ),
            pytest.param(
                '/people/',
                ['Сообщество проекта']
            ),
            pytest.param(
                '/alumni/',
                ['Наши выпускники']
            ),
            pytest.param(
                '/curriculum/program/',
                ['Мои учебные программы']
            ),
            pytest.param(
                '/schedule/',
                ['Ближайшие две недели', 'Дисциплина', 'Тип события']
            ),
            pytest.param(
                '/career/',
                ['Мои резюме']
            )
        ]
    )
    def test_navigation(self, url, testStrings):
        self.main_page.go_to_section(url)
        self.main_page.wait(2).until(lambda a: self.main_page.is_navigation_active(url))
        assert self.main_page.is_navigation_active(url)
        for s in testStrings:
            assert s in self.driver.page_source


class TestSettings(BaseCase):
    open_settings = True

    def test_settings(self):
        assert "Настройки" in self.driver.title
        old_value = self.settings_page.get_about_value()
        self.settings_page.change_about("очень умный и красивый")
        self.settings_page.wait(5).until(EC.presence_of_element_located(SettingsLocators.SAVE_MESSAGE))
        assert 'О себе' in self.settings_page.get_save_message()
        assert "очень умный и красивый" in self.driver.page_source
        self.settings_page.change_about(old_value)


