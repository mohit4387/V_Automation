import unittest
from nose.plugins.attrib import attr
from Page_Object.Caregiover_Event.Event_Page import Events_Page
from Page_Object.Login_Page import Login_Page
import TestData
import Test_Context


@attr("all_regression")
class CaregiverLogin_Valid(unittest.TestCase):
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
        and david caregiver user name should be display at top right hand side. Also it should land to home page
        """
        #Login with valid user to app

        # Check valid username is displayed or not
        events = Events_Page()
        b_username_verification = events.verify_user_name(exp_user_name=TestData.EXP_USER_NAME)
        if not b_username_verification:
            self.problems.append("username verification is failed")

        #Check landed to expected home url
        actual_home_url = self.driver.current_url
        print "Actual home URL......", actual_home_url

        if TestData.EXP_HOME_URL != actual_home_url:
            self.problems.append("Actual URL is not matched with expected home URL")

        self.assertFalse(self.problems)
        #if expected_home_url != main_page.is_homepage() :
            #self.problems.append(("URL are not matched"))

        #if expected_home_url != main_page.is_homepage() :
             #self.problems.append(("step 2 verification failed"))

        #self.assertFalse(self.problems)

    def tearDown(self):
        self.driver.close()

