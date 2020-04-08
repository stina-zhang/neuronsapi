#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from base.runmethod import RunMethod
from base.get_Data import GetData
from base.common_util import CommonUtil
from base.operation_header import OperationHeader
import json, requests, unittest
import logging
from base.connect_db import OperationMysql
from base import globalvar
import re

class run_room_getAll(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        '''获取新增家庭ID'''
        cls.header = OperationHeader().get_header()
        url = globalvar.Base_Url + "/scene/add"
        data = {"name": "002 testhome"}
        cls.sceneid = requests.post(url=url, data=json.dumps(data), headers=cls.header).json()['result']
        '''新增房间'''
        room_url = globalvar.Base_Url + "/room/add"
        room_data = {"sceneId" : cls.sceneid, "name" : "测试房间", "icon":2}
        requests.post(url=room_url, data=json.dumps(room_data), headers=cls.header)
        '''读测试用例sheet'''
        cls.data = GetData(fileName='/Users/stina/Desktop/apitest.xls', sheetName='room_getAll')
        cls.run_method = RunMethod()
        cls.com_util = CommonUtil()

    def test_run_room_getAll(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            url = globalvar.Base_Url + self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            request_data_old = self.data.get_request_data(i)
            request_data = re.sub('sid', self.sceneid, request_data_old)
            expect = self.data.get_expcet_data(i)
            header = self.data.is_header(i)
            if header == None:
                header = self.header
            else:
                header = json.loads(header)
            response = self.run_method.run_main(method, url, request_data.encode('utf-8'), header).json()

            # 表格里填入返回值
            write_json = str(response)
            self.data.write_response(i, write_json)

            # 与预期值做比较
            res = "state':"+ str(response['state'])
            if self.com_util.is_equal_str(expect, res) == 1:
                self.data.write_result(i, 'pass')
                logging.info("**********room_getAll test success***********")
                globalvar.pass_count.append(i)
            else:
                self.data.write_result(i, 'fail')
                logging.info("**********room_getAll test fail***********")
                globalvar.fail_count.append(i)

    @classmethod
    def tearDownClass(cls) -> None:
        '''删除测试房间'''
        sql_room = "SELECT id FROM room WHERE creator=1693143315735314432 AND name!='默认房间' AND flag=0"
        sql_room_data = OperationMysql().search_all(sql_room)
        if sql_room_data != None:
            sql_count = sql_room_data[0]
            for i in range(sql_count):
                rid = sql_room_data[1][i]['id']
                data = json.dumps({"roomId": rid})
                url = globalvar.Base_Url + '/room/del'
                response = requests.post(url=url, data=data, headers=cls.header)
        else:
            pass

        '''删除测试家庭'''
        sql_scene = "SELECT id FROM scene WHERE owner_id=1693143315735314432 AND name!='默认家庭' AND flag=0"
        sql_scene_data = OperationMysql().search_all(sql_scene)
        if sql_scene_data != None:
            sql_count = sql_scene_data[0]
            for i in range(sql_count):
                sid = sql_scene_data[1][i]['id']
                data = json.dumps({"sceneId": sid})
                url = globalvar.Base_Url + '/scene/del'
                response = requests.post(url=url, data=data, headers=cls.header)
        else:
            pass

if __name__ == '__main__':
    unittest.main()