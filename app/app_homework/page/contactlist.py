#!/usr/bin/env python
# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from app.app_homework.page.basepage import BasePage
from app.app_homework.page.mamagelist import ManageList
class ContactList(BasePage):
    def goto_manageMem(self):
        #进入通讯管理列表
        self.find_click(MobileBy.ID,"com.tencent.wework:id/hvi")
        return ManageList(self.driver)