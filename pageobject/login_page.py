from base.base_set import BaseSet
from selenium.webdriver.common.by import By


class LoginPage(BaseSet):
    username_loc = (By.NAME, "loginname")
    password_loc = (By.NAME, "password")
    submit_loc = (By.XPATH, "//*[@id = 'loginsubmit']").click()

    def login_input(self, username, password):
        self.send_Mykeys(LoginPage.username_loc, username)
        self.send_Mykeys(LoginPage.password_loc, password)
        self.click(LoginPage.submit_loc)
