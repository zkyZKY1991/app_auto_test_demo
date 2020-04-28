# -*-coding:utf-8-*-
# @Time:2020/4/28   16:02
# @Author:ZKY
# @Email:475854688@qq.com
# @File:configs.py
# @Software:PyCharm
import os


class Config:
    # 根目录地址
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Outputs的路径
    outputs_path = os.path.join(root_path, "Outputs")
    # log的路径
    log_path = os.path.join(outputs_path, "log")
    # report的路径
    report_path = os.path.join(outputs_path, "report")
    # screenshot的路径
    screenshot_path = os.path.join(outputs_path, "screenshot")
    # TestDatas的路径
    data_path = os.path.join(root_path, "TestDatas")


if __name__ == '__main__':
    a = Config()
    print(a.root_path)
    print(a.outputs_path)
    print(a.log_path)
    print(a.screenshot_path)
    print(a.report_path)
    print(a.data_path)
