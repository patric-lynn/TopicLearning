#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
        raise Networkerror("Bad hostname")
except Networkerror, e:
        print e.args