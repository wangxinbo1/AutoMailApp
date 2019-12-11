# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：AutoMailApp -> run_script
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/18 0018 22:08
@Desc   ：
=================================================='''
import pytest


# @pytest.mark.parametrize("name,age",[("age",20),("age",50)])
# def test_kaishi(name,age):
#     print("{}and{}".format(name,age))


if __name__=="__main__":
    pytest.main(["-s", "-v", "--reruns", "1", "--reruns-delay", "10", "--resultlog", "OutPut/log_file/log.txt", "--html=OutPut/Report/report1.html", "--alluredir=OutPut/allure" ])

