# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: debug
# Author: TangJianjun
# Date: 2020/8/20
# Description:
#-----------------------------------------------------------------------------------
import datetime
import os
import random

# dy=str(datetime.datetime.today().date())
# print(type(dy),dy)
# num = random.randint(3, 4)
# print(num)
import tkinter as tk

import openpyxl

# wb = openpyxl.load_workbook("./花名册.xlsx")
# get_sheet = wb["Sheet1"]
# list_data = []
# first_row = True
# for row in get_sheet:
#     if first_row:
#         first_row = False
#         continue
#     for lab in row:
#         list_data.append(lab.value)
#         break
# print(list_data)

# import tkinter as tk
#
# def new():
#     text.insert(tk.END,str(datetime.datetime.today().date()))
#     root.after(1000,new)
# root=tk.Tk()
# text=tk.Text(root)
# text.pack()
# root.after(1000,new)
# root.mainloop()
# def func1():
#     print(bt['text'])
#     bt['command']=func2
#     bt['text']='fun2'
#     bt.update()
# def func2():
#     print(bt['text'])
#     bt['command'] = func1
#     bt['text'] = 'fun1'
#     bt.update()
#
#
# root=tk.Tk()
# bt=tk.Button(root,text='fun1',command=func1)
# bt.pack()
# root.mainloop()
# 花名册文件路径
excel_file_path = "花名册.xlsx"
# 工作表名
excel_sheet = "Sheet1"
# 记录存储文件路径
file_path = "name_record.json"
# os.system("%s"%excel_file_path)
os.system("%s"%file_path)