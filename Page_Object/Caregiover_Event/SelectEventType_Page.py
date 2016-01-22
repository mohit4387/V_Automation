__author__ = 'ashwinidesh'

from Page_Object.Base_Page import BasePage
from Page_Elements.Dropdown import DemoDropDownField
from Page_Elements.Buttons import DemoButtonsField

import Test_Context

class Select_Event_Type(BasePage):


    def __init__(self):
        self.el_event_type_list = DemoDropDownField(page=self, name="Select Event Type", locator="//*[@id='new-task-type-modal']//ul[@class='list--options']/li", locator_type="XPATH")
        self.driver = Test_Context.getOrCreateWebdriver()

