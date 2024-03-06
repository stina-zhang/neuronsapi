#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from logs.logger import Logger
from test_case import test_login, test_dept_add
from base.send_email import SendEmail
from base import globalvar
from HTMLTestRunnerNew import HTMLTestRunner
import time, os
import configparser
from common.readconfig import Config


if __name__ == '__main__':

    '日志配置'
    Logger('all', 'INFO').getLogger()

    '测试报告设置'
    report_name = 'neurons接口测试报告'
    report_title = 'neurons接口unittest框架测试报告'
    report_desc = 'neurons登录和增加科室接口详细测试报告'
    report_path = './report/'
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_file = report_path + 'report_' + timestr + '.html'
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    else:
        pass
    with open(report_file, 'wb') as report:
        '添加测试用例'
        suite = unittest.TestSuite()
        suite.addTest(test_login.run_login('test_login'))
        suite.addTest(test_dept_add.run_dept_add('test_run_dept_add'))
        runner = HTMLTestRunner(stream=report, verbosity=2, title=report_title, description=report_desc)
        runner.run(suite)
    report.close()
    time.sleep(3)
    '发送邮件'
    pass_count = globalvar.pass_count
    fail_count = globalvar.fail_count
    SendEmail().send_main(pass_count, fail_count)



