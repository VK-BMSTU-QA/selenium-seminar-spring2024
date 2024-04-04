from .base_page import BasePage
from ui.locators.settings_locators import SettingsPageLocators

class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    locators = SettingsPageLocators()

    def get_about(self):
        about_textarea = self.find(self.locators.ABOUT_TEXTAREA_LOCATOR)
        return about_textarea.text
    
    def get_success_msg(self):
        return self.find(self.locators.SUCCESS_MSG_LOCATOR).text

    def update_about(self, about):
        about_textarea = self.find(self.locators.ABOUT_TEXTAREA_LOCATOR)
        about_textarea.clear()
        about_textarea.send_keys(about)
        self.click(self.locators.SAVE_BTN_LOCATOR)
