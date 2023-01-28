from selenium.webdriver.common.by import By
from Base.base import BasePage
from Common.common import open_browser
from Common.parse_yaml import PareseYaml

main_url = PareseYaml().parse_yaml("tms.url.main")


class Tms_dic_manage(BasePage):
    def __init__(self):
        driver = open_browser()
        driver.get(main_url)

        localstorage = PareseYaml().parse_yaml("tms.storage")
        (key, value), = localstorage.items()
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script('localStorage.setItem(arguments[0], arguments[1]);', key, value)

        driver.refresh()
        driver.get(main_url)
        super().__init__(driver)


if __name__ == '__main__':
    a = Tms_dic_manage()
