import os
import time

from loguru import logger

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
        try:
            ele = self.driver.find_element(by, value)
            logger.info(f"模块:{doc}，获取元素成功，定位方法{by}，定位表达式{value}")
            return ele
        except:
            logger.error(f"模块:{doc}，获取元素失败，定位方法{by}，定位表达式{value}")
            self.save_screenshot(doc)
            raise


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    # ele: WebElement = driver.find_element(By.ID, "kw")
