from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')

    LOGIN_BUTTON_LOCATOR = (By.LINK_TEXT, 'Войти')
    SUBMIT_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[@id="popup-login-form-submit"]')

    SUBMIT_PROFILE_EDIT_LOCATOR = (By.NAME, 'submit_profile_edit')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass
