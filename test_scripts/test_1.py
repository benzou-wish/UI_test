import time

from selenium.webdriver.common.by import By

from page.login_page import LoginPage
from page.welcome_page import WelcomePage
import pytest
from selenium.webdriver import ActionChains


class TestWelcome:
    def test_go_login(self, get_driver):
        """

        :param get_driver: init a driver from conftest for entire test use
        :return:
        """
        # create a homepage po
        welcomePage = WelcomePage(get_driver)
        # remove the dialog
        welcomePage.hide_dialog()
        # click login btn in homepage
        loginPage = welcomePage.go_to_login()
        time.sleep(1)
        loginPage.input_username()

    def test_go_signup(self):
        pass
