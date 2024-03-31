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

class MainPageParkLocators(BaseParkPageLocators):
    BLOGS_BUTTON = (By.XPATH, '//*[@id="header"]//a[@href="/blog/"]')
    PEOPLE_BUTTON = (By.XPATH, '//*[@id="header"]//a[@href="/people/"]')
    PROGRAM_BUTTON = (By.XPATH, '//*[@id="header"]//a[@href="/curriculum/program/"]')
    ALUMNI_BUTTON = (By.XPATH, '//*[@id="header"]//a[@href="/alumni/"]')
    BLOGS_CONTENT_TITLE = (By.XPATH, '//*[@id="content"]//h2')
    PEOPLE_CONTENT_TITLE = (By.XPATH, '//*[@id="content"]//h2')
    ALUMNI_CONTENT_TITLE = (By.XPATH, '//*[@id="content"]//h1')
    MAIN_PROGRAMS_TITLE = (By.XPATH, '//*[@id="content"]//a[@href="/curriculum/program/main/"]')
    USER_DROPDOWN = (By.ID, 'dropdown-user-trigger')
    USER_MENU_SETTINGS_BUTTON = (By.XPATH, '//*[@id="dropdown-user-menu"]//li[@class="item-settings"]')
    PROFILE_ABOUT = (By.ID, 'profile_about')
    SETTINGS_SUBMIT_BUTTON = (By.NAME, 'submit_profile_edit')
    SETTINGS_SUCCESS_CHANGE_MSG = (By.XPATH, '//*[@id="content"]//div[@class="profile_settings_success-msg"]')
