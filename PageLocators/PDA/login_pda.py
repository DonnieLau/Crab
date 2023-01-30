from appium import webdriver
import time

apptestDict = {
    # 连接的设备信息
    "unicodeKeyBoard": True
}
# 与appium session之间建立联系，括号内为appium服务地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', apptestDict)
