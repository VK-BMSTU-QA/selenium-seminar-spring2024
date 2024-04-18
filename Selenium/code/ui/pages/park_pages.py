from selenium.webdriver.common.keys import Keys

from ui.pages.base_page import BasePage
from ui.locators.park_locators import *


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.find(LoginPageLocators.LOGIN_INPUT).send_keys(user)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(Keys.ENTER)


class SettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    def change_about(self, text):
        about_field = self.find(SettingsLocators.ABOUT_FIELD)
        about_field.clear()
        about_field.send_keys(text)
        self.click(SettingsLocators.SUBMIT_BUTTON)

    def get_about_value(self):
        about_field = self.find(SettingsLocators.ABOUT_FIELD)
        return about_field.get_attribute('value')

    def get_save_message(self):
        return self.find(SettingsLocators.SAVE_MESSAGE).text



class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def is_navigation_active(self, url):
        item = self.find(MainPageLocators.navButtonByUrl(url))
        return "active" in item.get_attribute('class')

    def go_to_section(self, url):
        self.click(MainPageLocators.navButtonByUrl(url))

    def open_settings(self):
        self.click(MainPageLocators.DROPDOWN_MENU)
        self.click(MainPageLocators.COG_BTN)
        return SettingsPage(self.driver)
