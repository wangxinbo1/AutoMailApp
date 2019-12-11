# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：AutoMailApp -> send_email_data
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/15 0015 22:20
@Desc   ：
=================================================='''
import random
test_account = "2421327542@qq.com"

def get_random_number(n):
    return ''.join(random.sample("0123456789", n))

if __name__=="__main__":
    a= get_random_number(6)
    print(a,type(a))