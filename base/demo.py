#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import json


class RunMain:

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def send_post(self, url, data, header):
        res = requests.post(url=url, data=data, headers=header).json()
        return res

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data, headers)
        return res

if __name__ == '__main__':
    url = 'http://api.domi100.net/account/login'
    data = json.dumps({"username": "18167122309", "password": "e10adc3949ba59abbe56e057f20f883e", "appId": "1469503131678220288"})
    header = {"Content-Type": "application/json"}
    res = RunMain().run_main(url, 'post', data, header)




