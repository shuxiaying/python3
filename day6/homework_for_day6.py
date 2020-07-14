# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: homework_for_day6
# Author: TangJianjun
# Date: 2020/7/13
# Description:
#-----------------------------------------------------------------------------------
from CEM import WriteCsv,GetCsvData,WriteExcel,GetExcelData
# 写诗
wcsv=WriteCsv()
rcsv=GetCsvData()
dt='锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。'
dtl=[['锄禾日当午，'],['汗滴禾下土。'],['谁知盘中餐，'],['粒粒皆辛苦。']]
wcsv.csv_file('c:\\poetry.csv',dtl)
rcsv.csv_file('c:\\poetry.csv')
# 写歌
we=WriteExcel()
ge=GetExcelData()
song=[['两只老虎~ 两只老虎~'],['跑得快~ 跑得快~'],['一只没有眼睛~'],['一只没有耳朵~'],['真奇怪~ 真奇怪~']]
we.xlsx_file('c:\\song.xlsx',song)
ge.xlsx_file('c:\\song.xlsx','Sheet')
# 数据库操作
msq_cnt=MysqlConnect()
msq_cnt.host='192.168.28.64'
msq_cnt.user='test'
msq_cnt.password='123456'
msq_cnt.database='test'
sql='select * from person'
msq_cnt.msq_sql(sql)