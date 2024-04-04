from selenium.webdriver.common.by import By
from .header_locators import HeaderLocators

class SettingsPageLocators:
    header = HeaderLocators()

    ABOUT_TEXTAREA_LOCATOR = (By.CSS_SELECTOR, '[name=about]')
    SAVE_BTN_LOCATOR = (By.CSS_SELECTOR, '[name=submit_profile_edit]')
    SUCCESS_MSG_LOCATOR = (By.CSS_SELECTOR, '.profile_settings_success-msg')
