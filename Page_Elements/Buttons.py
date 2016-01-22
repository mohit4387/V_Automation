__author__ = 'ashwinidesh'
from Element import DemoElements

class DemoButtonsField(DemoElements):

    def click(self):
        self.find_element().click()

    def get_status(self):
        el = self.find_element()
        class_att = el.get_attribute("class")
        if class_att.find("selected") > 0:
            return "SELECTED"
        else:
            return "DESELECTED"

    def is_displayed(self):
        self.find_element().is_displayed()