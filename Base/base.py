import os
import time

from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

png_path = ""


class BasePage:
    """
    对于一些原生api的一个封装
    """

    def __int__(self, driver):
        """
        初始化一个浏览器驱动对象
        :param driver:接收浏览器驱动
        :return:无返回
        """
        self.driver = driver

    def save_screenshot(self, doc=""):
        """
        页面截图
        :param doc: 需要提示的模块
        :return 无返回
        """
        file_path = png_path + f"{doc}_{time.strftime('%y%m%d%H%M%S', time.localtime())}.png"
        try:
            self.driver.save_screenshot(file_path)
            logger.info(f"截图成功, 图片路径:{file_path}")
        except:
            logger.error(f"{doc}-截图失败!")
            raise

    def get_element(self, by, value, doc=''):
        """
        定位元素
        :param by:定位方法
        :param value:定位表达式
        :param doc:模块信息
        :return:返回定位元素，如果失败则抛出异常
        """
        try:
            element = self.driver.find_element(by, value)
            logger.info(f"模块：{doc}，获取元素成功，定位方法{by}，定位表达式{value}")
            return element
        except:
            logger.error(f"模块：{doc}，获取元素失败，定位方法{by}，定位表达式{value}")
            self.save_screenshot(doc)
            raise

    def wait_element_presence(self, locator, timeout=10, doc=''):
        """
        等待获取元素
        :param locator:元素定位方式和定位表达式
        :param timeout:等待时间，默认10s
        :param doc:模块信息
        :return:返回定位元素，如果失败则抛出异常
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            logger.info(f"模块：{doc}等待元素成功，定位方式{locator}")
            return element
        except:
            logger.error(f"模块：{doc}等待元素失败，定位方式{locator}")
            self.save_screenshot(doc)
            raise

    def url_matches(self, url, timeout=10, doc="url路径匹配"):
        """
        等待路径匹配
        :param url: 期望的url路径
        :param timeout: 等待时间，默认10s
        :param doc: 模块信息
        :return: 无返回
        """
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_matches(url))
            logger.info(f"{doc}:页面路径:{self.driver.current_url}, 匹配路径:{url}")
        except:
            logger.error(f"{doc}:页面路径:{self.driver.current_url}, 匹配路径:{url}")
            self.save_screenshot(doc)
            raise

    def quit(self):
        """
        退出浏览器
        :return:无返回
        """
        self.driver.quit()
        logger.info(f"退出浏览器成功")

if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    # ele: WebElement = driver.find_element(By.ID, "kw")
