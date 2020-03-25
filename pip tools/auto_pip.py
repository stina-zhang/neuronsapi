#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os, logging


#  日志配置
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
logDir = './auto_pip.log'
logging.basicConfig(filename=logDir, level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


#  读取配置文件
fo = open('./config.ini')
lines = fo.read().splitlines()   #返回list,自动去掉换行符

#  执行安装库的指令
backInfo = os.popen('pip list')
info = backInfo.read()

#  验证是否安装成功
for line in lines:
    if line in info:
        logging.warning(f'--------{line} installed')
    else:
        pipObject = os.popen('pip list ' + line)
        pipRes = pipObject.read()
        if 'successful' in pipRes:
            logging.info(f'---------{line} installed pass')
        else:
            logging.error(f'---------{line} installed failed')

