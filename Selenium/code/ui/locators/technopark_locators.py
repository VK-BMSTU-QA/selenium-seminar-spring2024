from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR_CLASS = (By.CLASS_NAME, 'nav__button__menu')
    LOGIN_FORM_INPUT = (By.NAME, 'login')
    PASSWORD_FORM_INPUT = (By.NAME, 'password')
    SUBMIT_FORM_INPUT = (By.NAME, 'submit_login')
    PROFILE_USERNAME_LOCATOR = (By.CLASS_NAME, 'username')

class BasePageLocators:
    BLOG_LOCATOR_LINK = (By.CSS_SELECTOR, '.technopark__menu__item_3')
    PEOPLE_LOCATOR_LINK = (By.CSS_SELECTOR, '.technopark__menu__item_4')
    PROGRAM_LOCATOR_LINK = (By.CSS_SELECTOR, '.technopark__menu__item_41')
    GRADUATES_LOCATOR_LINK = (By.CSS_SELECTOR, '.technopark__menu__item_42')

class SettingsLocators:
    ABOUT_TEXTAREA_LOCATOR = (By.CSS_SELECTOR, '[name=about]')
    SAVE_BTN_LOCATOR = (By.CSS_SELECTOR, '[name=submit_profile_edit]')
    SUCCESS_MSG_LOCATOR = (By.CSS_SELECTOR, '.profile_settings_success-msg')
    DROPDOWN_BTN_LOCATOR = (By.CSS_SELECTOR, '#dropdown-user-trigger')
    SETTINGS_BTN_LOCATOR = (By.CSS_SELECTOR, '.item-settings')