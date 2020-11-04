#!/usr/bin/env python
# coding=utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.podemo1.page.add_member import AddMemberPage
from web.podemo1.page.base_page import BasePage


class MainPage(BasePage):
    def goto_addmember(self):
        # 点击增加成员
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        sleep(2)
        return AddMemberPage(self.driver)

    def goto_contact(self):
        #         验证添加的联系人
        self.find(By.CSS_SELECTOR, '.frame_nav_item_title').click()
        self.find(By.CSS_SELECTOR, '.js_add_member').click()
        # self.find(By.CSS_SELECTOR,'#username').send_keys(username)
        # self.find(By.CSS_SELECTOR,'#memberAdd_acctid').send_keys(account)
        # self.find(By.CSS_SELECTOR,'#memberAdd_phone').send_keys(phone)
        # self.find(By.CSS_SELECTOR,'.qui_btn ww_btn js_btn_save').click()
        return AddMemberPage(self.driver)
