#!/usr/bin/env python
# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from app.app_homework.page.basepage import BasePage
from app.app_homework.page.contactlist import ContactList
from app.app_homework.page.mamagelist import ManageList
class MainPage(BasePage):
    def goto_contact(self):
        """
        进入通讯录
        """
        self.find_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return ContactList(self.driver)