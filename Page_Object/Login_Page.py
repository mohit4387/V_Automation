__author__ = 'ashwinidesh'


from Page_Object.Base_Page import BasePage

from Page_Elements.TextField import DemoTxtField

from Page_Elements.Buttons import DemoButtonsField
from Page_Object.Caregiover_Event.Event_Page import Events_Page

from Page_Elements.Element import DemoElements

import Test_Context
import TestData

class Login_Page(BasePage):

    def __init__(self):
        self.url = "https://secure.alwaysreach.net"
        self.el_username = DemoTxtField(page=self, name="Username or Email", locator="login_field", locator_type="ID")
        self.el_password = DemoTxtField(page=self, name="Password", locator="password_field", locator_type="ID")
        self.el_login = DemoButtonsField(page=self, name="Log In", locator="sign-in-button", locator_type="ID")
        self.driver = Test_Context.getOrCreateWebdriver()

    def login_to_app_valid(self):
        self.driver.get(self.url)
        #self.driver.get(TestData.URL)
        self.driver.maximize_window()
        self.el_username.set_text(TestData.VALID_USERNAME)
        self.el_password.set_text(TestData.VALID_PASSWORD)
        self.el_login.click()
        events = Events_Page()
        events.el_user.wait_for_page_element(30)

    def login_to_app_invalid(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.el_username.set_text(TestData.INVALID_USERNAME)
        self.el_password.set_text(TestData.INVALID_PASSWORD)
        self.el_login.click()
        self.el_login.wait_for_page_element(30)

