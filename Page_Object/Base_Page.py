__author__ = 'ashwinidesh'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Page_Elements.Element import DemoElements
import Test_Context

class BasePage(object):
    url = None

    def __init__(self, pages):
        self.driver = Test_Context.get_test_context()
        self.pages = pages
        """:type: Pages"""


    def click_by_xpath(self, obj_xpath):
        elem = self.driver.find_element_by_xpath(obj_xpath)
        elem.click()

    """def fill_form_by_id(self, form_element_id, value):
        return self.fill_form_by_css('#%s' % form_element_id, value)
        """
    def _get_page(self, page_class, wait_for_page):
        # Add to the list of page objects that were touched during the current test:
        # self.page_tags.append("'{}'".format(page_class.__name__))
        self._testMethodName = ""
        self._outcome = None
        self._testMethodDoc = 'No test'
        var_name = "_{}".format(page_class.__name__)
        # Instead, let's always return a fresh page object:
        # On second thought, let's wait to do this, I broke PD1000
        cached_page = getattr(self, var_name, None)
        # cached_page = None

        if cached_page is None:
            cached_page = page_class()
            # I can't change the __init__ on every page object now, but I can inject the test narrative here:
            # cached_page.narrative = self.narrative
            # Also inject the test name:
            self.test_name = "-".join([self.__class__.__name__, self._testMethodName[:80]])
            cached_page.test_name = self.test_name

            setattr(self, var_name, cached_page)

            # This gives page objects access to any other page object. This will help us make better helper functions:
            cached_page.pages = self.pages

        if wait_for_page:
            cached_page.wait_for_page()
        return cached_page

    def navigate(self):
        self.driver.get(self.url)
