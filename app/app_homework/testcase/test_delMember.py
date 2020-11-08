#!/usr/bin/env python
# coding=utf-8
from app.app_homework.page.app_all import App

class TestDemo():
    def setup(self):
        self.main=App()
    def test_del(self,name):
        result=self.main.goto_mainpage().goto_contact().goto_manageMem().Modify_mem(name).del_mem().get_toast()
        assert "管理通讯录" in result
    def teardown(self):
        self.main.stop()