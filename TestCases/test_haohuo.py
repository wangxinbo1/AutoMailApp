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
import time
from PageObject.haohuo_page import HaoHuoPage

@pytest.mark.usefixtures("init_driver_enter_haohuo")
class TestEnterHaoHuo():
    """
    发送email
    """
    def test_enter_haohuo(self, init_driver_enter_haohuo):
        time.sleep(8)
        # print(init_driver_enter_haohuo.contexts)
        # contexts = init_driver_enter_haohuo.contexts
        # # ['NATIVE_APP', 'WEBVIEW_com.netease.mail']
        # init_driver_enter_haohuo.switch_to.context(contexts[1])
        # time.sleep(5)
        # print(init_driver_enter_haohuo.current_context)
        # init_driver_enter_haohuo.find_element_by_xpath('//a[@class="btn J-sub"]').click()
        # time.sleep(5)


if __name__=="__main__":
    pytest.main(["-s", "-v", "--reruns","1","--reruns-delay","5","--resultlog","OutPut/log_file/log.txt","--html=OutPut/Report/report1.html", "--alluredir=OutPut/allure" ])