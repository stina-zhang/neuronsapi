#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.runmethod import RunMethod
from base.get_Data import GetData
from base.common_util import CommonUtil
from base.operation_header import OperationHeader
import json, requests, unittest
from base.send_email import SendEmail
from logs.logger import Logger
import logging
from base.connect_db import OperationMysql
from base import globalvar

class run_scene_add(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        url = "http://api.domi100.net/account/login"
        data = {"username": "13580265868", "password": "123456", "appId": "1469503131678220288"}
        header = {"Content-Type": "application/json"}
        requests.post(url=url, data=json.dumps(data), headers=header)
        cls.run_method = RunMethod()
        cls.data = GetData(fileName='/Users/stina/Desktop/apitest.xls', sheetName='scence_add')
        cls.com_util = CommonUtil()
        cls.send_email = SendEmail()
    @classmethod
    def tearDownClass(cls) -> None:
        sql = "SELECT id FROM scene WHERE owner_id=1825161797143461888 AND name!='默认家庭' AND flag=0"
        sql_data = OperationMysql().search_all(sql)
        if sql_data !=None:
            sql_count = sql_data[0]
            for i in range(sql_count):
                sid = sql_data[1][i]['id']
                data = json.dumps({"sceneId":sid})
                url = 'http://121.40.53.16:8080/scene/del'
                header = OperationHeader().get_header()
                response = requests.post(url=url, data=data, headers=header)
        else:
            pass

    def test_run_scene_add(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            request_data = self.data.get_request_data(i)
            expect = str(int(self.data.get_expcet_data(i)))
            header = self.data.is_header(i)
            if header == None:
                header = OperationHeader().get_header()
            else:
                header = json.loads(header)

            # 表格里填入返回值
            write_json = str(self.run_method.run_main(method, url, request_data.encode('utf-8'), header).json())
            self.data.write_response(i, write_json)

            # 与预期值做比较
            res = str(self.run_method.run_main(method, url, request_data.encode('utf-8'), header).status_code)
            if self.com_util.is_equal_str(expect, res) == 1:
                self.data.write_result(i, 'pass')
                logging.info("**********scence_add test success***********")
                globalvar.pass_count.append(i)
            else:
                self.data.write_result(i, 'fail')
                logging.info("**********scence_add test fail***********")
                globalvar.fail_count.append(i)






