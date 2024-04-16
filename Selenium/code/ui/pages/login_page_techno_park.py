from .base_page import BasePage
from .main_page_techno_park import MainPage
from ui.locators import techno_park_locators as tp_locators
from utils.credentials import Credentials

class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    locators = tp_locators.LoginLocators()
    
    def login(self, credentials: Credentials):
        self.click(self.locators.LOGIN_BUTTON, timeout=5)

        login_input = self.find(self.locators.LOGIN_INPUT, timeout=5)
        login_input.clear()
        login_input.send_keys(credentials.login)

        password_input = self.find(self.locators.PASSWORD_INPUT, timeout=5)
        password_input.clear()
        password_input.send_keys(credentials.password)

        self.click(self.locators.SUBMIT_LOGIN_BUTTON, timeout=5)

        self.mainPage = MainPage(self.driver)

        return self.mainPage


