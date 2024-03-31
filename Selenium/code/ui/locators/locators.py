from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, 'Войти')
    LOGIN = (By.NAME, 'login')
    PASSWORD = (By.NAME, 'password')
    SUBMIT = (By.ID, 'popup-login-form-submit')


class LKPageLocators:
    ABOUT = (By.ID, "profile_about")
    SUBMIT = (By.NAME, "submit_profile_edit")
    LAST_NAME_EN = (By.ID, 'id_last_name_en')
