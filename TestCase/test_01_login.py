import pytest
import logging
import allure

from PageLocators.login import Login
from Common.parse_yaml import PareseYaml
from Common.parse_xlsx import parse_xlsx
from Config.config import base_path

login_data_path = base_path + PareseYaml().parse_yaml("case.login")
login_data = parse_xlsx(login_data_path)


@pytest.mark.parametrize(('tenant', 'username', 'password', 'status'), login_data)
@allure.feature("用户登录")
class TestLogin:
    def setup(self):
        self.login = Login()

    def teardown(self):
        self.login.quit()

    @allure.story("用户登录")
    def test_01_login(self, tenant, username, password, status):
        self.login.login(tenant, username, password)
        if status == 1:  # 正常登录
            self.login.login_success_check()
            assert "退出登录" in self.login.driver.page_source
        elif status == 2: #租户错误
            self.login.login_tenant_check()
            assert "租户不存在" in self.login.driver.page_source
        elif status == 0:  # 用户名或者密码错误
            self.login.login_error_check()
            assert "登录失败，账号密码不正确" in self.login.driver.page_source
        else:
            logging.error(f"传入的status参数的值{status}不正确, 只能是0(用户名或者密码错误)、1(正常登录)、2(租户错误)")
            assert False
