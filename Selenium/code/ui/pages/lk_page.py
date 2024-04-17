from ui.locators.park_locators import SettingsLocators, HeaderLocators
from ui.pages.base_page import BasePage


class LkPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    def update_last_name(self, last_name):
        last_name_ru = self.find(SettingsLocators.LAST_NAME)
        old = last_name_ru.get_attribute('value')
        last_name_ru.clear()
        last_name_ru.send_keys(last_name)
        self.click(SettingsLocators.SUBMIT)

        return old

    def from_main_go_to_settings(self):
        self.click(SettingsLocators.DROPDOWN)
        self.click(SettingsLocators.SETTINGS)
        self.find(HeaderLocators.HEADER)
