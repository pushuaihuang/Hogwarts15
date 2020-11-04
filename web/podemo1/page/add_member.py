#!/usr/bin/env python
# coding=utf-8
from time import sleep

from appium.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo1.page.base_page import BasePage
class AddMemberPage(BasePage):
    def add_member(self,username,account,phonenum):
        # 添加联系
        # locator = (By.CSS_SELECTOR,"#username")

        # def wait_for_next(x:WebDriver):
        #     try:
        #         return x.find_element(*locator)
        #     except:
        #         return "123"
        # WebDriverWait(self.driver,10).until(wait_for_next)
        # self.find(locator).send_keys(username)
        self.find(By.CSS_SELECTOR,"#username").send_keys(username)
        self.find(By.CSS_SELECTOR,"#memberAdd_acctid").send_keys(account)
        self.find(By.CSS_SELECTOR,"#memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        # element:WebElement=WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # element.click()
        # element=self.wait_for_click(locator,10)
        # element.click()
        # 获取添加后的联系人列表从而判断是否添加成功
        total_list=[]
        while True:
            contactlist=self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
            titlelist=[elemen.get_attribute('title') for elemen in contactlist]
            if username in titlelist:
                return True
            total_list=total_list+titlelist
            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
        return titlelist



