import TestData
from Page_Locators.Caregiver.MainPage_Locators import MainPageLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def caregiver_username(self, user):
        element = self.driver.find_element(*MainPageLocators.USERNAME_FEILD)
        element.send_keys(TestData.get_user(user)["username"])

    def caregiver_password(self, user):
        element = self.driver.find_element(*MainPageLocators.PASSWORD_FEILD)
        element.send_keys(TestData.get_user(user)["password"])

    def login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def caregiver_user_login(self, user):
        self.caregiver_username(user)
        self.caregiver_password(user)
        self.login_button()

    def is_homepage(self):
        homepage_url = self.driver.current_url
        print "Home Page URL:", homepage_url
        return homepage_url

    def is_login_error(self):
        login_error = self.driver.find_element(*MainPageLocators.FLASH_ALERT_MESSAGE).text
        print "Flash alert message:", login_error
        return login_error