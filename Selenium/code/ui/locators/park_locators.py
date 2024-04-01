from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, 'Войти')
    LOGIN = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')
    SUBMIT = (By.ID, 'popup-login-form-submit')


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
