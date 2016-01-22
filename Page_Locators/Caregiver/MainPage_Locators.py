from selenium.webdriver.common.by import By


class MainPageLocators(object):
    USERNAME_FEILD = (By.ID, 'login_field')
    PASSWORD_FEILD = (By.ID, 'password_field')
    LOGIN_BUTTON = (By.ID, 'sign-in-button')
    FLASH_ALERT_MESSAGE = (By.CSS_SELECTOR, '.icon-block__text--block')
