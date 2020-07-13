# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: csv_file
# Author: TangJianjun
# Date: 2020/7/13
# Description:
#-----------------------------------------------------------------------------------
from day6 import Get_Csv_Data,Write_csv, Append_csv
#读文件
rf= Get_Csv_Data()
#写文件-覆盖
wf= Write_csv()
#写文件-追加
af= Append_csv()
fp='c:\\test3.csv'
fd=[['name','age','sex'],['Tom','18','boy'],['Jack','19','boy']]
# wf.csv_file(fp,fd)
# rf.csv_file(fp)
# fd2=[['Jully','17','girl']]
# af.csv_file(fp,fd2)
# rf.csv_file(fp)
