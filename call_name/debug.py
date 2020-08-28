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
import tkinter as tk

import openpyxl
import pyttsx3

pass
# dy=str(datetime.datetime.today().date())
# print(type(dy),dy)
# num = random.randint(3, 4)
# print(num)


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
# f1 = tk.Frame(root, bd=1, height=150, width=300)
# f1.pack(pady=10)
# def sp_unchecked():
#     sp_bt["command"]=0
# def sp_checked():
#     sp_bt["command"]=sp_unchecked
# # 创建语音播报开关
# sp_bt=tk.Checkbutton(f1,text="语音播报",font=('',10),justify="right",command=sp_unchecked)
# sp_bt.pack()
# # bt=tk.Button(root,text='fun1',command=func1)
# # bt.pack()
# root.mainloop()
# 花名册文件路径
# excel_file_path = "花名册.xlsx"
# # 工作表名
# excel_sheet = "Sheet1"
# # 记录存储文件路径
# file_path = "name_record.json"
# # os.system("%s"%excel_file_path)
# os.system("%s"%file_path)

# dict1={
#     "刘婷婷": 1,
#     "唐建军": 1,
#     "孙家耀": 0,
#     "宋羽": 0
#   }
# keys=[]
# keys.extend(dict1.keys())
# keys=random.choice(keys)
# print(keys)
# namelist=['刘婷婷', '唐建军', '孙家耀', '宋羽', '廖智强', '张辛壁', '曾世华', '梁羽岑', '石曹山', '胡家瑞', '陈奕宏']
# try:
#     assert keys==namelist
# except:
#     keys=set(keys)
#     namelist=set(namelist)
#     print(keys-namelist)
#     print(namelist-keys)
name='张三'
new=''
song='123456789876543212345678987654323456789987654334567890765432345678909876543212345678909765432'
for i in song:
    new+=(i+',')
print(new)
eng = pyttsx3.init()
# eng.say('If never see you again, good morning and good night!')
# eng.say(new)
eng.say(song)
eng.runAndWait()
# eng.stop()