
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page.sample_login import Login


class HomePage(BasePage):
    _base_url = "https://www.google.com"

    def login(self):
        self.driver.get(self._base_url)
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()
        # 创建Register实例后，可调用Register中的方法
        return Login(self.driver)

