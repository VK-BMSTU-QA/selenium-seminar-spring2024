import pytest
import time
from base import BaseCase
from ui.locators.header_locators import HeaderSections

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login, password = credentials
        self.main_page = self.login_page.login(login, password)
        assert "Лента" in self.driver.title
        assert self.driver.current_url == self.main_page.url


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
