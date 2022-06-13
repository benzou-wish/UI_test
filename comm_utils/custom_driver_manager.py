import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from log import Log


class CustomDriverManager:
    def __init__(self):
        print(r'this is custom driver manager')

    def __del__(self):
        print(r'this is to delete driver manager')


class CustomDriver:
    def __init__(self):
        print('this is to start a new webdriver')

    def __del__(self):
        print(r'this is to stop a webdriver')

