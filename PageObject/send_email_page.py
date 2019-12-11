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
import time

class SendMailPage(BasePage):
    """
    email页面
    """
    # 业务
    def send_mail_no_attachment(self, receiver, subject, body):
        self.input_mail_text(receiver, subject, body)
        self.click_element(sendmail_loc.loc_send_mail_button,"发送邮件界面_发送按钮")



    def input_mail_text(self, receiver, subject, body):
        self.input_text(sendmail_loc.loc_receiver_input_box,"发送邮件界面_接收人输入框", receiver)
        self.input_text(sendmail_loc.loc_subject_input_box,"发送邮件界面_主题输入框", subject)
        self.input_text(sendmail_loc.loc_body_input_box, "发送邮件界面_正文输入框", body)

    def upload_attachment(self):
        self.click_element(sendmail_loc.loc_add_attachment_button,"发送邮件邮件_上传附件按钮")
        self.click_element(sendmail_loc.loc_attachment_file,"发送邮件界面_上传附件弹窗_选择的第一个文件")
        self.click_element(sendmail_loc.loc_attachment_file_upload_complete_button, "发送邮件界面_上传附件弹窗_完成按钮")

    def send_mail_with_attachment(self, receiver, subject, body):
        self.upload_attachment()
        self.input_mail_text(receiver, subject, body)
        self.click_element(sendmail_loc.loc_send_mail_button,"发送邮件界面_发送按钮")

    # 校验
    def verify_send_mail_success(self):
        try:
            self.wait_page_contains_ele(home_loc.loc_more_button, "首页_More按钮")
            return True
        except:
            return False


