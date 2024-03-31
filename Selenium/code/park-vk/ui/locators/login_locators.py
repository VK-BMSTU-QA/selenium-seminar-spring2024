from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, '.nav__button__menu > a')
    LOGIN_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name=login]')
    PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name=password]')
    LOGIN_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, '#popup-login-form-submit')
    ERROR_MSG_LOCATOR = (By.CSS_SELECTOR, '#popup-login-form > .error-message')
