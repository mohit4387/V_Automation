__author__ = 'ashwinidesh'
from selenium import webdriver

DRIVER = None

def getOrCreateWebdriver():
    global DRIVER
    DRIVER = DRIVER or webdriver.Chrome("D:\SeniorLink_care\chromedriver")
    return DRIVER