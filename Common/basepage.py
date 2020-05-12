# -*-coding:utf-8-*-
# @Time:2020/4/24   10:17
# @Author:ZKY
# @Email:475854688@qq.com
# @File:basepage.py
# @Software:PyCharm
import datetime
import os
import time
from datetime import date

from appium import webdriver
from selenium.webdriver import remote
from Settings.configs import Config
from Common.logger_handler import LoggerHandler


class AppBasePage:
    def __init__(self, driver: remote):
        self.driver = driver

    def get_screenshot(self):
        pass

    def my_logger(self):
        time_now = datetime.datetime.time()
        filename = os.path.join(Config.log_path(), time_now)
        logger_handler = LoggerHandler("zky", "DEBUG", filename=filename)
        pass

    def get_element(self):
        pass

    def click_element(self):
        pass


if __name__ == '__main__':
    pass
