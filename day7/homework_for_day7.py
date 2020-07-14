# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: homework_for_day7
# Author: TangJianjun
# Date: 2020/7/14
# Description:
#-----------------------------------------------------------------------------------
import os
from day6.CEM import GetCsvData, GetExcelData, MysqlConnect
# 第一题
while 1:
    if os.path.exists('C:\\hello'):
        if os.path.exists('C:\\hello\\test.txt'):
            with open('C:\\hello\\test.txt') as f1:
                print(f1.read())
                break
        else:
            with open('C:\\hello\\test.txt',mode='w') as fc:
                fc.write(str(os.listdir('c:\\')))
                continue
    else:
        os.mkdir('C:\\hello')
        continue
print('…………我是分割线…………')
# 读取csv文件数据
rcsv=GetCsvData()
try:
    rcsv.csv_file('c:\\test1.csv')
except Exception:
    raise Exception('error: file does not exists! ')
print('…………我是分割线…………')
#获取excel表数据
rxl=GetExcelData()
try:
    rxl.xlsx_file('c:\\test1.xlsx','Sheet')
except Exception:
    raise Exception('error: check the file_path and sheet_name.')
print('…………我是分割线…………')
#获取MySQL数据
ms=MysqlConnect()
ms.host='192.168.28.64'
ms.user='test'
ms.password='123456'
ms.database='test'
sql="select p.name,p.sex,p.age from person p;"
ms.msq_sql(sql)