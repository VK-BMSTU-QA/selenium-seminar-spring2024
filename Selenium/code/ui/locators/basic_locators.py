from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, "nav__button__menu")
    LOGIN_INPUT = (By.NAME, "login")
    PASSWORD_INPUT = (By.NAME, "password")
    FINAL_LOGIN_BUTTON = (By.NAME, "submit_login")
    BAD_DATA_MESSAGE = (By.CLASS_NAME, "error-message")


class SectionLocators:
    BLOGS = (By.LINK_TEXT, "Блоги")
    PEOPLE = (By.LINK_TEXT, "Люди")
    PROGRAM = (By.LINK_TEXT, "Программа")


class SettingsLocators:
    ABOUT_ME_INPUT = (By.ID, 'profile_about')
    SAVE_BUTTON = (By.NAME, 'submit_profile_edit')



