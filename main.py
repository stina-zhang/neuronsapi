#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from logs.logger import Logger
from test_case import test_login, test_scene_add, test_scene_del, test_scene_getAll, test_scene_edit
from test_case import test_room_add, test_room_getAll, test_room_edit, test_room_del
from test_case import test_firm_add, test_firm_getAll, test_firm_edit, test_firm_del
from test_case import test_product_add, test_product_getById, test_product_getByPage,test_product_edit, test_product_del
from base.send_email import SendEmail
from base import globalvar
from HTMLTestRunnerNew import HTMLTestRunner
import time, os
import configparser
from common.readconfig import Config


if __name__ == '__main__':
    #
    '日志配置'
    Logger('all', 'INFO').getLogger()
    #
    # '添加测试用例'
    # suite = unittest.TestSuite()
    # suite.addTest(test_login.run_login('test_login'))
    # suite.addTest(test_scene_add.run_scene_add('test_run_scene_add'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #
    # '发送邮件'
    # pass_count = globalvar.pass_count
    # fail_count = globalvar.fail_count
    # # SendEmail().send_main(pass_count, fail_count)
    #
    '测试报告设置'
    report_name = 'Domi接口测试报告'
    report_title = '多米家接口unittest框架测试报告'
    report_desc = '多米家登录和场景接口详细测试报告'
    report_path = './report/'
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_file = report_path + 'report_' + timestr + '.html'
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    else:
        pass
    with open(report_file, 'wb') as report:
        suite = unittest.TestSuite()
        suite.addTest(test_login.run_login('test_login'))
        suite.addTest(test_scene_add.run_scene_add('test_run_scene_add'))
        suite.addTest(test_scene_del.run_scene_del('test_run_scene_del'))
        suite.addTest(test_scene_del.run_scene_del('test_run_scene_del_error'))
        suite.addTest(test_scene_getAll.run_scene_getAll('test_run_scene_getAll'))
        suite.addTest(test_scene_edit.run_scene_edit('test_run_scene_edit'))
        suite.addTest(test_room_add.run_room_add('test_run_room_add'))
        suite.addTest(test_room_getAll.run_room_getAll('test_run_room_getAll'))
        suite.addTest(test_room_edit.run_room_edit('test_run_room_edit'))
        suite.addTest(test_room_del.run_room_del('test_run_room_del'))
        suite.addTest(test_firm_add.run_firm_add('test_run_firm_add'))
        suite.addTest(test_firm_getAll.run_firm_getAll('test_run_firm_getAll'))
        suite.addTest(test_firm_edit.run_firm_edit('test_run_firm_edit'))
        suite.addTest(test_firm_del.run_firm_del('test_run_firm_del'))
        suite.addTest(test_product_add.run_product_add('test_run_product_add'))
        suite.addTest(test_product_getById.run_product_getById('test_run_product_getById'))
        suite.addTest(test_product_getByPage.run_product_getByPage('test_run_product_getByPage'))
        suite.addTest(test_product_edit.run_product_edit('test_run_product_edit'))
        suite.addTest(test_product_del.run_product_del('test_run_product_del'))
        runner = HTMLTestRunner(stream=report, verbosity=2, title=report_title, description=report_desc)
        runner.run(suite)
    report.close()
    time.sleep(3)
    '发送邮件'
    pass_count = globalvar.pass_count
    fail_count = globalvar.fail_count
    SendEmail().send_main(pass_count, fail_count)



