__author__ = 'ashwinidesh'

from Page_Elements.Element import DemoElements

class DemoDropDownField(DemoElements):
    def __init__(self, page, name, locator, locator_type):
        self.page = page
        self.name = name
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def select_from_list(self, item_to_select):
        all_items = self.find_elements()
        for i in range(0,len(all_items)):
            litem = all_items[i].text
            if litem == item_to_select:
                all_items[i].click()
                break






