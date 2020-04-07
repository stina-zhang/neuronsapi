#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json

class OperationHeader:

    def get_token(self):
        url = "http://api.domi100.net/account/login"
        data = {"username": "13800138002", "password": "123456", "appId": "1469503131678220288"}
        header = {"Content-Type": "application/json"}
        rep = requests.post(url=url, data=json.dumps(data), headers=header)
        token = rep.json()['result']['token']
        return token
    def get_header(self):
        newToken = self.get_token()
        header = {"Content-Type": "application/json", "token": newToken}
        return header


