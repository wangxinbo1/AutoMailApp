# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：AutoMailApp -> login_page_loc
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/13 0013 20:08
@Desc   ：
=================================================='''

from appium import webdriver
from PageObject.home_page import HomePage
import pytest
from PageLocator.home_page_loc import HomePageLoc as home_loc
from PageLocator.sendmail_page_loc import SendMailPageLoc as sendmail_loc
from TestDatas import common_data as cd, send_email_data as sed

# desired_caps = {}
# desired_caps["platformName"]="Android"
# desired_caps["platformVersion"]="5.1"
# desired_caps["deviceName"]="Emulator"
# desired_caps["automationName"]="UiAutomator2"
# desired_caps["appPackage"]="com.netease.mail"
# desired_caps["appActivity"]="com.netease.mobimail.activity.LaunchActivity"
# desired_caps["noReset"]=True


random_number = cd.get_random_number(6)

@pytest.mark.usefixtures("init_driver_and_enter_mail")
class TestSendMail():
    """
    发送email
    """
    def test_send_mail(self, init_driver_and_enter_mail):
        init_driver_and_enter_mail[1].send_mail_with_attachment(cd.test_account,sed.email_subject+random_number,sed.email_body+random_number)
        assert init_driver_and_enter_mail[1].verify_send_mail_success()



if __name__=="__main__":
    pytest.main("-s","-v")