# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: py_os
# Author: TangJianjun
# Date: 2020/7/14
# Description:
#-----------------------------------------------------------------------------------
import os
# 创建目录：当目录不存在时，使用os.mkdir()创建目录
# os.mkdir('c:\\test')
# 只能创建单目录，不能创建多个目录
# os.mkdir('c:\\test\\test1')
# 删除空目录：os.rmdir()
# os.rmdir('c:\\test\\test1')
# 删除非空目录
import shutil
# shutil.rmtree('c:\\test')
#判断是否存在文件夹或文件，存在返回True，不存在返回false
# from sys import path
# print(path.isdir('c:\\test'))
# print(path.isfile('c:\\test'))
# print(os.path.exists('c:\\test'))
# 获取当前盘符下所有文件和文件夹的名称
# print(os.listdir('c:\\'))
# 获取文件的最近访问时间，以epoch格式显示
# print(os.path.getatime('c:\\test'))
# 获取文件的创建时间，以epoch格式显示
# print(os.path.getctime('c:\\test'))
# 获取文件的最近修改时间，以epoch格式显示
tm=os.path.getmtime('c:\\test')
print(tm)
# 将epoch格式时间转成字符串格式显示
import time
dm=time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(tm))
print(dm)