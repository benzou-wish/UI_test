import time

import pytest


class TestSample:
    def test_1(self, get_driver):
        get_driver.get('https://qa.wishpost.cn')
        time.sleep(1)

    def test_2(self, get_driver):
        get_driver.get('https://qa.wishwms.cn')
        time.sleep(1)
