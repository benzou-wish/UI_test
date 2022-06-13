# coding=utf-8
import allure
import pytest
from selenium import webdriver
from comm_utils.custom_driver_manager import AutoInstallDriver


@pytest.fixture(scope='function')
def get_driver(get_service) -> webdriver:
    """
    :return: webdriver
    """
    driver = webdriver.Remote(command_executor=get_service.service_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def get_service():
    service = AutoInstallDriver('chrome').get_service()
    yield service
    service.stop()


