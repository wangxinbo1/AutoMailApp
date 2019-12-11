# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：邮箱大师 -> home_page_loc
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/13 0013 21:55
@Desc   ：
=================================================='''

from appium.webdriver.common.mobileby import MobileBy


class HaoHuoPageLoc():
    """
    好货页面的元素
    """
    # 好货界面的webview界面元素
    loc_subscribe_button = (MobileBy.XPATH, "//a[@class='btn J-sub']")  # 订阅按钮
    loc_title_text = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.netease.mail:id/tv_title")') # 网易员工精选标题