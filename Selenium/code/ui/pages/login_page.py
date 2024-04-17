from ui.locators.park_locators import LoginPageLocators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.find(LoginPageLocators.LOGIN).send_keys(user)
        self.find(LoginPageLocators.PASSWORD).send_keys(password)
        self.click(LoginPageLocators.SUBMIT)

        return MainPage(self.driver)
