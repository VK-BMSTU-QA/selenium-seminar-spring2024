from selenium.webdriver.common.by import By
from enum import Enum

class HeaderSections(Enum):
    BLOGS = 'blogs'
    PEOPLE = 'people'
    PROGRAMS = 'programs'
    GRADUATES = 'graduates'


class HeaderLocators():
    BLOG_BTN_LOCATOR = (By.CSS_SELECTOR, '.technopark__menu__item_3')
    PEOPLE_BTN_LOCATOR = (By.CSS_SELECTOR, '.technopark__menu__item_4')
    PROGRAMS_BTN_LOCATOR = (By.CSS_SELECTOR, '.technopark__menu__item_41')
    GRADUATES_BTN_LOCATOR = (By.CSS_SELECTOR, '.technopark__menu__item_42')
    ACTIVE_SECTION_LOCATOR = (By.CSS_SELECTOR, '.active')
    DROPDOWN_BTN_LOCATOR = (By.CSS_SELECTOR, '#dropdown-user-trigger')
    SETTINGS_BTN_LOCATOR = (By.CSS_SELECTOR, '.item-settings')

    def get_locator_by_section(self, section):
        if section == HeaderSections.BLOGS:
            return self.BLOG_BTN_LOCATOR
        elif section == HeaderSections.PEOPLE:
            return self.PEOPLE_BTN_LOCATOR
        elif section == HeaderSections.PROGRAMS:
            return self.PROGRAMS_BTN_LOCATOR
        elif section == HeaderSections.GRADUATES:
            return self.GRADUATES_BTN_LOCATOR
        else:
            raise TypeError('unknown section')
    