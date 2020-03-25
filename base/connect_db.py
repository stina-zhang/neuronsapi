# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql.cursors
import json

class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='47.98.47.243',
            port=61306,
            user='domi',
            passwd='domi!#$123454321',
            db='iot_db',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        # result = json.dumps(result)
        return result

    def search_all(self, sql):
        dataNum = self.cur.execute(sql)
        result = self.cur.fetchall()
        # result = json.dumps(result)
        return dataNum, result


