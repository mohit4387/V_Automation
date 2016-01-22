__author__ = 'ashwinidesh'

import unittest
from nose.plugins.attrib import attr
from Page_Object.Login_Page import Login_Page
from Page_Object.Caregiover_Event.Event_Page import Events_Page

from Page_Object.Caregiover_Event.NewEvent_Page import New_Event_Page

import Test_Context
import TestData

@attr("all_regression")
class SignupTest(unittest.TestCase):
    problems = []

    def setUp(self):
        self.driver = Test_Context.getOrCreateWebdriver()
        login = Login_Page()
        login.login_to_app_valid()

    @attr("regression", "tc01")
    def test_tc01(self):

        """
        Provide username:davidcaregive601 and password: 123456 ->
        It should land to https://secure.alwaysreach.net/patients/caregiver_navigation
        and david caregiver user name should be display at top right hand side
        """

        # Check Events button -> By default Events button should be selected and clickable
        events = Events_Page()
        b_username_verification = events.verify_user_name(exp_user_name=TestData.EXP_USER_NAME)
        if not b_username_verification:
            self.problems.append("username verification is failed")
        b_event_button_status = events.verify_event_button_status(exp_status="SELECTED")
        if not b_event_button_status:
            self.problems.append("event button verification is failed")

        # Click on Add an Event button -> It should open add event screen -> Provide the details and save it ->
        # Home page should display created Event for the selected date

        events.navigate_new_event_screen()
        new_events = New_Event_Page()
        new_events.create_new_event(title=TestData.TITLE, type=TestData.TYPE, all_day=TestData.ALL_DAY)

        message = events.verify_newly_created_event()
        if message != "Newly Added Event Details Are Correct":
            self.problems.append("Actual result :- [ " + message +" ]")

        self.assertFalse(self.problems)


    def tearDown(self):
        self.driver.close()

