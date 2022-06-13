import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os

os.environ['GH_TOKEN'] = "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"


class AutoInstallDriver:
    def __init__(self, driver):
        if driver == 'chrome':
            self.service = ChromeService(ChromeDriverManager(path=os.path.join(os.getcwd(), '../drivers')).install())
        elif driver == 'firefox':
            self.service = FirefoxService(GeckoDriverManager(path=os.path.join(os.getcwd(), '../drivers')).install())

    def get_service(self):
        self.service.start()
        return self.service
