from ui.pages.base_page import BasePage
from ui.locators import basic_locators


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    locators = basic_locators.SettingsLocators()

    def fill_about_input(self, value):
        about_field = self.find(self.locators.ABOUT_ME_INPUT)
        about_field.clear()
        about_field.send_keys(value)

    def save(self):
        self.click(self.locators.SAVE_BUTTON)

    def update_about_input(self, value):
        self.fill_about_input(value)
        self.save()

    def get_about_value(self):
        return self.find(self.locators.ABOUT_ME_INPUT).text
