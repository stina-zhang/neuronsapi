#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import os
import configparser


class Config:
    """配置文件"""
    def __init__(self):
        self.config_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'config.ini')
        if not os.path.exists(self.config_path):
            raise FileNotFoundError("配置文件%s不存在！" % self.config_path)
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(self.config_path, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(self.config_path, 'w') as f:
            self.config.write(f)


    @property
    def base_url(self):
        return self._get("HTTP", "Base_Url")


# if __name__ == '__main__':
    # Base_Url = Config().base_url

