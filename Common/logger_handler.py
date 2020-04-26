# -*-coding:utf-8-*-
# @Time:2020/4/24   10:16
# @Author:ZKY
# @Email:475854688@qq.com
# @File:logger_handler.py
# @Software:PyCharm
import logging

import os


class LoggerHandler(logging.Logger):
    """
    封装一个logger的处理类，继承logger，用于对日志的处理，包括日志的输出
    """
    def __init__(self, logger_name="root", logger_level="DEBUG", filename=None,
                 fmt="%(name)s-%(lineno)d-%(levelname)s-%(asctime)s-%(filename)s-日志信息：%(message)s"):
        # 设置父类里面的name，初始化一个日志加载器
        super().__init__(name=logger_name)
        # 设置日志加载器logger的等级
        self.setLevel(logger_level.upper())
        # 设置日志的输出格式
        fmt = logging.Formatter(fmt)
        if filename:
            # 创建一个文件日志处理器
            file_handler = logging.FileHandler(filename,encoding="utf-8")
            # 设置日志处理器的等级
            file_handler.setLevel(logger_level)
            # 设置日志的输出格式
            file_handler.setFormatter(fmt)
            # 日志加载器中添加日志处理器
            self.addHandler(file_handler)
        # 创建一个控制台日志输出
        control_handler = logging.StreamHandler()
        # 设置日志的等级
        control_handler.setLevel(logger_level)
        # 设置日志输出格式
        control_handler.setFormatter(fmt)
        # 加载器中添加控制台日志处理器
        self.addHandler(control_handler)


if __name__ == '__main__':
    log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(log_path, "Outputs/log/log_demo.txt")
    my_logger = LoggerHandler("zky","DEBUG",filename)
    my_logger.error("我是error日志")
