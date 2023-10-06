import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    
class TestSearchLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):

#main commands
    def enter_text_into_field(self, locator, word, description_loc=None):
        if description_loc:
            element_name = description_loc
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True
    
    def click_button(self, locator, description_loc=None):
        if description_loc:
            element_name = description_loc
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True
  
    #enter text
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description_loc="login field")
        logging.info(f"We entered login in the field {TestSearchLocators.ids['LOCATOR_LOGIN_FIELD']}")
    
    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description_loc="password field")
        logging.info(f"We entered password in the field {TestSearchLocators.ids['LOCATOR_PASS_FIELD']}")
      
    #click
    def click_login_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description_loc="login button")
        logging.info(f"We clicked on the login button {TestSearchLocators.ids['LOCATOR_LOGIN_BTN']}")

    def click_about_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BTN_ABOUT"], description_loc="about button")
        logging.info(f"We clicked on the button ABOUT {TestSearchLocators.ids['LOCATOR_BTN_ABOUT']}")

    #get text
    def get_header_size(self):
        element_size = self.get_element_property(TestSearchLocators.ids["LOCATOR_HEADER_ABOUT"], "font-size")
        logging.info(f"We find size {element_size} of header {TestSearchLocators.ids['LOCATOR_HEADER_ABOUT']}")
        return element_size



