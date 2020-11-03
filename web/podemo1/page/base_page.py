#!/usr/bin/env python
# coding=utf-8
"""
完成添加联系人功能，使用显式等待隐式等待结合的方式，练习课上的知识点。
"""
# 基类，最基本的方法，
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    base_url=""
    def  __init__(self,driver:WebDriver):
        if driver==None:
            options=Options()
            options.debugger_address='127.0.0.1:9222'
            self.driver=webdriver.Chrome(options=options)
            # self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        else:
            self.driver=driver
    def find(self,by,seletor):
        return self.driver.find_element(by,seletor)
    def finds(self,by,seletor):
        return self.driver.find_elements(by,seletor)



