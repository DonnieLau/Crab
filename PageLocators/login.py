from selenium.webdriver.common.by import By
from Base.base import BasePage
from Common.common import open_browser
from Common.parse_yaml import PareseYaml

login_url = PareseYaml().parse_yaml("tms.url.login")


class Login(BasePage):
    loc_tenant = (By.XPATH, '//*[@id="login_container"]/form/div[1]/div/div/input')
    loc_username = (By.XPATH, '//*[@id="login_container"]/form/div[2]/div/div/input')
    loc_password = (By.XPATH, '//*[@id="login_container"]/form/div[3]/div/div/input')
    loc_submit_btn = (By.XPATH, '//*[@id="login_container"]/form/div[4]/div/button')

    loc_tenant_error = (By.XPATH, '//*[@id="login_container"]/form/div[1]/div/div[2]')
    loc_login_error = (By.XPATH, "//h2[text()='登录失败，账号密码不正确']")
    loc_login_success = "index"

    def __init__(self):
        driver = open_browser()
        driver.get(login_url)
        super().__init__(driver)

    # 定义登录方法
    def login(self, tenant, username, password):
        tenant_ele = self.get_element(*self.loc_tenant)
        self.clear(tenant_ele)
        self.input_text(tenant_ele, tenant)

        username_ele = self.get_element(*self.loc_username)
        self.clear(username_ele)
        self.input_text(username_ele, username)

        password_ele = self.get_element(*self.loc_password)
        self.clear(password_ele)
        self.input_text(password_ele, password)

        submit_ele = self.get_element(*self.loc_submit_btn)
        self.click(submit_ele)

        self.login_success_check()
        localstorage = self.get_storage('Admin-Auto-Token')
        data = PareseYaml().data
        PareseYaml().switch_yaml(data, 'Admin-Auto-Token', localstorage['Admin-Auto-Token'])

    def login_success_check(self):
        self.url_matches(self.loc_login_success)

    def login_tenant_check(self):
        self.wait_elements_all_presence(self.loc_tenant_error, doc="租户不存在")

    def login_error_check(self):
        self.wait_elements_all_presence(self.loc_login_error, doc="登录失败，账号密码不正确")


if __name__ == '__main__':
    a = Login()
    a.login('美迈科技', 'Donnie.Liu', '123456')
