# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: csv_excel_mysql
# Author: TangJianjun
# Date: 2020/7/13
# Description:
#-----------------------------------------------------------------------------------
import csv
import openpyxl
from openpyxl import Workbook
import pymysql
# 读取csv文件数据
class Get_Csv_Data:
    def csv_file(self,file_path):
        """
        Getting the data from csv file, display with dict
        :param file_path:
        :return:
        """
        with open(file_path,mode='r',encoding='utf8') as f:
            f=csv.DictReader(f)
            for i in f:
                return i

# 覆盖文件写入
class Write_csv:
    def csv_file(self,filepath,data):
        """
        Writing data into the file,truncating the file first
        :param filepath:
        :param data:
        :return:
        """
        with open(filepath,mode='w',newline='',encoding='utf8') as f:
            f=csv.writer(f)
            for i in data:
                f.writerow(i)
#末尾追加写入
class Append_csv:
    def csv_file(self,filepath,data):
        """
        Appending to the end of the file if it exists
        :param filepath:
        :param data:
        :return:
        """
        with open(filepath,mode='a',newline='',encoding='utf8') as f:
            f=csv.writer(f)
            for i in data:
                f.writerow(i)
#操作excel文件
wb=Workbook()
ws=wb.active#获取文件当前活动sheet
# 向excel表写入数据
class Write_Excel:
    def xlsx_file(self,filepath,data):
        """
        Appending data to te end of excel file, if file is not exist.
        :param filepath:
        :param data:
        :return:
        """
        for i in data:
            ws.append(i)
        wb.save(filepath)
#获取excel表数据
class Get_Excel_Data:
    def xlsx_file(self,filepath,sheet_name):
        get_wb = openpyxl.load_workbook(filepath)
        get_sheet = get_wb[sheet_name]
        for get_tuple in get_sheet:
            for get_cell in get_tuple:
                print( get_cell.value,end='')
        print()
#获取MySQL数据
class Mysql_Connect():
    my_cnt=pymysql.connect(host=host,
                    port=port,
                    user=user,
                    password=password,
                    database='test',
                    charset='utf8')
    my_data = my_cnt.cursor()
    def msq_sql(self,sql):
        my_data.execute(sql)
        my_cnt.commit()
        get_data = my_data.fetchall()
        print(get_data)
        my_cnt.close()