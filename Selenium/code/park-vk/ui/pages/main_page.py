from .base_page import BasePage
from ui.locators.main_locators import MainPageLocators

from .settings_page import SettingsPage

class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'
    locators = MainPageLocators()

    def is_active_section(self, section):
        section = self.find(self.locators.header.get_locator_by_section(section))
        return "active" in section.get_attribute('class')

    def move_to(self, section):
        self.click(self.locators.header.get_locator_by_section(section))
    
    def open_settings(self):
        self.click(self.locators.header.DROPDOWN_BTN_LOCATOR)
        self.click(self.locators.header.SETTINGS_BTN_LOCATOR)
        return SettingsPage(self.driver)
