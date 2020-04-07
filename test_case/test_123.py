#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json, requests, unittest
from ddt import ddt,data,unpack,file_data

@ddt
class run_test_1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup cls")

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    @file_data('ppp.yaml')
    def test_1(self, **kwargs):
        name = kwargs.get('name')
        text = kwargs.get('text')
        print(name, text)

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown cls")

if __name__ == '__main__':
    unittest.main()
