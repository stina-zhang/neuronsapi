#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
# sys.path.append("E:/www/ImoocInterface")
from base.runmethod import RunMethod
from base.get_Data import GetData
from base.common_util import CommonUtil
# from data.dependent_data import DependdentData
# from util.send_email import SendEmail
from base.operation_header import OperationHeader
from base.operation_json import OperetionJson

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mai = SendEmail()


    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()

        for i in range(1, rows_count):
            # is_run = self.data.get_is_run(i)
            # if is_run:
            cid = self.data.get_case_id(i)
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            request_data = self.data.get_request_data(i)
            # request_data = self.data.get_data_for_json(i)
            expect = self.data.get_expcet_data(i)
            header = self.data.is_header(i)
            # depend_case = self.data.is_depend(i)
            # if depend_case != None:
            #     self.depend_data = DependdentData(depend_case)
                #获取的依赖响应数据
                # depend_response_data = self.depend_data.get_data_for_key(i)
                #获取依赖的key
                # depend_key = self.data.get_depend_field(i)
                # request_data[depend_key] = depend_response_data

                # res = self.run_method.run_main(method, url, request_data)
                # op_header = OperationHeader(res)
                # op_header.write_cookie()
            if header == None:
                header = OperationHeader().get_header()
            # elif header == 'yes':
            #     op_json = OperetionJson('../dataconfig/cookie.json')
            #     cookie = op_json.get_data('apsid')
            #     cookies = {
            #         'apsid':cookie
            #     }
            #     res = self.run_method.run_main(method, url, request_data,cookies)


            res = str(self.run_method.run_main(method, url, request_data, header).status_code)

            if self.com_util.is_equal_str(expect, res) == 1:
                # print(f'第{i+1}行' + '测试通过')
                # print(expect)
                # print(res)
                self.data.write_result(i, 'pass')
                # pass_count.append(i)
            else:
                self.data.write_result(i, 'fail' + res)
                # fail_count.append(i)
                print(cid + '测试不通过')
        # self.send_mai.send_main(pass_count,fail_count)




if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
