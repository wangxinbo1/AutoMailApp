# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：邮箱大师 -> home_page_object
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/13 0013 22:24
@Desc   ：
=================================================='''
from appium.webdriver.webdriver import WebDriver
from Common.base_page import BasePage
from appium import webdriver
from PageLocator.home_page_loc import HomePageLoc as home_loc
from PageLocator.sendmail_page_loc import SendMailPageLoc as sendmail_loc
from TestDatas import common_data as cd, send_email_data as sed
from PageLocator.haohuo_page_loc import HaoHuoPageLoc as hhpl
import time

class HaoHuoPage(BasePage):
    """
    home页面对象
    """
    # 业务
    def switch_jingxuan(self):
        contexts = self.get_context(hhpl.loc_title_text, "好货界面_网易员工精选")
        time.sleep(5)
        self.switch_context(contexts[1],"好货界面")

    def click_subscription_journal(self):
        self.click_element(hhpl.loc_subscribe_button , "好货界面_订阅按钮")

    # 校验


