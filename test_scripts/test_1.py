import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from comm_utils.config import ConfigReader
from page.login_page import LoginPage
from page.welcome_page import WelcomePage
import pytest
from selenium.webdriver import ActionChains


class TestWelcome:
    def test_go_login(self, driver, config):
        """

        :param driver: init a driver from conftest for entire test use
        :return:
        """
        # open a browser
        driver.get(config.base_url)

        # go to welcome page
        welcomePage = WelcomePage(driver)

        # remove the uni inventory dialog if exists
        try:
            welcomePage.close_uni_dialog()
        except (NoSuchElementException, TimeoutException):
            pass

        # click login btn in homepage
        loginPage = welcomePage.go_to_login()
        time.sleep(1)
        loginPage.input_username()

    def test_go_signup(self):
        pass
