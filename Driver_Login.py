__author__ = 'mohitp'

from selenium import webdriver
import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_Locators.Caregiver.MainPage_Locators import MainPageLocators
from Page_Locators.Caregiver.Event_Locators import EventPageLocators

class Driver_Initialisation():

    def initialise(self):
        browser = TestData.get_value("browser")

        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()

        self.driver.get(TestData.get_value("url"))
        self.driver.maximize_window()


    def login(self, user):
        element = self.driver.find_element(*MainPageLocators.USERNAME_FEILD)
        element.send_keys(TestData.get_user(user)["username"])
        element = self.driver.find_element(*MainPageLocators.PASSWORD_FEILD)
        element.send_keys(TestData.get_user(user)["password"])
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#new-task-button')))
        print "Login successful. Homepage loaded"

#dr = Driver_Initialisation()
#dr.initialise()
#dr.login("valid_user")