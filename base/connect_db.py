# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql.cursors
import json

class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='',
            port=61306,
            user='',
            passwd='',
            db='iot_db',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def search_all(self, sql):
        dataNum = self.cur.execute(sql)
        result = self.cur.fetchall()
        # result = json.dumps(result)
        return dataNum, result


