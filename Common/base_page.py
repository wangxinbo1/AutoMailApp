from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Common.handle_log import logger
from Common.dir_path import SCREENSHOT_DIR_PATH

class BasePage():
    """
    基本页面对象
    """

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def wait_ele_visible(self, loc, doc_img, timeout=30, frequency=0.5):
        logger.info("等待'{}'元素值为'{}'可见".format(doc_img, loc))
        start_time = time.time()
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
        except:
            logger.error("查找'{}'元素出现失败".format(doc_img))
            raise
        else:
            end_time = time.time()
            logger.info("等待'{}'元素出现成功，等待时间为{}s".format(doc_img, end_time-start_time))


    def wait_page_contains_ele(self, loc, doc_img, timeout=30, frequency=0.5):
        logger.info("等待'{}'元素值为'{}'出现在页面".format(doc_img, loc))
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
            logger.info("等待{}元素出现成功".format(doc_img))
        except:
            logger.error("等待{}元素出现失败".format(doc_img))
            raise

    def find_element(self, loc, doc_img):
        logger.info("查找'{}'元素值为'{}'".format(doc_img, loc))
        self.wait_ele_visible(loc,doc_img)
        try:
            ele = self.driver.find_element(*loc)
            logger.info("找到'{}'元素".format(doc_img))
            return ele
        except:
            logger.error("未找到'{}'元素".format(doc_img))
            raise

    def input_text(self, loc, doc_img, text_value):
        logger.info("在{}的{}元素处输入{}".format(doc_img, loc, text_value))
        try:
            self.find_element(loc, doc_img).send_keys(text_value)
            logger.info("成功输入文本值")
        except:
            self.save_error_screenshot(doc_img)
            logger.error("输入文本值失败")
            raise

    def click_element(self, loc, doc_img):
        logger.info("在{}点击{}元素".format(doc_img, loc))
        try:
            self.find_element(loc, doc_img).click()
            logger.info("点击'{}'元素成功".format(doc_img))
        except:
            logger.error("点击'{}'元素失败".format(doc_img))
            self.save_error_screenshot(doc_img)
            raise

    def get_context(self, native_loc, doc_img):
        self.wait_page_contains_ele(native_loc, doc_img)
        logger.info("在'{}'页面获取到所有的context".format(doc_img))
        try:
            time.sleep(5)
            contexts = self.driver.contexts
            time.sleep(5)
            logger.info("获取所有的contexts '{}'成功".format(contexts))
            return contexts
        except:
            logger.error("获取所有的contexts失败")
            raise

    def switch_context(self, context, doc_img):
        logger.info("在{}切换到{}页面".format(doc_img, context))
        try:
            time.sleep(5)
            self.driver.switch_to.context(context)
            logger.info("切换到'{}' webview成功".format(context))
        except:
            logger.error("切换到'{}' webview失败".format(context))
            self.save_error_screenshot(doc_img)
            raise

    def click_element(self, loc, doc_img):
        logger.info("在{}点击{}元素".format(doc_img, loc))
        try:
            self.find_element(loc, doc_img).click()
            logger.info("点击'{}'元素成功".format(doc_img))
        except:
            logger.error("点击'{}'元素失败".format(doc_img))
            self.save_error_screenshot(doc_img)
            raise

    def save_error_screenshot(self, doc_img):
        file_name = doc_img + str(time.strftime("%Y%m%d%H%M%S",time.localtime())) + ".png"
        file_path = SCREENSHOT_DIR_PATH + '/' + file_name
        self.driver.save_screenshot(file_path)

if __name__=="__main__":
    pass