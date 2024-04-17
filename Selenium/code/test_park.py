from base import BaseCase
from ui.locators.park_locators import SettingsLocators, HeaderLocators


class TestLogin(BaseCase):
    authorize = True

    def test_login(self):
        self.main_page.find(HeaderLocators.BLOGS)
        assert 'Блоги' in self.driver.page_source
        assert 'Люди' in self.driver.page_source
        assert 'Программа' in self.driver.page_source
        assert 'Выпуски' in self.driver.page_source
        assert 'Расписание' in self.driver.page_source
        assert 'Вакансии' in self.driver.page_source


class TestRedirect(BaseCase):
    authorize = True

    def test_blogs_to_people(self):
        self.main_page.find(HeaderLocators.BLOGS).click()
        self.main_page.find(HeaderLocators.HEADER)
        assert 'Все блоги' in self.driver.page_source
        assert 'Прямой эфир' in self.driver.page_source

        self.main_page.find(HeaderLocators.PEOPLE).click()
        self.main_page.find(HeaderLocators.HEADER)
        assert 'Сообщество проекта' in self.driver.page_source
        assert 'Статистика' in self.driver.page_source
        assert 'Фильтры' in self.driver.page_source

    def test_program_to_vacancy(self):
        self.main_page.find(HeaderLocators.PROGRAM).click()
        self.main_page.find(HeaderLocators.HEADER)
        assert 'Мои учебные программы' in self.driver.page_source
        assert 'Основные программы' in self.driver.page_source
        assert 'Открытые курсы' in self.driver.page_source
        assert 'Архив видео' in self.driver.page_source

        self.main_page.find(HeaderLocators.VACANCY).click()
        self.main_page.find(HeaderLocators.HEADER)
        assert 'Вакансии' in self.driver.page_source
        assert 'Прямой эфир' in self.driver.page_source


class TestLK(BaseCase):
    authorize = True

    def test_settings(self):
        self.lk_page.from_main_go_to_settings()
        assert 'Имя [рус]' in self.driver.page_source
        assert 'Фамилия [eng]' in self.driver.page_source
        assert 'Имя [eng]' in self.driver.page_source
        assert 'Дата рождения' in self.driver.page_source
        assert 'Номер телефона' in self.driver.page_source
        assert 'О себе' in self.driver.page_source
        assert 'Фотография' in self.driver.page_source
        assert 'Пол' in self.driver.page_source
        assert 'Размер одежды' in self.driver.page_source

    def test_change_last_name(self):
        self.lk_page.from_main_go_to_settings()

        assert 'О себе' in self.driver.page_source
        assert 'Вы успешно отредактировали поле' not in self.driver.page_source

        last_name = 'Тест'
        old = self.lk_page.update_last_name(last_name)

        self.main_page.find(SettingsLocators.DROPDOWN)
        assert 'Вы успешно отредактировали поле: Фамилия' in self.driver.page_source
        assert last_name in self.driver.page_source

        self.lk_page.update_last_name(old)
        self.main_page.find(SettingsLocators.DROPDOWN)
        assert 'Вы успешно отредактировали поле: Фамилия' in self.driver.page_source
