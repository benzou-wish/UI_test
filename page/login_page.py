from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    _url = "https://qa.wishpost.cn/welcome/#/login"

    class Loc:
        username_input = (By.ID, 'input-74')

    def input_username(self):
        self.input(*self.Loc.username_input, input_value='test_user')

    def login(self):
        pass

    def sign_up(self):
        pass

    def forget_password(self):
        pass
