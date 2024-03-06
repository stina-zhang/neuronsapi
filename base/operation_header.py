#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json

class OperationHeader:

    def login(self):
        url = "https://sleep.neuronsxc.com/login/password"
        data = {"username":"root","password":"yyds@neurons"}
        header = {"Content-Type": "application/json"}
        rep = requests.post(url=url, data=json.dumps(data), headers=header, verify=False)
        return rep

    def get_token(self):
        token = self.login().json()['data']['token']
        return token

    def get_header(self):
        newToken = self.get_token()
        header = {"Content-Type": "application/json", "Authorization": newToken}
        return header


