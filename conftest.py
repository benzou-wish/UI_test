# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from base.base_page import BasePage
from comm_utils.config import ConfigReader


@pytest.fixture(scope='session')
def driver() -> WebDriver:
    """
    :return: WebDriver
    """
    basePage = BasePage(browser='chrome')
    driver = basePage.driver
    yield driver
    basePage.close()


def pytest_addoption(parser):
    """

    :param parser:
    :return: env name
    """
    parser.addoption('--env', action='store', default='qa', required=True,
                     help='请输入执行环境名, 如: qa')


@pytest.fixture(scope='session', autouse=True)
def config(request):
    """从配置对象中读取自定义参数的值"""
    env = request.config.getoption('--env')
    return ConfigReader(env)
