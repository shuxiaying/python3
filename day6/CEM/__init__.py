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
class GetCsvData:
    def csv_file(self,file_path):
        """
        Getting the data from csv file, display with dict
        :param file_path:
        :return:
        """
        with open(file_path,mode='r') as f:
            f=csv.reader(f)
            for i in f:
                print(i[0])

# 覆盖文件写入
class WriteCsv:
    def csv_file(self,filepath,data):
        """
        Writing data into the file,truncating the file first
        :param filepath:
        :param data:
        :return:
        """
        with open(filepath,mode='w',newline='') as f:
            f=csv.writer(f)
            for i in data:
                f.writerow(i)
#末尾追加写入
class AppendCsv:
    def csv_file(self,filepath,data):
        """
        Appending to the end of the file if it exists
        :param filepath:
        :param data:
        :return:
        """
        with open(filepath,mode='a',newline='') as f:
            f=csv.writer(f)
            for i in data:
                f.writerow(i)
# 向excel表写入数据
class WriteExcel:
    def xlsx_file(self,filepath,data):
        """
        Appending data to te end of excel file, if file is not exist.
        :param filepath:
        :param data:
        :return:
        """
        wb = Workbook()
        ws = wb.active  # 获取文件当前活动sheet
        for i in data:
            ws.append(i)
        wb.save(filepath)
#获取excel表数据
class GetExcelData:
    def xlsx_file(self,filepath,sheet_name):
        get_wb = openpyxl.load_workbook(filepath)
        get_sheet = get_wb[sheet_name]
        for get_tuple in get_sheet:
            for get_cell in get_tuple:
                print( get_cell.value)
        print()
#获取MySQL数据
class MysqlConnect:
    host = 'host'
    port = 3306
    user = 'user'
    password = 'password'
    database = 'database'
    charset = 'utf8'
    def msq_sql(self,sql):
        global my_cnt
        try:
            my_cnt = pymysql.connect(host=self.host,
                                 port=self.port,
                                 user=self.user,
                                 password=self.password,
                                 database=self.database,
                                 charset=self.charset)
        except Exception:
           Exception("Database connect fail, check the value of host, user, password, database and port")
        my_data = my_cnt.cursor()
        try:
            my_data.execute(sql)
            my_cnt.commit()
        except Exception:
            Exception('ERROR 1064 (42000): You have an error in your SQL syntax; '
                  'check the manual that corresponds to your MySQL server '
                  'version for the right syntax to use near \'',sql,'\' at line 1')
        get_data = my_data.fetchall()
        for i in get_data:
            for t in i:
                print(t,end='\t')
            print('\r')
        my_cnt.close()