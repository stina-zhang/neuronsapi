#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from logs.logger import Logger
from test_case import test_login, test_sence_add
from base.send_email import SendEmail
from base import globalvar
from HTMLTestRunnerNew import HTMLTestRunner
import time, os


if __name__ == '__main__':

    # 日志配置
    Logger('all', 'INFO').getLogger()

    # 添加测试用例
    suite = unittest.TestSuite()
    suite.addTest(test_login.run_login('test_login'))
    suite.addTest(test_sence_add.run_scene_add('test_run_scene_add'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

    #发送邮件
    pass_count = globalvar.pass_count
    fail_count = globalvar.fail_count
    # SendEmail().send_main(pass_count, fail_count)

    # 测试报告设置
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
        suite.addTest(test_sence_add.run_scene_add('test_run_scene_add'))
        runner = HTMLTestRunner(stream=report, title=report_title, description=report_desc)
        runner.run(suite)
    report.close()
    time.sleep(3)
