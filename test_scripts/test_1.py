import time

from selenium.webdriver.common.by import By

from page.homepage import HomePage
import pytest
from selenium.webdriver import ActionChains


class TestSample:
    def test_1(self, get_driver):
        """

        :param get_driver: init a driver from conftest for entire test use
        :return:
        """
        browser = get_driver
        # create a homepage po
        homepage = HomePage(browser=browser)
        # click the button on dialog
        homepage.click(locator_type=By.CLASS_NAME, locator_value='btn-close-popup')
        # click login btn in homepage
        login_page = homepage.login()
