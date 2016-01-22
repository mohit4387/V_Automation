__author__ = 'ashwinidesh'
from Page_Object.Base_Page import BasePage
from Page_Elements.TextField import DemoTxtField
from Page_Elements.Buttons import DemoButtonsField
from Page_Elements.Dropdown import DemoDropDownField
from Page_Elements.Checkbox import DemoCheckBoxField
from Page_Object.Caregiover_Event.SelectEventType_Page import Select_Event_Type

import Test_Context

class New_Event_Page(BasePage):

    def __init__(self):
        self.el_title = DemoTxtField(page=self, name="Title", locator="title", locator_type="ID")
        self.el_event_type = DemoDropDownField(page=self, name="Event Type", locator="new-task-type-input", locator_type="ID")
        self.el_all_day = DemoCheckBoxField(page=self, name="All Day", locator="allDay", locator_type="ID")
        self.el_location = DemoTxtField(page=self, name="Location", locator="location", locator_type="ID")
        self.el_notes = DemoTxtField(page=self, name="Notes", locator="task_notes", locator_type="ID")
        self.el_save_event = DemoButtonsField(page=self, name="Save Event", locator="save-new-task", locator_type="ID")
        self.el_start_time = DemoButtonsField(page=self, name="Start Time", locator="startTime", locator_type="ID")
        self.el_end_time = DemoButtonsField(page=self, name="End Time", locator="endTime", locator_type="ID")
        self.driver = Test_Context.getOrCreateWebdriver()

    def navigate(self):
        self.driver = Test_Context.getOrCreateWebdriver()
        self.driver.get(self.url)

    def create_new_event(self, title, type, all_day):
        self.el_title.set_text(title)
        self.el_event_type.click()
        popup_select_ev_type = Select_Event_Type()
        popup_select_ev_type.el_event_type_list.wait_for_page_element(30)
        popup_select_ev_type.el_event_type_list.select_from_list(type)
        if all_day == "All Day":
            self.el_all_day.click()
        self.el_location.set_text("Test Location")
        self.el_notes.set_text("Test Notes")
        self.el_save_event.click()

    def verify_start_end_time_all_day_event(self):
        if self.el_all_day.click():
            self.el_start_time.is_displayed()
            self.el_end_time.is_displayed()







