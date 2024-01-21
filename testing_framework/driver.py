from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service

from testing_framework.singleton import singleton


@singleton
class Driver:
    driver = None

    def __init__(self):
        chrome_options = ChromeOptions()

        service = Service()
        self.driver = webdriver.Chrome(options=chrome_options, service=service)
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver
