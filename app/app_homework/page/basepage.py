#!/usr/bin/env python
# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage():
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self,by,locator):
        self.driver.find_element(by,locator).click()
    def scroll(self,text):
        srocll=self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));').click()
        return srocll
    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result