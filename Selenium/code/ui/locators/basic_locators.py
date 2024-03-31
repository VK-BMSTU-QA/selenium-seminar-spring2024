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


class LocatorsForParkPages:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.nav__button__menu>a')
    USER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Логин или почта"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
    ABOUT_INPUT = (By.ID, 'profile_about')
    ENG_NAME_INPUT = (By.ID, 'id_first_name_en')
    ENG_SURNAME_INPUT = (By.ID, 'id_last_name_en')
    SETTINGS_LINK = (By.XPATH, '//*[@id="wrapper"]/div[2]/a')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="content"]/div/div[1]/form/div[2]/button')
    MENU_ITEM_LINK = lambda item_name: (By.LINK_TEXT, item_name)