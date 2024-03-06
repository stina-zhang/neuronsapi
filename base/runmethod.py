#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import urllib3
import json
class RunMethod:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    def post_main(self, url, data, header=None):
        res = None

        if header != None:
            res = requests.post(url=url, data=data, headers=header,verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        # return json.dumps(res, ensure_ascii=False)
        return res

# if __name__ == '__main__':
    # url = 'http://api.domi100.net/account/login'
    # data = json.dumps(
        # {"username": "18167122309", "password": "e10adc3949ba59abbe56e057f20f883e", "appId": "1469503131678220288"})
    # header = {"Content-Type": "application/json"}
    # res = RunMethod().run_main('Post', url, data, header)['result']['id']
    # run = json.loads(res)['result']['id']
    # print('id= ' + res)


