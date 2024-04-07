from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass


class BaseParkPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#header .nav__button__menu')
    LOGIN_INPUT = (By.NAME, 'login')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_SUBMIT_BUTTON = (By.ID, 'popup-login-form-submit')
    LOGO_IMG = (By.CSS_SELECTOR, '#header img')

class MainParkPageLocators(BaseParkPageLocators):
    BLOGS_BUTTON = (By.CSS_SELECTOR, '#header a[href="/blog/"]'
    BLOGS_CONTENT_TITLE = (By.CSS_SELECTOR, '#content h2')

    PEOPLE_BUTTON = (By.CSS_SELECTOR, '#header a[href="/people/"]')
    PEOPLE_CONTENT_TITLE = (By.CSS_SELECTOR, '#content h2')

    PROGRAM_BUTTON = (By.CSS_SELECTOR, '#header a[href="/curriculum/program/"]')

    ALUMNI_BUTTON = (By.CSS_SELECTOR, '#header a[href="/alumni/"]')
    ALUMNI_CONTENT_TITLE = (By.CSS_SELECTOR, '#content h1')

    MAIN_PROGRAMS_TITLE = (By.CSS_SELECTOR, '#content a[href="/curriculum/program/main/"]')

    USER_DROPDOWN = (By.ID, 'dropdown-user-trigger')
    USER_MENU_SETTINGS_BUTTON = (By.CSS_SELECTOR, '#dropdown-user-menu li.item-settings')
    PROFILE_ABOUT = (By.ID, 'profile_about')

    SETTINGS_SUBMIT_BUTTON = (By.NAME, 'submit_profile_edit')
    SETTINGS_SUCCESS_CHANGE_MSG = (By.CSS_SELECTOR, '#content div.profile_settings_success-msg')
