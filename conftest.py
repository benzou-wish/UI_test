# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from base.base_page import BasePage


@pytest.fixture(scope='session')
def get_driver() -> WebDriver:
    """
    :return: WebDriver
    """
    basePage = BasePage(browser='chrome')
    driver = basePage.driver
    yield driver
    basePage.close()
