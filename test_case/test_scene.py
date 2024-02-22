#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from base.runmethod import RunMethod
from base.get_Data import GetData
from base.common_util import CommonUtil
from base.operation_header import OperationHeader
from base.dependent_data import  DependentData
import json, requests, unittest
import logging
from base.connect_db import OperationMysql
from base import globalvar
import re

class run_scene(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.run_method = RunMethod()
        cls.data = GetData(fileName='/Users/stina/Desktop/apitest的副本 2.xls', sheetName='scene_edit')
        cls.com_util = CommonUtil()

    @classmethod
    def tearDownClass(cls) -> None:
        '删除场景'
        sql = "SELECT id FROM scene WHERE owner_id=1693143315735314432 AND name!='默认家庭' AND flag=0"
        sql_data = OperationMysql().search_all(sql)
        if sql_data != None:
            sql_count = sql_data[0]
            for i in range(sql_count):
                sid = sql_data[1][i]['id']
                data = json.dumps({"sceneId": sid})
                url = globalvar.Base_Url + '/scene/del'
                header = OperationHeader().get_header()
                requests.post(url=url, data=data, headers=header)
        else:
            pass


    def test_run_scene(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(2, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_request_data(i)
                expect = str(int(self.data.get_expcet_data(i)))
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case,fileName='/Users/stina/Desktop/apitest的副本 2.xls', sheetName='scene_edit')
                    # 获取的依赖响应数据
                    depend_reponse_data = self.depend_data.get_data_for_key(i)
                    #  获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    #  替换数据
                    request_data = re.sub(depend_key, depend_reponse_data, request_data)
                    print(request_data)
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
                    logging.info("**********scene test success***********")
                    globalvar.pass_count.append(i)
                else:
                    self.data.write_result(i, 'fail')
                    logging.info("**********scene test fail***********")
                    globalvar.fail_count.append(i)


if __name__ == '__main__':
    unittest.main()