#!/usr/bin/env python
#coding=utf-8
#author:pushuai
import json
import logging
import requests
from hamcrest import *
from serve.base_api import BaseApi
class Tag(BaseApi):
    def __init__(self):
        super().__init__()
    def list(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        data={
            "method":"post",
            "url":url,
            "params":{"access_token": self.token},
            "json":{'tag_id': []}
        }
        re=self.send(data)
        return re

    def add(self,group_name,tag_list,**kwargs):
        """
        :param group_name: 标签组的名字
        :param tag_list: 标签列表
        :param kwargs: 包括group_id等
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        data={
            "method":"post",
            "url":url,
            "params":{"access_token": self.token},
            "json":{
                "group_name":group_name,
                "tag":tag_list,
                **kwargs
            }
        }
        re=self.send(data)
        return re
    def is_tag_group_name_exist(self,group_name):
        #查询元素是否存在,如果不存在报错
        for group in self.list().json()["tag_group"]:
            if group_name in group["group_name"]:
                return group["group_id"]
        """
        如果写return false，不能准备判断，因为false，none,"",0,返回都是相同的
        """
        return ""
    def is_group_id_exit(self,group_id):
        for group in self.list().json()["tag_group"]:
            if group_id in group["group_id"]:
                return True
            return False
    #在添加之前进行数据清理清理
    def add_and_detect(self,group_name,tag_list,**kwargs):
        re=self.add(group_name,tag_list,**kwargs)
        if re.json()["errcode"] == 40017:
            group_id=self.is_tag_group_name_exist(group_name)
            if not group_id:
                return False
            self.delete_group(group_id)
            self.add(group_name, tag_list,**kwargs)
        result=self.is_tag_group_name_exist(group_name)
        if not result:
            print("add not success")
        return result


    def update(self,tag_id,tag_name):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag"
        data={
            "method":"post",
            "url":url,
            "params":{"access_token": self.token},
            "json":{"id": tag_id, "name": tag_name}
        }
        re=self.send(data)
        return re
    def delete_group(self,group_id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        data={
            "method":"post",
            "url":url,
            "params":{"access_token": self.token},
            "json":{"group_id":group_id}
        }
        re=self.send(data)
        return re
    def delete_and_detect(self,group_ids):
        delete_group_ids=[]
        re=self.delete_group(group_ids)
        #如果group_id不存在进行添加再删除的操作
        if re.json()["errcode"] == 40068:
            for group_id in group_ids:
                #如果标签不存在,进行id创建并添加到标签组
                if not self.is_group_id_exit(group_id):
                    group_id_add=self.add_and_detect(group_name="pushuai",tag_list = [{"name": "pu"},
                    {"name": "shuai"}])
                    delete_group_ids.append(group_id_add)
                #如果标签存在就存在标签组俩门
                else:
                    delete_group_ids.append(group_id)
            re=self.delete_group(delete_group_ids)
        return re







