#!/usr/bin/env python
#coding=utf-8
#author:pushuai
import json
import random
import string

import requests


class BaseConnect():
    def __init__(self):
        self.token = self.get_token()
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid = "wwf350dc501ba40036"
        corpsecret = "T7Ut5tfjfQc8_8m1gsTlLr2Le-xGNDSKrUMTLekG-iM"
        re=requests.get(url,params={"corpid": corpid, "corpsecret": corpsecret})
        assert re.json()["errcode"] == 0
        access_Token = re.json()["access_token"]
        return access_Token
    def random_mobile(self):
        headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                    "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                    "186", "187", "188", "189"]
        head=random.choice(headList)
        tail=''.join(random.sample(string.digits,8))
        mobile=head+tail
        return mobile
    def send(self,kwargs):
        re=requests.request(**kwargs)
        print(json.dumps(re.json(), indent=2))
        return re