#!/usr/bin/env python
# coding=utf-8
"""
完成添加联系人功能，使用显式等待隐式等待结合的方式，练习课上的知识点。
"""
# 基类，最基本的方法，
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    base_url=""
    def  __init__(self,driver:WebDriver = None):
        if driver == None:
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
    # def wait_for_click(self,locator,time):
    #     element:WebElement =WebDriverWait(self.driver,time).until(expected_conditions.element_to_be_clickable(locator))
    #     return element




