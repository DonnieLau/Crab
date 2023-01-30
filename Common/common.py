import time
from selenium import webdriver
from loguru import logger
from Common.parse_yaml import PareseYaml

# 读取配置文件, 并且配置对应的日志存放路径
log_path = PareseYaml().parse_yaml("path.log")
filename_info = log_path + "tms_info_" + time.strftime("%Y%m%d", time.localtime()) + ".log"
filename_error = log_path + "tms_error_" + time.strftime("%Y%m%d", time.localtime()) + ".log"
logger.add(filename_info, level="INFO", encoding="utf-8", rotation="00:00")
logger.add(filename_error, level="ERROR", encoding="utf-8", rotation="00:00")


# 打开浏览器
def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver



