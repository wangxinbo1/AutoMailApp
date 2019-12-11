# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：邮箱大师 -> home_page_loc
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/13 0013 21:55
@Desc   ：
=================================================='''

from appium.webdriver.common.mobileby import MobileBy

class SendMailPageLoc():
    """
    Send Mail页面的元素
    """

    #发送邮件界面元素

    loc_send_mail_button = (MobileBy.ID, "com.netease.mail:id/send")  # 发送按钮

    loc_receiver_input_box = (MobileBy.ID, "com.netease.mail:id/mailcompose_address_input")  # 接收人按钮

    loc_subject_input_box = (MobileBy.ID, "com.netease.mail:id/mailcompose_subject_textedit")  # 主题输入框

    loc_body_input_box = (MobileBy.XPATH, "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText") # 正文处

    loc_add_attachment_button = (MobileBy.ID, "com.netease.mail:id/mailcompose_btn_add_attachment") # 上传附件按钮

    loc_attachment_file =(MobileBy.ID, "com.netease.mail:id/image_gallery_item_image") # 上传附件的文件（选择的第一个）

    loc_attachment_file_upload_complete_button = (MobileBy.ID, "com.netease.mail:id/attach_choose_large_vertical_menu_new_btn_done") # 选择附件后弹出的完成按钮


# loc_attachment_button = (MobileBy.ANDROID_UIAUTOMATOR,"new UiSelector().resourceId(com.netease.mail:id/mailcompose_btn_add_attachment") # 上传附件按钮