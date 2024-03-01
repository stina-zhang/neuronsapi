#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import xlrd, requests, json
import urllib3
import random
def get_token():
    token_Url = "https://sleep.neuronsxc.com/login/password"
    token_Data = {"username":"root","password":"yyds@neurons"}
    token_Headers = {"Content-Type": "application/json"}
    rep = requests.post(token_Url, data=json.dumps(token_Data), headers=token_Headers,verify=False)
    token = rep.json()['data']['token']
    return token
def get_Headers(inToken):
    headers = {"Content-Type": "application/json", "token": inToken}
    return headers

def user_Register():
    user_tel = '13' + str(random.randint(100000000,999999999))
    addUser_Url = 'http://api.domi100.net/account/register'
    headers = {"Content-Type": "application/json"}
    excelDir = '/Users/stina/Desktop/apitest.xls'
    workbook = xlrd.open_workbook(excelDir)
    workSheet = workbook.sheet_by_name('sheet1')
    userData = json.loads(workSheet.cell_value(2, 6))
    userData['username'] = user_tel

    resp = requests.post(addUser_Url, data=json.dumps(userData), headers=headers)
    addUserId = resp.json()['result']['id']
    return addUserId




if __name__ == '__main__':

    urllib3.disable_warnings()
    token = get_token()
    headers = get_Headers(token)
    # addUserId = user_Register()
    print(token)
    print(headers)
    # print(addUserId)




