from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, 'Войти')
    LOGIN_BUTTON_VK = (By.CLASS_NAME, 'social-link')
    LOGIN = (By.CLASS_NAME, 'vkuiInput__el')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'vkuiButton__in')
    PASSWORD = (By.CLASS_NAME, 'vkc__TextField__input')
    SUBMIT = (By.CLASS_NAME, 'vkc__Button__title')


class HeaderLocators:
    BLOGS = (By.LINK_TEXT, 'Блоги')
    PEOPLE = (By.LINK_TEXT, 'Люди')
    PROGRAM = (By.LINK_TEXT, 'Программа')
    GRADUATES = (By.LINK_TEXT, 'Выпуски')
    SCHEDULE = (By.LINK_TEXT, 'Выпуски')
    VACANCY = (By.LINK_TEXT, 'Вакансии')


class SettingsLocators:
    SUBMIT = (By.NAME, "submit_profile_edit")
    LAST_NAME = (By.ID, 'id_last_name')
