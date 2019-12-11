# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：AutoMailApp -> conftest
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/15 0015 19:48
@Desc   ：
=================================================='''
from Common.handle_yaml import desired_caps
from PageObject.send_email_page import SendMailPage
from appium import webdriver
import pytest
from PageObject.home_page import HomePage
from PageObject.haohuo_page import HaoHuoPage
import time
# @pytest.fixture()
# def init_driver():
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#     hp = SendMailPage(driver)
#     yield hp


def _base_driver(**kwargs):
    if kwargs:
        for key, value in kwargs.items():
            desired_caps[key]=value
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver


# 初始化driver,并进入发送email界面
@pytest.fixture(scope="class")
def init_driver_and_enter_mail():
    driver=_base_driver(noReset=True)
    HomePage(driver).enter_mail()
    hp = SendMailPage(driver)
    yield driver, hp
    driver.close_app()


@pytest.fixture(scope="class")
def init_driver_enter_haohuo():
    driver=_base_driver(noReset=True)
    HomePage(driver).enter_haohuo()
    time.sleep(5)
    hh = HaoHuoPage(driver)
    hh.switch_jingxuan()
    hh.click_subscription_journal()
    yield driver
    driver.close_app()


