from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LOCATOR = (By.LINK_TEXT, 'Войти')
    LOGIN = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')
    LOGIN_SUBMIT = (By.ID, 'popup-login-form-submit')


class HeaderLocators:
    BLOGS_LOCATOR = (By.LINK_TEXT, 'Блоги')
    PEOPLE_LOCATOR = (By.LINK_TEXT, 'Люди')
    PROGRAM_LOCATOR = (By.LINK_TEXT, 'Программа')
    GRADUATES_LOCATOR = (By.LINK_TEXT, 'Выпуски')
