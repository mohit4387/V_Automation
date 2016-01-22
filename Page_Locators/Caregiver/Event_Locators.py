__author__ = 'ashwinidesh'
from selenium.webdriver.common.by import By


class EventPageLocators(object):
    EVENTS_BUTTON = (By.ID, 'nav-tasks')
    TODAY_BUTTON = (By.ID, 'calendar-today')
    ADD_AN_EVENT_BUTTON = (By.CSS_SELECTOR, '#new-task-button')
    WEEK_BUTTON = (By.CSS_SELECTOR, '.calendar-week')
    MONTH_BUTTON = (By.CSS_SELECTOR, '.calendar-month')

