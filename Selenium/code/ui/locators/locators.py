from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, 'Войти')
    LOGIN = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')
    SUBMIT = (By.ID, 'popup-login-form-submit')
