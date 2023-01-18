from selenium.webdriver.common.by import By
from Base.base import BasePage
from Common.common import open_browser
from Common.parse_yaml import parse_yaml

login_url = parse_yaml("tms.url.login")


class Login(BasePage):
    # 定义元素位置
    loc_tenant = (By.XPATH, '//*[@id="login_container"]/form/div[1]/div/div[1]/input')
    loc_username = (By.XPATH, '//*[@id="login_container"]/form/div[2]/div/div[1]/input')
    loc_password = (By.XPATH, '//*[@id="login_container"]/form/div[3]/div/div[1]/input')
    loc_submit_btn = (By.XPATH, '//*[@id="login_container"]/form/div[4]/div/button')

    loc_login_error = (By.XPATH, "//span[text()='用户名或者密码错误']")
    loc_login_success = "main"

    def __init__(self):
        driver = open_browser()
        driver.get(login_url)
        super().__init__(driver)

    # 定义业务方法
    def login(self, username, password):
        username_ele = self.get_element(*self.loc_username)
        self.clear(username_ele)
        self.input_text(username_ele, username)
        password_ele = self.get_element(*self.loc_password)
        self.clear(password_ele)
        self.input_text(password_ele, password)
        submit_ele = self.get_element(*self.loc_submit_btn)
        self.click(submit_ele)

    def login_success_check(self):
        self.url_matches(self.loc_login_success)

    def login_error_check(self):
        self.wait_ele_all_presence(self.loc_login_error, doc="用户登录错误验证")
