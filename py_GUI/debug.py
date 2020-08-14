# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: debug
# Author: TangJianjun
# Date: 2020/8/13
# Description:
#-----------------------------------------------------------------------------------
import datetime
import os
import sys

now_date=datetime.datetime.today().date()
try:
    with open('./start.log', mode='r', encoding='utf-8') as lf:
        contents = lf.read()
    print(len(contents))
    print((contents))
except:
    with open('./start.log', mode='w', encoding='utf-8') as lf:
        lf.write(str(now_date))

# try:
#     assert len(contents) < 4
# except:
#     with open('./start.log', mode='r', encoding='utf-8') as lf:
#         first_line = lf.readline(-1)
#         first_line = str(first_line)[:first_line.find('\n')]
#     print(first_line)
#     with open('./start.log', mode='w', encoding='utf-8') as lf:
#         for i in contents:
#             if not first_line in i and i !='\n':
