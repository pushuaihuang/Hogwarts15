#!/usr/bin/env python
# coding=utf-8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "pushuai"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        #
        # caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    # def test_login(self):
    #
    #     el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
    #     el1.click()
    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        # app端点击滑动activity，android的使用方法
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # setting
        self.driver.update_settings({"waitForIdleTimeout": 4})
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text, '次外出')]").click()
        # 显示等待
        WebDriverWait(self.driver,10).until(lambda x : "外出打卡成功" in x.page_source)
    # def test_daka_work(self):
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
    #     self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
    #                              'new UiScrollable(new UiSelector()\
    #                              .scrollable(true).instance(0))\
    #                              .scrollIntoView(new UiSelector()\
    #                              .text("打卡").instance(0));').click()
    #     # setting
    #     self.driver.update_settings({"waitForIdleTimeout": 2})
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
    def setdown(self):
        self.driver.quit()
