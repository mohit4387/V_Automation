__author__ = 'ashwinidesh'
from Page_Elements.Element import DemoElements

class DemoCheckBoxField(DemoElements):
    def __init__(self, page, name, locator, locator_type):
        self.page = page
        self.name = name
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()
