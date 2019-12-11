# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：AutoMailApp -> handle_yaml
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/11/15 0015 19:53
@Desc   ：
=================================================='''
import yaml
from Common.dir_path import YAML_FILE_PATH


class HandleYaml():
    """
    处理并封装yaml文件
    """
    def __init__(self):
        with open(YAML_FILE_PATH, 'r') as fs:
            content = fs.read()
            self.ya = yaml.load(content,yaml.FullLoader)

    def get_value(self):
        return self.ya

desired_caps = HandleYaml().get_value()

if __name__=="__main__":
    print(desired_caps)