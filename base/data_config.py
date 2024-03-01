#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class global_var:

#   case_id
    Id = '0'
    request_name = '1'
    url = '3'
    run = '10'
    request_way = '4'
    header = '5'
    case_depend = '11'
    data_depend = '12'
    field_depend = '13'
    data = '6'
    expect = '7'
    response = '8'
    result = '9'

#   获取caseid
def get_id(self):
    return global_var.Id

#   获取url
def get_url(self):
    return global_var.url

def get_run(self):
    return global_var.run

def get_run_way(self):
    return global_var.request_way

def get_header(self):
    return global_var.header

def get_case_depend(self):
    return global_var.case_depend

def get_data_depend(self):
    return global_var.data_depend

def get_field_depend(self):
    return global_var.field_depend

def get_data(self):
    return global_var.data

def get_expect(self):
    return global_var.expect

def get_response(self):
    return global_var.response

def get_result(self):
    return global_var.result

def get_header_value(self):
    return global_var.header


