#!/usr/bin/env python
# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from app.app_homework.page.basepage import BasePage


class ManageList(BasePage):
    def Modify_mem(self,name):
        # 点击要修改的联系人
        self.find_click(MobileBy.XPATH, f"//*[@text='{name}']")
        from app.app_homework.page.delete_member import Delete_mem
        return Delete_mem(self.driver)
    def get_toast(self):
        result=self.get_toast()
        return result