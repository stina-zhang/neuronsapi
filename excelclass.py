#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import xlrd, requests, json
import random
def get_token():
    token_Url = "http://api.domi100.net/account/login"
    token_Data = {"username": "18167122309", "password": "e10adc3949ba59abbe56e057f20f883e", "appId": "1469503131678220288"}
    token_Headers = {"Content-Type": "application/json"}
    rep = requests.post(token_Url, data=json.dumps(token_Data), headers=token_Headers)
    token = rep.json()['result']['token']
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
    token = get_token()
    headers = get_Headers(token)
    addUserId = user_Register()
    print(token)
    print(headers)
    print(addUserId)




