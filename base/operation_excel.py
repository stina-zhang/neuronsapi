#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import xlrd
from xlutils.copy import copy
class OperationExcel:
    def __init__(self, file_name=None, sheet_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_name = sheet_name
        else:
            self.file_name = '/Users/stina/PycharmProjects/neuronsapi/test_case/neuronsapitest.xls'
            self.sheet_name = 'login'
        self.data = self.get_data()

    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name, formatting_info=True)
        tables = data.sheet_by_name(self.sheet_name)
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    #写入数据
    def write_value(self, row, col, value):
        '''
        写入excel数据
        row,col,value
        '''
        read_data = xlrd.open_workbook(self.file_name, formatting_info=True)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_name)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    #根据对应的caseid 找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    #根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num+1


    #根据行号，找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


