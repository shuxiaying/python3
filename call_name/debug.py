# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: debug
# Author: TangJianjun
# Date: 2020/8/20
# Description:
#-----------------------------------------------------------------------------------
import datetime
import random

# dy=str(datetime.datetime.today().date())
# print(type(dy),dy)
# num = random.randint(3, 4)
# print(num)
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

stat = datetime.datetime.now().time()
def info():
    new_stat = datetime.datetime.now().time()
    if stat.__eq__(new_stat):
        print("True")
    else:
        print("False")
info()