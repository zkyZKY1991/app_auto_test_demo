# -*-coding:utf-8-*-
# @Time:2020/4/27   13:40
# @Author:ZKY
# @Email:475854688@qq.com
# @File:yaml_handler.py
# @Software:PyCharm
import os

import yaml

class YamlHandler:
    def __init__(self,filename):
        self.filename = filename

    def get_data(self):
        with open(self.filename, mode='r',encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def set_data(self, data):
        with open(self.filename, mode="w", encoding="utf-8") as f:
            yaml.dump(data, f, Allow_unicode=True)


if __name__ == '__main__':
    yaml_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(yaml_path, "Settings/config.yaml")
    my_yaml = YamlHandler(filename)
    d = my_yaml.get_data()
    print(d)