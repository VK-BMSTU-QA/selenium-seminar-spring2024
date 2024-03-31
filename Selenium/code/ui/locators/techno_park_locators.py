from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, 'nav__button__menu')
    LOGIN_INPUT = (By.NAME, 'login')
    PASSWORD_INPUT = (By.NAME, 'password')
    SUBMIT_LOGIN_BUTTON = (By.ID, 'popup-login-form-submit')

class MainLocators:
    BLOG_BUTTON = (By.XPATH, '//a[contains(@href,"/blog/")]')
    PEOPLE_BUTTON = (By.XPATH, '//a[contains(@href,"/people/")]')
    PROGRAM_BUTTON = (By.XPATH, '//a[contains(@href,"/curriculum/program/")]')
    ALUMNI_BUTTON = (By.XPATH, '//a[contains(@href,"/alumni/")]')
    SCHEDULE_BUTTON = (By.XPATH, '//a[contains(@href,"/schedule/")]')
    CAREER_BUTTON = (By.XPATH, '//a[contains(@href,"/career/")]')

class SettingsLocators:
    ABOUT_INPUT = (By.NAME, 'about')
    SUBMIT_EDIT = (By.NAME, 'submit_profile_edit')
