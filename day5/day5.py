# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: day5
# Author: TangJianjun
# Date: 2020/7/10
# Description:
#-----------------------------------------------------------------------------------
#生成器，函数，全局变量与局部变量
"""
在python 中，生成器的本质就是一个迭代器，
使用了yield 的函数被称为生成器（generator）
yield作用：返回值、将函数变成生成器（函数运行是遇到yield后先返回再挂起）
"""
def generator1():
    yield 1
    yield 2
    yield 3
#调用生成器时需要使用nest()或__next()__()函数并重新赋值，
# 否则只能调用第一个field值，当调用次数大于field数量时报错
print(next(generator1()))#1
print(next(generator1()))#1
gt1=generator1()
print(next(gt1))#1
print(next(gt1))#2
print(gt1.__next__())#3
# print(next(gt1))#StopIteration
#生成器推导式
print(type(i for i in range(11)))#<class 'generator'>
print(i for i in range(11))#<generator object <genexpr> at 0x0000029D1E85C840>
pass
#函数：完成特定功能的一个语句组，可以一个功能模块使用，并自定义函数名
"""
def 自定义函数名(参数列表)：
    语句体
"""
def id():
    print("/day5/day5.py")