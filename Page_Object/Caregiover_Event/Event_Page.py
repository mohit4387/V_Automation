__author__ = 'ashwinidesh'

from Page_Object.Base_Page import BasePage
from Page_Elements.TextField import DemoTxtField
from Page_Elements.Buttons import DemoButtonsField
from Page_Object.Caregiover_Event.NewEvent_Page import New_Event_Page
import time
import TestData
import Test_Context

class Events_Page(BasePage):
    def __init__(self):
        self.el_user = DemoTxtField(page=self, name="Username", locator="//div[@class='nav-right']/h4", locator_type="XPATH")
        self.el_add_an_event = DemoButtonsField(page=self, name="Add an Event", locator="new-task-button", locator_type="ID")
        self.el_events_tab = DemoButtonsField(page=self, name="Events", locator="nav-tasks", locator_type="ID")
        self.el_tasks_all_day = DemoTxtField(page=self, name="All Day", locator="//*[@id='tasks-home-container']//p[contains(text(),\'" + TestData.ALL_DAY + "\')]", locator_type="XPATH")
        self.el_tasks_title = DemoTxtField(page=self, name="Title", locator="//*[@id='tasks-home-container']//p[contains(text(),\'" + TestData.TITLE + "\')]", locator_type="XPATH")
        self.el_tasks_type = DemoTxtField(page=self, name="Event Type", locator="//*[@id='tasks-home-container']//p[contains(text(),\'" + TestData.TYPE + "\')]", locator_type="XPATH")
        self.driver = Test_Context.getOrCreateWebdriver()

    def verify_user_name(self, exp_user_name = "david caregiver"):
        act_user_name = self.el_user.get_value()
        if act_user_name != exp_user_name:
            return False
        else:
            return True

    def verify_event_button_status(self, exp_status = "SELECTED"):
        btn_status = self.el_events_tab.get_status()
        if btn_status != exp_status:
            return False
        else:
            return True

    def navigate_new_event_screen(self, exp_status = "SELECTED"):
        self.el_add_an_event.wait_for_page_element(30)
        time.sleep(15)
        self.el_add_an_event.click()
        new_events = New_Event_Page()
        new_events.el_title.wait_for_page_element(30)

    def verify_newly_created_event(self):
        self.el_tasks_title.wait_for_page_element(70)
        is_title_correct = self.el_tasks_title.check_exist()
        if is_title_correct:
            el_exp_title = self.el_tasks_title.find_element()
            event_details = el_exp_title.find_element_by_xpath('..')
            if event_details.text.find(TestData.TYPE) != -1:
                is_type_correct = True
            else:
                is_type_correct = False
            if event_details.text.find(TestData.ALL_DAY) != -1:
                is_all_day = True
            else:
                is_all_day = False
        else:
            is_title_correct = False
            return "Event Not Created."

        if is_type_correct and is_all_day and is_title_correct:
            return "Newly Added Event Details Are Correct"
        else:
            return "Newly Added Event Details Are Not Correct"

    def navigate(self):
        self.driver = Test_Context.getOrCreateWebdriver()
        self.driver.get(self.url)

