#!/usr/bin/env python
#coding=utf-8
#author:pushuai
import pytest
from  datetime import datetime
from jsonpath import jsonpath
from server1.tag import Tag
class TestTag():
    def setup_class(self):
        group_name="pushuai"
        self.tag=Tag()
        self.tag.clean_data(group_name)
    def test_list(self):
        re=self.tag.list()
        assert re.json()["errcode"] == 0
    @pytest.mark.parametrize("group_name,tag_list",[
        ["pushuai",[{"name": "TAG_NAME_1"}]],
        ["pushuai",[{"name": "TAG_NAME_2"}]],
    ])
    @pytest.mark.run(order=1)
    def test_add(self,group_name,tag_list):
        re=self.tag.add(group_name,tag_list)
        print(jsonpath(re.json(), "$..name"))
        assert tag_list[0]["name"] in jsonpath(re.json(), "$..name")
    @pytest.mark.run(order=3)
    def test_deleteGroupId(self):
        #group_id=["et-yZbCAAAylgH0xF_pgdbdOUD9LmDcg"]]]
        group_name="pushuai"
        group_id=self.tag.check_isExit(group_name)
        re=self.tag.deleteGroupId(group_id)
        assert re.json()["errcode"] == 0
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("group_name,tag_name_before",[
        ["pushuai","TAG_NAME_1"],
        ["pushuai", "TAG_NAME_2"],
    ])
    def test_update(self,group_name,tag_name_before):
        tag_id = self.tag.search_tag_id(group_name,tag_name_before)
        tag_name = tag_name_before + str(datetime.now().strftime("%Y%m%d-%H%M%S"))
        re=self.tag.update(tag_id,tag_name)
        assert re.json()["errcode"] == 0




