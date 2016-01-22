__author__ = 'ashwinidesh'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import Test_Context
from Test_Context import Test_Context

class DemoElements(object):
    def __init__(self, page, name, locator, locator_type):
        self.page = page
        self.name = name
        self.locator = locator
        self.locator_type = locator_type
        self.tc = Test_Context.get_test_context()

    def find_element(self):
        if self.locator_type == "XPATH":
            element = self.page.driver.find_element_by_xpath(self.locator)
        elif self.locator_type == "ID":
            element = self.page.driver.find_element_by_id(self.locator)
        elif self.locator_type == "CSS":
            element = self.page.driver.find_element_by_css(self.locator)
        return element

    def find_elements(self):
        if self.locator_type == "XPATH":
            elements = self.page.driver.find_elements_by_xpath(self.locator)
        elif self.locator_type == "ID":
            elements = self.page.driver.find_elements_by_id(self.locator)
        elif self.locator_type == "CSS":
            elements = self.page.driver.find_elements_by_css(self.locator)
        return elements

    def wait_for_page(self, locator):
        """
        Things to check:
            No errors
            No waiting spinners
            document.readyState == "complete"
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.page.driver.find_element(locator)))
            print "Page is ready!"
        except TimeoutException:
            print "Loading took too much time!"

    def wait_for_page_element(self, timeout):
        """
        Things to check:
            No errors
            No waiting spinners
            document.readyState == "complete"
        """
        locator = self.locator
        locator_type = self.locator_type
        try:
            if self.locator_type == "XPATH":
                WebDriverWait(self.page.driver, timeout).until(lambda driver : self.page.driver.find_element_by_xpath(locator))
            elif self.locator_type == "ID":
                WebDriverWait(self.page.driver, timeout).until(lambda driver : self.page.driver.find_element_by_id(locator))
            elif self.locator_type == "CSS":
                WebDriverWait(self.page.driver, timeout).until(lambda driver : self.page.driver.find_element_by_css_selector(locator))
            print "Page is ready!"
        except TimeoutException:
            print "Loading took too much time!"

    def check_exist(self):
        try:
            if self.locator_type == "XPATH":
                element = self.page.driver.find_element_by_xpath(self.locator)
            elif self.locator_type == "ID":
                element = self.page.driver.find_element_by_id(self.locator)
            elif self.locator_type == "CSS":
                element = self.page.driver.find_element_by_css(self.locator)
            return True
        except:
            return False

