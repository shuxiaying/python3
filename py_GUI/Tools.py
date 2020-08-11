# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: Tools
# Author: TangJianjun
# Date: 2020/8/11
# Description:
#-----------------------------------------------------------------------------------
import os
import tkinter as tk
def ranzi():
    os.system('C:\\ranzi\\xampp\\ranzi.bat')
def fiddler():
    os.system('C:\\Fiddler\\Fiddler\\Fiddler.bat')
def jmeter():
    os.system('C:\\jmeter\\apache-jmeter-5.2.1\\bin\\jmeter.bat')
def webtours():
    os.system('C:\\Web Tours 1.0\\StartServer.bat')
root=tk.Tk(className='快捷启动工具')
f1=tk.Frame(root,width=40)
f2=tk.Frame(f1,width=40)
f3=tk.Frame(f1,width=40)
f4=tk.Frame(f1,width=40)
f5=tk.Frame(f1,width=40)
f6=tk.Frame(f1,width=40)

lable1=tk.Label(f1,text="欢迎使用快捷启动工具~",font=14)
lable1.pack(padx=8)

bt1=tk.Button(f2,text='然之系统',command=ranzi,bd=3,font=14,width=18)
bt2=tk.Button(f3,text='Fiddler v5.4',command=fiddler,bd=3,font=14,width=18)
bt3=tk.Button(f4,text='JMeter 5.2.1',command=jmeter,bd=3,font=14,width=18)
bt4=tk.Button(f5,text='Web Tours 1.0',command=webtours,bd=3,font=14,width=18)
bt5=tk.Button(f6,text='退出',command=root.quit,bd=3,font=14,width=18)

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()
bt5.pack()

f1.pack(pady=6)
f2.pack(pady=4)
f3.pack(pady=4)
f4.pack(pady=4)
f5.pack(pady=4)
f6.pack(pady=4)

root.mainloop()