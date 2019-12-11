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

class HomePage(BasePage):
    """
    home页面对象
    """
    # 业务
    def enter_mail(self):
        self.click_element(home_loc.loc_plus_button, "首页_点击加号按钮")
        self.click_element(home_loc.loc_write_mail, "首页_写邮件按钮")

    # 校验
    def verify_enter_send_mail_page(self):
        try:
            self.wait_page_contains_ele(sendmail_loc.loc_send_mail_button, "发送邮件界面_发送按钮")
            return True
        except:
            return False

    def enter_haohuo(self):
        self.click_element(home_loc.loc_haohuo_button,"首页底部_好货按钮")

    def click_mail(self):
        self.click_element(home_loc.loc_mail_button,"首页底部_邮件按钮")

    def enter_contacts(self):
        self.click_element(home_loc.loc_contacts_button, "首页底部_通讯录按钮")

    def enter_personal(self):
        self.click_element(home_loc.loc_me_button, "首页底部_我按钮")