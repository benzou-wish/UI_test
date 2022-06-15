import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

os.environ['GH_TOKEN'] = "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"


class BasePage:
    """
    define base class for all page object
    """
    def __init__(self, browser=None, options=None):
        if browser and isinstance(browser, WebDriver):
            self._driver = browser
        elif browser and isinstance(browser, str):
            self._service = None
            self.InitDriver(browser, options)

    def InitDriver(self, browser, options):
        if browser == 'chrome':
            self._service = ChromeService(
                ChromeDriverManager(path=os.path.join(os.getcwd(), '../drivers')).install())
            option = webdriver.ChromeOptions()
            if options:
                option.add_argument(options)
            self._driver = webdriver.Chrome(service=self._service, options=option)
            self._driver.implicitly_wait(3)

        elif browser == 'firefox':
            self._service = FirefoxService(
                GeckoDriverManager(path=os.path.join(os.getcwd(), '../drivers')).install())
            self._service.start()
            option = webdriver.FirefoxOptions()
            if options:
                option.add_argument(options)
            self._driver = webdriver.Firefox(service=self._service, options=option)
            self._driver.implicitly_wait(3)

        else:
            raise Exception('only support chrome and firefox for now')

    def close(self):
        self._driver.quit()
        self._service.stop()

    @property
    def driver(self):
        return self._driver

    def get_source(self):
        """
        get page source code
        :return:
        """
        return self._driver.page_source

    def get_url(self):
        """
        get page url
        :return:
        """
        return self._driver.current_url

    def get_window_handler(self):
        """
        get page window handler
        :return:
        """
        return self._driver.current_window_handle