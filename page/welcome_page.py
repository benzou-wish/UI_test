from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page.login_page import LoginPage


class WelcomePage(BasePage):
    _url = "https://qa.wishpost.cn"

    class Loc:
        close_uni_inventory_dialog = (By.CLASS_NAME, 'btn-close-popup')
        login_btn = (By.CLASS_NAME, 'wt-btn-secondary')

    def go_to_login(self):
        self.find_element(*self.Loc.login_btn).click()
        # 创建LoginPage实例后
        return LoginPage(self.driver)

    def close_uni_dialog(self):
        self.click(*self.Loc.close_uni_inventory_dialog)
