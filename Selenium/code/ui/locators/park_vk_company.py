from selenium.webdriver.common.by import By
from enum import Enum

class HeaderLocators(Enum):
    BLOG_BTN_LOCATOR = (By.CLASS_NAME, 'technopark__menu__item_3')
    PEOPLE_BTN_LOCATOR = (By.CLASS_NAME, 'technopark__menu__item_4')
    PROGRAMS_BTN_LOCATOR = (By.CLASS_NAME, 'technopark__menu__item_41')
    GRADUATES_BTN_LOCATOR = (By.CLASS_NAME, 'technopark__menu__item_42')
    ACTIVE_SECTION_LOCATOR = (By.CLASS_NAME, 'active')
    DROPDOWN_BTN_LOCATOR = (By.ID, 'dropdown-user-trigger')
    SETTINGS_BTN_LOCATOR = (By.CLASS_NAME, 'item-settings')


class LoginPageLocators:
    LOGIN_BTN_LOCATOR = (By.CLASS_NAME, 'nav__button__menu>a')
    LOGIN_INPUT_LOCATOR = (By.NAME, 'login')
    PASSWORD_INPUT_LOCATOR = (By.NAME, 'password')
    LOGIN_SUBMIT_BTN_LOCATOR = (By.ID, 'popup-login-form-submit')

class SettingsPageLocators:
    ABOUT_TEXTAREA_LOCATOR = (By.NAME, 'about')
    SAVE_BTN_LOCATOR = (By.NAME, 'submit_profile_edit')
    SUCCESS_MSG_LOCATOR = (By.CLASS_NAME, 'profile_settings_success-msg')