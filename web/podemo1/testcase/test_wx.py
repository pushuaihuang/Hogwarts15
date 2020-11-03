#!/usr/bin/env python
# coding=utf-8
from web.podemo1.page.main_page import MainPage


class TestWx:
    def setup(self):
        self.mian=MainPage()
    def test_addmember(self):
        username=''
        account=''
        addmember=self.mian.goto_addmember()
