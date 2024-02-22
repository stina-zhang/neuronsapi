#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
import json

from base.operation_excel import OperationExcel
from base.runmethod import RunMethod
from base.get_Data import GetData
from jsonpath_rw import jsonpath, parse
from base.operation_header import OperationHeader

class DependentData:

    def __init__(self, case_id,fileName,sheetName):
        self.case_id = case_id
        self.opera_excel = OperationExcel(fileName, sheetName)
        self.data = GetData(fileName, sheetName)

    #  通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #  执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_request_data(row_num)
        header = self.data.is_header(row_num)
        if header == None:
            header = OperationHeader().get_header()
        else:
            header = json.loads(header)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, header).json()
        return res

    #  根据依赖的key去获取执行依赖测试case的响应,然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]