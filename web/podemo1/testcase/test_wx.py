#!/usr/bin/env python
# coding=utf-8
from web.podemo1.page.main_page import MainPage


class TestWx:
    def setup(self):
        print("开始=----------------")
        self.main=MainPage()
    def test_addmember(self):
        username="abdmju"
        account="123506715"
        phone="18311208909"
        titlelist=self.main.goto_addmember().add_member(username,account,phone)
        assert username in titlelist
    # def test_addmember1(self):
    #     self.main.goto_contact()
