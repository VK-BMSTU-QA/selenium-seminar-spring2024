from .base_page import BasePage
from ui.locators.technopark_locators import SettingsLocators


class SettingsPage(BasePage):
    def update_about(self, about):
        about_textarea = self.find(SettingsLocators.ABOUT_TEXTAREA_LOCATOR)
        about_textarea.clear()
        about_textarea.send_keys(about)
        self.click(SettingsLocators.SAVE_BTN_LOCATOR)

