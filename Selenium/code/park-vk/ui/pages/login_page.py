from .base_page import BasePage
from .main_page import MainPage
from ui.locators.login_locators import LoginPageLocators

class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    locators = LoginPageLocators()

    def login(self, username, password):
        self.click(self.locators.LOGIN_BTN_LOCATOR)

        login_input = self.find(self.locators.LOGIN_INPUT_LOCATOR)
        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR)
        login_input.send_keys(username)
        password_input.send_keys(password)
        self.click(self.locators.LOGIN_SUBMIT_BTN_LOCATOR)

        return MainPage(self.driver)

