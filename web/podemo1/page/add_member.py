#!/usr/bin/env python
# coding=utf-8
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage
class AddMemberPage(BasePage):
    def __init__(self,driver:WebDriver):
        self.driver=driver
    def add_member(self,username,account,phonenum):
        # 添加联系
        # self.driver.find_element(By.ID,'')