from appium import webdriver
import time

apptestDict = {
    # 连接的设备信息
    "platformName": "Android",
    'platformVersion': '7.1.2',
    "deviceName": "127.0.0.1:62001",
    "appPackage": "plus.H56BFB035",  # app包名
    "appActivity": "io.dcloud.PandoraEntry",  # app的初始化类
    "unicodeKeyBoard": True
}
# 与appium session之间建立联系，括号内为appium服务地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', apptestDict)
