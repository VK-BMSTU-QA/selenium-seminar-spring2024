from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, 'Войти')
    LOGIN_INPUT = (By.NAME, 'login')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_FORM = (By.ID, 'popup-login')
    LOGIN_FORM_ERROR = (By.CSS_SELECTOR, '.validate-error-login')


class MainPageLocators:
    def navButtonByUrl(url):
        return (By.CSS_SELECTOR, '.technopark__menu__item:has(a[href="'+ url +'"])')
    
    DROPDOWN_MENU = (By.CSS_SELECTOR, '#dropdown-user-trigger')
    COG_BTN = (By.CSS_SELECTOR, '.item-settings')

class SettingsLocators:
    ABOUT_FIELD = (By.CSS_SELECTOR, '[name=about]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name=submit_profile_edit]')
    SAVE_MESSAGE = (By.CSS_SELECTOR, '.profile_settings_success-msg')
