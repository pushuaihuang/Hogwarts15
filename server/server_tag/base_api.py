#!/usr/bin/env python
#coding=utf-8
#author:pushuai
import json

import requests
from hamcrest import *
class BaseApi():
    def __init__(self):
        self.token=self.getToken()
    def getToken(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid = "wwf350dc501ba40036"
        corpsecret = "VMhPaQhHoy9jSVRqR-BID7P7a5tJ6rbFBWlDLnDvDjw"
        data={
            "method":"get",
            "url":url,
            "params":{"corpid": corpid, "corpsecret": corpsecret}
        }
        re=self.send(data)
        #使用hamcrest断言更加的灵活
        assert_that(re.status_code, equal_to(200))
        assert_that(re.json()["errcode"], equal_to(0))
        access_Token = re.json()["access_token"]
        return access_Token
    def send(self,kwargs):
        re=requests.request(**kwargs)
        print(json.dumps(re.json(), indent=2))
        return re
