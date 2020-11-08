#!/usr/bin/env python
# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from app.app_homework.page.basepage import BasePage

class Delete_mem(BasePage):
    def del_mem(self,name):
        #点击删除联系人
        self.find_click(MobileBy.XPATH,"//#[@text='删除成员']")
        from app.app_homework.page.mamagelist import ManageList
        return ManageList(self.driver)
