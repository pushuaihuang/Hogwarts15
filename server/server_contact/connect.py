#!/usr/bin/env python
#coding=utf-8
#author:pushuai
import json
import requests
from server_contact.base_connect import BaseConnect
class Connect(BaseConnect):
    def __init__(self):
        super().__init__()
    def creat_connect(self,user_id,name,**kwargs):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create
        :param user_id:
        :param name:
        :param token:
        :param kwargs:department:,mobile：手机号码
        :return:
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data={
            "method":"post",
            "url":url,
            "params":{"access_token": self.token},
            "json":{
                "userid": user_id,
                "name": name,
                "mobile": self.random_mobile(),
                **kwargs
            }

        }
        re=self.send(data)
        return re
    def get_member(self,userid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :param userid:
        :return:
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/user/get"
        data={
            "method":"get",
            "url":url,
            "params":{"access_token":self.token,"userid":userid},
        }
        re=self.send(data)
        return re
    def update_member(self,userid,**kwargs):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :userid:用户id，前端的账号名
        :return:
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data={
            "method":"post",
            "url":url,
            "params":{"access_token":self.token},
            "json":{
                "userid": userid,
                **kwargs
            }
        }
        re=self.send(data)
        return re
    def delete_member(self,userid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        data={
            "method":"get",
            "url":url,
            "params":{"access_token":self.token,"userid":userid},
                             }
        re=self.send(data)
        return re
    def delete_and_detect(self,userid):
        re=self.delete_member(userid)
        #如果不存在，创建userid
        if re.json()["errcode"] == 60111:
            name = "shuai"
            department = [1]
            mobile = self.random_mobile()
            self.creat_connect(userid,name,department=department,mobile=mobile)
            result=self.delete_member(userid)
            return result
        return re
    #检查userid是否存在，存在先删除
    def create_and_detect(self,userid,name,**kwargs):
        re=self.creat_connect(userid,name,**kwargs)
        if re.json()["errcode"] == 60102:
            re=self.delete_member(userid)
            re=self.creat_connect(userid, name, **kwargs)
            return re
        return re
    def update_and_detect(self,userid,name,**kwargs):
        re=self.update_member(userid)
        if re.json()["errcode"] == 60111:
            name1 = "shuai"
            department = [1]
            re=self.creat_connect(userid,name1,department=department)
            result=self.update_member(re.json()["userid"],name)
            return result
        return re





