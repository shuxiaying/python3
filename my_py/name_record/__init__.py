# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: __init__.py
# Author: TangJianjun
# Date: 2020/7/15
# Description:
#-----------------------------------------------------------------------------------
import openpyxl
from openpyxl import Workbook
#获取excel表数据
class GetExcelData:
    def xlsx_file(self,filepath,sheet_name):
        global get_wb
        try:
            get_wb = openpyxl.load_workbook(filepath)
        except Exception:
            raise Exception('The file does not exists!')
        try:
            get_sheet = get_wb[sheet_name]
        except Exception:
            raise Exception('error: check the sheet name. ')
        try:
            for get_tuple in get_sheet:
                for get_cell in get_tuple:
                    print(get_cell.value, end='\t')
                print()
        except Exception:
            raise Exception('The sheet maybe empty.')
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