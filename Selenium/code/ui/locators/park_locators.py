from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.LINK_TEXT, 'Войти')
    LOGIN_INPUT = (By.NAME, 'login')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_FORM = (By.ID, 'popup-login')


class MainPageLocators:
    def navButtonByUrl(url):
        return (By.XPATH, '//a[@href="'+url+'"]')
    
    DROPDOWN_MENU = (By.CSS_SELECTOR, '#dropdown-user-trigger')
    COG_BTN = (By.CSS_SELECTOR, '.item-settings')

class SettingsLocators:
    ABOUT_FIELD = (By.CSS_SELECTOR, '[name=about]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name=submit_profile_edit]')
    SAVE_MESSAGE = (By.CSS_SELECTOR, '.profile_settings_success-msg')



# class EventsPageLocators(BasePageLocators):
#     pass
