import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.base_page import PageNotOpenedExeption
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    locators = basic_locators.LoginPageLocators()
    url = "https://park.vk.company/"
    authorize = False

    def login(self, login, password):

        self.click(self.locators.LOGIN_BUTTON)

        login_input = self.find(self.locators.LOGIN_INPUT)
        password_input = self.find(self.locators.PASSWORD_INPUT)

        login_input.send_keys(login)
        password_input.send_keys(password)

        self.click(self.locators.FINAL_LOGIN_BUTTON)
        time.sleep(5)
        return MainPage(self.driver)

    def find_error(self):
        self.find(self.locators.BAD_DATA_MESSAGE)
