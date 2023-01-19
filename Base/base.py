import time

from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

png_path = ""


class BasePage:
    """
    对于一些原生api的一个封装
    """

    def __init__(self, driver):
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
            # self.driver.save_screenshot(file_path)
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
            # self.save_screenshot(doc)
            raise

    def get_all_elements(self, by, value, doc=''):
        """
        定位所有元素
        :param by:定位方法
        :param value:定位表达式
        :param doc:模块信息
        :return:返回定位的所有元素，如果失败则抛出异常
        """
        try:
            element = self.driver.find_elements(by, value)
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
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_element_located(locator))
            logger.info(f"模块：{doc}等待元素成功，定位方式{locator}")
            return element
        except:
            logger.error(f"模块：{doc}等待元素失败，定位方式{locator}")
            self.save_screenshot(doc)
            raise

    def wait_elements_all_presence(self, locator, timeout=10, doc=''):
        """
        等待获取元素
        :param locator:元素定位方式和定位表达式
        :param timeout:等待时间，默认10s
        :param doc:模块信息
        :return:返回定位元素，如果失败则抛出异常
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_all_elements_located(locator))
            logger.info(f"模块：{doc}等待元素成功，定位方式{locator}")
            return element
        except:
            logger.error(f"模块：{doc}等待元素失败，定位方式{locator}")
            self.save_screenshot(doc)
            raise

    def url_matches(self, url, timeout=10, doc="url路径匹配"):
        """
        等待路径匹配
        :param url:期望的url路径
        :param timeout:等待时间，默认10s
        :param doc:模块信息
        :return:无返回
        """
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_matches(url))
            logger.info(f"{doc}:页面路径:{self.driver.current_url}, 匹配路径:{url}")
        except:
            logger.error(f"{doc}:页面路径:{self.driver.current_url}, 匹配路径:{url}")
            self.save_screenshot(doc)
            raise

    def wait_element_visible(self, locator, timeout=10, doc=""):
        """
        等待元素显示
        :param locator:元素定位方式和定位表达式
        :param timeout:等待时间，默认10s
        :param doc:模块信息
        :return:返回定位元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
            logger.info(f"{doc}:元素定位成功,定位方式:{locator}")
            return ele
        except:
            self.save_screenshot(doc)
            logger.error("{}-元素不存在:{}".format(doc, locator))
            raise

    def click(self, ele, doc=""):
        """
        点击页面元素
        :param ele:页面中的元素
        :param doc:模块信息
        :return:无返回
        """
        try:
            logger.info(f"操作说明{doc},点击页面元素{ele.get_attribute('outerHTML')}")
            ele.click()
        except:
            logger.error(f"{doc}-点击操作{ele.get_attribute('outerHTML')}失败")
            self.save_screenshot(doc)
            raise

    def clear(self, ele, type=1, doc=""):
        """
        清除元素内容
        :param ele: 定位到的元素
        :param type: 1: 使用常规方式清除 0: 使用选中, 然后使用回退键
        :param doc:
        :return:
        """
        try:
            if type == 1:
                ele.clear()
            else:
                ele.send_keys(Keys.Ctrontrol, 'a')
                ele.send_keys(Keys.BACKSPACE)
            logger.info(f"模块:{doc},清楚元素内容成功, 清除方式{type},操作元素{ele.get_attribute('outerHTML')}")
        except:
            logger.error(f"{doc}-清楚元素内容失败!, 清除方式{type},操作元素{ele.get_attribute('outerHTML')}")
            self.save_screenshot(doc)
            raise

    def input_text(self, ele, value, doc=""):
        """
        给定位元素元素设置值
        :param ele:定位的元素
        :param value:设置对应的值
        :return:无返回
        """
        try:
            ele.send_keys(value)
            logger.info(f"功能模块:{doc}, 输入文本内容{value}, 定位的元素{ele.get_attribute('outerHTML')}")
        except:
            logger.error(f"{doc}-设置内容失败,  输入文本内容{value}, 定位的元素{ele.get_attribute('outerHTML')}")
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
    driver.get("https://www.baidu.com/")
    # ele: WebElement = driver.find_element(By.ID, "kw")
