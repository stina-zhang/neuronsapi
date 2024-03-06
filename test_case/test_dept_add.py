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

class run_dept_add(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        "登录"
        url = globalvar.Base_Url + "/login/password"
        data = { "username": "root","password": "yyds@neurons"}
        header = {"Content-Type": "application/json"}
        requests.post(url=url, data=json.dumps(data), headers=header,verify=False)
        cls.run_method = RunMethod()
        cls.data = GetData(fileName='/Users/stina/PycharmProjects/neuronsapi/test_case/neuronsapitest.xls', sheetName='dept_add')
        cls.com_util = CommonUtil()
        cls.header = OperationHeader().get_header()
        # cls.send_email = SendEmail()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_run_dept_add(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
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
            res = self.run_method.run_main(method, url, request_data.encode("utf-8"), header).json()
            write_json = str(res)
            print(write_json)
            self.data.write_response(i, write_json)

            # 与预期值做比较
            res_message =res.get("message")
            if self.com_util.is_contain(expect, res_message) == 1:
                self.data.write_result(i, 'pass')
                logging.info("**********dept_add test success***********")
                globalvar.pass_count.append(i)
            else:
                self.data.write_result(i, 'fail')
                logging.info("**********dept_add test fail***********")
                globalvar.fail_count.append(i)

            # 获取id
            if res_message == "ok":
                "通过新增的科室名称获取ID"
                dept_name = json.loads(request_data).get("deptName")
                query_url = "https://sleep.neuronsxc.com/smDept/getDeptList?deptName="+dept_name+"&typeId=&isDeleted=0&pageNum=1&pageSize=10"
                dept_Id = self.run_method.run_main(method="get", url=query_url, header=header).json().get("data").get("list")[0].get("deptId")
                "删除新增的科室"
                delete_url = "https://sleep.neuronsxc.com/smDept/deleteById?id=" + str(dept_Id)
                response = self.run_method.run_main(method="get", url=delete_url, header=header)






if __name__ == '__main__':
    unittest.main()






