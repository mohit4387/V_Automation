__author__ = 'ashwinidesh'

from Page_Elements.Element import DemoElements
import Test_Context

class DemoTxtField(DemoElements):
    def __init__(self, page, name, locator, locator_type):
        # self.driver = test_context.getOrCreateWebdriver()
        self.page = page
        self.name = name
        self.locator = locator
        self.locator_type = locator_type

    def set_text(self,value):
        self.find_element().send_keys(value)

    def get_text(self):
        return self.find_element().text

    def get_value(self):
        return self.find_element().get_attribute('innerHTML')
