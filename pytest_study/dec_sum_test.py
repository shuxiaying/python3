# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: dec_sum
# Author: TangJianjun
# Date: 2020/8/14
# Description:
#-----------------------------------------------------------------------------------
# 自定义装饰器
import pytest


def dec_fun(data):
    def wraptor(func):
        for t in range(0,len(data)):
            def inner(argv):
                func(argv)
            inner(data[t])
    return wraptor

@dec_fun([(1,3,4),(1,3,5),[3,7,10],[33]])
# @dec_fun([1,23,3])
def test_sum(argv):
    print(argv,sum(argv))


def test_2(data):
    for i in range(0,len(data)):
        yield (data[i])

test_2([1,2,3])