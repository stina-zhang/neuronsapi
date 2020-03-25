#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import logging, time, os, sys

class Logger():

    def __init__(self, file_or_terminal, level):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
        info = '''
                file_or_terminal == terminal: 只打印到命令行
                file_or_terminal == file: 只打印到日志文件
                file_or_terminal == all: 同时打印到日志文件和命令行
                level = CRITICAL','ERROR','WARNING','INFO','DEBUG
            '''
        proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        resultPath = os.path.join(proDir, 'logs')
        result_Log_Path = os.path.join(resultPath, 'Log')
        # result_Html_Path = os.path.join(resultPath, 'HTML报告')
        Log_month_Dir = os.path.join(result_Log_Path, time.strftime("%Y-%m"))
        self.Log_day_log_Path = os.path.join(Log_month_Dir, time.strftime("%Y-%m-%d") + '.log')
        # 创建result文件夹及里面的日期时间文件夹、创建Log文件夹、创建"HTML报告"文件夹、当天日期命名的log文件夹（若不存在）
        for i in [resultPath, result_Log_Path, Log_month_Dir]:
            if not os.path.exists(i):
                os.mkdir(i)
        time.sleep(0.1)
        self.file_or_terminal = file_or_terminal
        # logging.info("**********邮件发送***********")

    def getLogger(self):
        fm = logging.Formatter(
            fmt='%(asctime)s %(filename)s[%(lineno)d] %(levelname)s %(message)s %(module)s %(funcName)s',
            datefmt="%Y-%m-%d %X")

        def only_file():
            fh = logging.FileHandler(os.path.join(self.Log_day_log_Path))
            fh.setFormatter(fm)
            self.logger.addHandler(fh)
            return self.logger

        def only_terminal():
            ch = logging.StreamHandler()
            ch.setFormatter(fm)
            self.logger.addHandler(ch)
            return self.logger

        def file_and_terminal():
            only_file()
            only_terminal()
            return self.logger

        choice_dict = {
            "terminal": only_terminal,
            "file": only_file,
            "all": file_and_terminal,
        }

        if choice_dict.get(self.file_or_terminal):
            return choice_dict.get(self.file_or_terminal)()
        else:
            return choice_dict.get("file")()


