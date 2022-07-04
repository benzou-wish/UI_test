from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page.sample_login import Login


class HomePage(BasePage):
    _base_url = "https://qa.wishpost.cn"

    def __init__(self, browser=None, options=None):
        super().__init__(browser, options)
        self.driver.get(self._base_url)

    def login(self):
        self.find_element(By.CLASS_NAME, "wt-btn-secondary").click()
        # 创建Login实例后，可调用Login中的方法
        return Login(self.driver)
