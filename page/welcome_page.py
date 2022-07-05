from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page.login_page import LoginPage


class WelcomePage(BasePage):
    _url = "https://qa.wishpost.cn"

    class Loc:
        close_uni_inventory_dialog = (By.CLASS_NAME, 'btn-close-popup')
        login_btn = (By.CLASS_NAME, 'wt-btn-secondary')

    def __init__(self, browser=None, options=None):
        super().__init__(browser, options)
        self.open(self._url)

    def go_to_login(self):
        self.find_element(*self.Loc.login_btn).click()
        # 创建LoginPage实例后
        return LoginPage(self.driver)

    def hide_dialog(self):
        self.click(*self.Loc.close_uni_inventory_dialog)
