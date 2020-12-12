#!/usr/bin/env python
#coding=utf-8
#author:pushuai
from hamcrest import *

from server_contact.connect import Connect
class TestConnect():
    def setup_class(self):
        self.connect=Connect()
    #60104,手机号已经存在,60102,userID存在
    def test_create(self):
        user_id="pushuai"
        name="张一山"
        department=[1]
        re=self.connect.creat_connect(user_id,name,department=department)
        assert re.json()["errcode"] == 0
    def test_get_member(self):
        userid="1234"
        re=self.connect.get_member(userid)
        assert re.json()["errcode"] == 0
    def test_update(self):
        userid="1234"
        name="shuai"
        re=self.connect.update_member(userid)
        assert re.json()["errcode"] == 0
    #60111不存在的userid
    def test_delete(self):
        userid="1234"
        re=self.connect.delete_member(userid)
        assert_that(re.json()["errcode"],equal_to(0))
    def test_delete_and_detect(self):
        userid = "1234"
        re=self.connect.delete_and_detect(userid)
        assert re.json()["errcode"] == 0
    def test_creat_and_detect(self):
        userid="1234"
        name="shuai"
        department = [1]
        re=self.connect.create_and_detect(userid,name,department=department)
        assert re.json()["errcode"] == 0
    def test_update_and_detect(self):
        userid="12349"
        name="pu"
        re=self.connect.update_and_detect(userid,name)
        assert re.json()["errcode"] == 0


