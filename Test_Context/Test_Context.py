__author__ = 'ashwinidesh'
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
_test_context = None

def get_test_context():
    """
    @rtype: TestContext
    """
    global _test_context
    if _test_context is None:
        _test_context = TestContext()
    return _test_context


class InvalidDriverException(Exception):
    """Thrown when we try to use a driver that isn't defined here"""
    pass


TRUE_VALUES = ['true', '1', 't', 'y', 'yes', True]


class TestContext(object):
    def __init__(self):
        print("TestContext being constructed")
        # A test case can set this if they'd like to skip opening a browser session, mostly for framework tests
        # Or any test that doesn't need to launch a browser:

        self.driver_to_use = os.getenv('BROWSER', 'chrome')
        self.platform = os.getenv('PLATFORM', 'windows 7')
        self.run_local = os.getenv('RUN_LOCAL', 'False').lower() in TRUE_VALUES
        self.ENTER_KEY = Keys.ENTER

        if self.run_local:
            self.command_executor = "C:/Selenium/WebDrivers/chromedriver.exe"

        # The session ID to set for this user:
        self.SESSION_ID = os.getenv('SESSIONID', None)

        self.POWER_USER = os.getenv('POWERUSER', "")
        self.POWER_PASS = os.getenv('POWERPASS', "")
        self.SERVERNAME = os.getenv('SERVERNAME', 'https://secure.alwaysreach.net')

        self.driver = None
        """:type: WebDriver"""

    def open_browser(self, name):

        if self.driver_to_use == "safari":
            self.driver = webdriver.Safari()
        elif self.driver_to_use == "firefox":
            self.driver = webdriver.Firefox()
        elif self.driver_to_use == "ie":
            self.driver = webdriver.Ie()
        elif self.driver_to_use == "chrome":
            self.driver == webdriver.Chrome("D:\SeniorLink_care\chromedriver.exe")
        else:
            self.driver = webdriver.Chrome(self.command_executor)
        self.driver.set_window_size(1300, 1500)