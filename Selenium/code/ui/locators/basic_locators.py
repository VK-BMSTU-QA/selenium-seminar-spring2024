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


class TechnoParkLocators:
    DIV_LOGIN_LOCATOR = (By.CLASS_NAME, 'nav__button__menu')
    LOGIN_INPUT_LOCATOR = (By.NAME, 'login')
    PASSWORD_INPUT_LOCATOR = (By.NAME, 'password')
    INPUT_BUTTON_IN_LOGIN_LOCATOR = (By.ID, 'popup-login-form-submit')