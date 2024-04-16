from .base_page import BasePage
from ui.locators import techno_park_locators as tp_locators 

class SettingsPage(BasePage):
     url = 'https://park.vk.company/cabinet/settings/'
     locators = tp_locators.SettingsLocators

     def __init__(self, driver):
          driver.get(self.url)
          super().__init__(driver)

     def update_about_info(self, about_info):
          about_input = self.find(self.locators.ABOUT_INPUT)
          original_text = about_input.text
          about_input.clear()
          about_input.send_keys(about_info)
          self.click(self.locators.SUBMIT_EDIT, timeout=5)

          return original_text
