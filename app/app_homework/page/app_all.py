#!/usr/bin/env python
# coding=utf-8
from appium.webdriver import webdriver

from app.app_homework.page.basepage import BasePage
from app.app_homework.page.main import MainPage


class App(BasePage):
    #启动app
    def start(self):
        if self.driver==None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "pushuai"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # 保存缓存，比如登陆状态
            caps["noReset"] = "true"
            # 不停止应用直接运行测试用例，但要注意保证运行的测试用例在一个界面上，不在同一个界面上，首先返回到测试用例的界面
            caps["dontStopAppOnReset"] = "true"
            # 一些设备的安装，如果第一运行已经安装过了，第二次打开设置为true
            caps['skipDeviceInitialization'] = 'true'
            # service相关的安装，如果第一运行已经安装过了，第二次打开设置为true
            caps['skipServerInstallation'] = 'true'
            #
            # caps["settings[waitForIdleTimeout]"] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self
    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
    def stop(self):
        self.driver.quit()
    def goto_mainpage(self):
        return MainPage(self.driver)
