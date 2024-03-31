from selenium.webdriver.common.by import By

class LoginLocators:
    DIV_LOGIN_LOCATOR = (By.CLASS_NAME, 'nav__button__menu')
    LOGIN_INPUT_LOCATOR = (By.NAME, 'login')
    PASSWORD_INPUT_LOCATOR = (By.NAME, 'password')
    INPUT_BUTTON_IN_LOGIN_LOCATOR = (By.ID, 'popup-login-form-submit')

class MainLocators:
    BLOG_LOCATOR = (By.XPATH, '//a[contains(@href,"/blog/")]')
    PEOPLE_LOCATOR = (By.XPATH, '//a[contains(@href,"/people/")]')
    PROGRAM_LOCATOR = (By.XPATH, '//a[contains(@href,"/curriculum/program/")]')
    ALUMNI_LOCATOR = (By.XPATH, '//a[contains(@href,"/alumni/")]')
    SCHEDULE_LOCATOR = (By.XPATH, '//a[contains(@href,"/schedule/")]')
    CAREER_LOCATOR = (By.XPATH, '//a[contains(@href,"/career/")]')

