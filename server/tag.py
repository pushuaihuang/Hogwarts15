#!/usr/bin/env python
#coding=utf-8
#author:pushuai
import json

import requests
from hamcrest import *

class Tag():
    def __init__(self):
        self.token=self.getToken()
    def getToken(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid="wwf350dc501ba40036"
        corpsecret="VMhPaQhHoy9jSVRqR-BID7P7a5tJ6rbFBWlDLnDvDjw"
        re=requests.get(url,params={"corpid":corpid,"corpsecret":corpsecret})
        assert_that(re.status_code,equal_to(200))
        assert_that(re.json()["errcode"],equal_to(0))
        access_Token=re.json()["access_token"]
        return access_Token
    def add(self,group_name,tag_list:list):
        #添加企业客户标签
        """
        企业可通过此接口向客户标签库中添加新的标签组和标签，每个企业最多可配置3000个企业标签。
        暂不支持第三方调用。
        请求方式: POST(HTTP)
        请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?access_token=ACCESS_TOKEN
        :return:
        """
        #tag_list,示例： tag_list = '[{"name": tag_name,"order": 1},{"name": "TAG_NAME_2","order": 2}]'
        url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        re=requests.post(url,params={"access_token": self.token},json={"group_name": group_name,
            "tag": tag_list})
        print(json.dumps(re.json(), indent=2))
        return re
    def list(self):
        # 接口获取企业客户标签详情
        """
        请求方式：post
        url=https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?access_token=ACCESS_TOKEN
        参数：access_token;参数说明：调用接口凭证
            tag_id；参数说明：要查询标签id，默认不填写获取所有id

        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        re = requests.post(url, params={"access_token": self.token}, json={'tag_id': []})
        # assert_that(re.status_code, equal_to(200))
        # assert_that(re.json()["errcode"], equal_to(0))
        print(json.dumps(re.json(),indent=2,ensure_ascii=False))
        return re

    def update(self,tag_id,tag_name):
        """
        企业可通过此接口编辑客户标签/标签组的名称或次序值。
        暂不支持第三方调用。
        请求方式: POST(HTTP)
        请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag?access_token=ACCESS_TOKEN
        :return:
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag"
        re=requests.post(url,params={"access_token": self.token},json={"id":tag_id,"name":tag_name})
        print(json.dumps(re.json(), indent=2, ensure_ascii=False))
        return re
    def deleteTagId(self,tag_id):
        """
        删除企业客户标签
        企业可通过此接口删除客户标签库中的标签，或删除整个标签组。
        暂不支持第三方调用。
        请求方式: POST(HTTP)
        请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag
        :return:
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        re=requests.post(url,params={"access_token": self.token},json=tag_id)
        return re
    def deleteGroupId(self,group_id):
        """
        删除企业客户标签
        企业可通过此接口删除客户标签库中的标签，或删除整个标签组。
        暂不支持第三方调用。
        请求方式: POST(HTTP)
        请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag
        :return:
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        re=requests.post(url,params={"access_token": self.token},json={"group_id":group_id})
        print(json.dumps(re.json(), indent=2, ensure_ascii=False))
        return re
    def clean_data(self,group_name):
        re=self.list()
        #判断标签组名是否已经存在，如果存在则删除
        for group in re.json()["tag_group"]:
            if(group["group_name"] == group_name):
                group_id = group["group_id"]
                self.deleteGroupId(group_id)
    def check_isExit(self,group_name):
        re = self.list()
        for group in re.json()["tag_group"]:
            if (group["group_name"] == group_name):
                group_id = group["group_id"]
                return group_id
    def search_tag_id(self,group_name,tag_name_before):
        re = self.list()
        for group in re.json()["tag_group"]:
            if(group["group_name"] == group_name):
                for tag in group["tag"]:
                    if(tag["name"]==tag_name_before):
                        tag_id=tag["id"]
                        return tag_id
