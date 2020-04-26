# -*-coding:utf-8-*-
# @Time:2020/4/26   14:38
# @Author:ZKY
# @Email:475854688@qq.com
# @File:test_activity.py
# @Software:PyCharm
from appium import webdriver

desired_capabilities ={
    # 添加测试机的设备名，android此项可以随便写
    "deviceName":"127.0.0.1:62001",
    # 添加设备的Android版本
    "platformVersion":"5.1.1",
    # 添加测试平台Android/ios
    "platformName":"Android",
    # 添加被测的APP包名
    "appPackage":"com.mobile.videonews.li.video",
    # 添加测试APP的启动入口
    "appActivity":"com.mobile.videonews.li.video.act.StartAty",
    # 设置测试框架为uiautomator2
    "automationName":"uiautomator2",
    # 设置不需要每次都是第一次启动app
    "noRest":"True"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)

