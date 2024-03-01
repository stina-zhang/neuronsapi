#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.runmethod import RunMethod
from base.get_Data import GetData
from base.common_util import CommonUtil
from base.operation_header import OperationHeader
import json
from base.send_email import SendEmail
from logs.logger import Logger
import logging, unittest
from base import globalvar

class run_login(unittest.TestCase):
    def setUp(self) -> None:
        self.run_method = RunMethod()
        self.data = GetData(fileName=r'C:\Users\Neurons\Desktop\neuronsapitest.xls', sheetName='login')
        self.com_util = CommonUtil()

    def tearDown(self) -> None:
        pass

    def test_login(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            cid = self.data.get_case_id(i)
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            request_data = self.data.get_request_data(i)
            expect = self.data.get_expcet_data(i)
            header = self.data.is_header(i)
            if header == None:
                header = OperationHeader().get_header()
            else:
                header = json.loads(header)

            # 表格里填入返回值
            res = str(self.run_method.run_main(method, url, request_data, header).json())
            self.data.write_response(i, res)

            #与预期值做比较
            res_message = 'message: ' + self.run_method.run_main(method, url, request_data, header).json().get("message")
            if self.com_util.is_equal_str(expect, res_message) == 1:
                self.data.write_result(i, 'pass')
                logging.info("**********login test success***********")
                globalvar.pass_count.append(i)
            else:
                self.data.write_result(i, 'fail')
                logging.info("**********login test fail***********")
                globalvar.fail_count.append(i)





















