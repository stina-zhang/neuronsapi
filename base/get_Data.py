#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base.operation_excel import OperationExcel
# from base.data_config import global_var
from base import data_config
from base.operation_json import OperetionJson
from base.connect_db import OperationMysql
from base import globalvar

class GetData:
    def __init__(self, fileName=None, sheetName=None):
        self.opera_excel = OperationExcel(fileName, sheetName)

    #  去获取excel行数,就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 去获取用例ID号
    def get_case_id(self, row):
        col = int(data_config.get_id(self))
        case_id = self.opera_excel.get_cell_value(row, col)
        return case_id

    #  获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_run(self))
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #  是否携带header
    def is_header(self, row):
        col = int(data_config.get_header(self))
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None

    #  获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_run_way(self))
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    #  获取url
    def get_request_url(self, row):
        col = int(data_config.get_url(self))
        url = globalvar.Base_Url + self.opera_excel.get_cell_value(row, col)
        return url

    #获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data(self))
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    #  通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperetionJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    #  获取预期结果
    def get_expcet_data(self,row):
        col = int(data_config.get_expect(self))
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    #  通过sql获取预期结果
    def get_expcet_data_for_mysql(self,row):
        op_mysql = OperationMysql()
        sql = self.get_expcet_data(row)
        res = op_mysql.search_one(sql)
        return res.decode('unicode-escape')

    def write_result(self, row, value):
        col = int(data_config.get_result(self))
        self.opera_excel.write_value(row, col, value)
        return(row,col,value)

    def write_response(self, row, value):
        col = int(data_config.get_response(self))
        self.opera_excel.write_value(row, col, value)
        return(row,col,value)

    #  获取依赖数据的key
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend(self))
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    #  判断是否有case依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend(self))
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    #  获取数据依赖字段
    def get_depend_field(self, row):
        col = int(data_config.get_field_depend(self))
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data





