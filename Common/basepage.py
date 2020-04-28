# -*-coding:utf-8-*-
# @Time:2020/4/24   10:17
# @Author:ZKY
# @Email:475854688@qq.com
# @File:basepage.py
# @Software:PyCharm
from appium import webdriver
from selenium.webdriver import remote


class AppBasePage:
    def __init__(self, driver:remote):
        self.driver = driver

    def get_screenshot(self):
        pass

    def my_logger(self):
        pass

    def get_element(self):
        pass

    def click_element(self):
        pass
