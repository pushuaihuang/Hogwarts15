#!/usr/bin/env python
#coding=utf-8
#author:pushuai
import pytest
from serve.tag import Tag
class TestTag():
    def setup_class(self):
        self.tag=Tag()
    @pytest.mark.list
    def test_list(self):
        re=self.tag.list()
        assert re.json()["errcode"] == 0
    @pytest.mark.add
    def test_add(self):
        group_name="pushuai"
        tag_list=[{"name":"pu"},
                  {"name":"shuai"}]
        re=self.tag.add(group_name,tag_list)
        assert re.json()["errcode"] == 0
    def test_add_detect(self):
        group_name = "pushuai"
        tag_list = [{"name": "pu"},
                    {"name": "shuai"}]
        re=self.tag.add_and_detect(group_name,tag_list)
        assert re
    def test_update(self):
        tag_id = "et-yZbCAAAJbG81rAME7PsZk9tB2MQOQ"
        tag_name = "pu_new"
        re=self.tag.update(tag_id,tag_name)
        assert re.json()["errcode"] == 0
    def test_deleteGroup(self):
        group_id="et-yZbCAAASqh1YuXoBAXCFR_WQsgQLQ"
        re=self.tag.delete_group(group_id)
        assert re.json()["errcode"] == 0
    def test_detete_and_detect(self):
        group_ids=["et-yZbCAAASqh1YuXoBAXCFR_WQsgQLQ"]
        re=self.tag.delete_and_detect(group_ids)
        assert re.json()["errcode"] == 0

