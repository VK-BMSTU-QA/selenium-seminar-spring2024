import pytest
import time
from base import BaseCase
from ui.locators.header_locators import HeaderSections
from ui.pages.base_page import PageNotOpenedExeption

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login, password = credentials
        self.main_page = self.login_page.login(login, password)
        assert "Лента" in self.driver.title
        assert self.driver.current_url == self.main_page.url
    
    def test_negative_login(self):
        login, password = "definitely_wrong_login", "definitely_wrong_password"
        try:
            self.login_page.login(login, password)
            raise RuntimeError('unexpected successful authentication')
        except PageNotOpenedExeption:
            error_msg = self.login_page.get_error_msg()
            assert len(error_msg) > 0
            assert error_msg == 'Учётные данные неверны'


class TestLK(BaseCase):
    authorize = True

    @pytest.mark.parametrize(
        'src,dst',
        [
            pytest.param(
                HeaderSections.BLOGS,
                HeaderSections.PEOPLE
            ),
            pytest.param(
                HeaderSections.PROGRAMS,
                HeaderSections.GRADUATES
            )
        ]
    )
    def test_header(self, src, dst):
        self.main_page.move_to(src)
        assert self.main_page.is_active_section(src)
        time.sleep(5)
        self.main_page.move_to(dst)
        assert self.main_page.is_active_section(dst)
    
    def test_about_change(self):
        self.settings_page = self.main_page.open_settings()
        assert self.driver.current_url == self.settings_page.url
        assert "Настройки" in self.driver.title
        time.sleep(5)
        self.settings_page.update_about('test')
        assert self.settings_page.get_about() == 'test'
        assert "О себе" in self.settings_page.get_success_msg()
        time.sleep(5)
        self.settings_page.update_about('')
