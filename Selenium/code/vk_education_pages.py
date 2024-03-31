from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from ui.locators import locators


class BasePage(object):
    url = 'https://park.vk.company/'

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    login_locators = locators.LoginPageLocators()

    def login(self, user, password):
        self.click(self.login_locators.LOGIN_BUTTON, timeout=5)

        login = self.find(self.login_locators.LOGIN, timeout=5)
        login.clear()
        login.send_keys(user)

        passwd = self.find(self.login_locators.PASSWORD, timeout=5)
        passwd.clear()
        passwd.send_keys(password)

        self.click(self.login_locators.SUBMIT, timeout=5)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def go_to_menu_items(self, first_item_name, second_item_name):
        self.find((By.LINK_TEXT, first_item_name), timeout=5).click()
        self.find((By.LINK_TEXT, second_item_name), timeout=5).click()


class LKPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'
    lk_page_locators = locators.LKPageLocators()

    def update_info(self, info):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        about = self.find(self.lk_page_locators.ABOUT, timeout=5)
        old = about.text
        about.clear()
        about.send_keys(info)
        self.click(self.lk_page_locators.SUBMIT, timeout=5)

        return old

    def update_last_name(self, last_name):
        self.driver.get('https://park.vk.company/cabinet/settings/')

        last_name_en = self.find(self.lk_page_locators.LAST_NAME_EN, timeout=5)
        old = last_name_en.get_attribute('value')
        last_name_en.clear()
        last_name_en.send_keys(last_name)
        self.click(self.lk_page_locators.SUBMIT, timeout=5)

        return old
