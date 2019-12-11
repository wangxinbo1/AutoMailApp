# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：邮箱大师 -> home_page_loc
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/13 0013 21:55
@Desc   ：
=================================================='''

from appium.webdriver.common.mobileby import MobileBy


class HomePageLoc():
    """
    home页面的元素
    """
    # home界面元素
    loc_plus_button = (MobileBy.ID, "com.netease.mail:id/iv_mail_list_plus")  # 加号按钮
    loc_more_button = (MobileBy.ID, "com.netease.mail:id/iv_mail_list_folder")  # 左上角的more按钮
    # loc_haohuo_button = (MobileBy.ID, "com.netease.mail:id/tab_ads")  # 底部的好货按钮
    loc_haohuo_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.netease.mail:id/tab_item_text").text("好货")') # 元素中的必须用双引号
    loc_mail_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.netease.mail:id/tab_item_text").text("邮件")')
    loc_contacts_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.netease.mail:id/tab_item_text").text("通讯录")')
    loc_me_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.netease.mail:id/tab_item_text").text("我")')

    # 加号弹窗中的元素

    loc_write_mail = (MobileBy.ID, "com.netease.mail:id/tv_write_mail")