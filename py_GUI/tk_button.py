# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: tk_button
# Author: TangJianjun
# Date: 2020/8/4
# Description:
#-----------------------------------------------------------------------------------
import random
import tkinter as tk

name_list = ['唐建军', '孙家耀', '张辛碧', '宋羽']
root=tk.Tk(className='Python tkinter button')#创建窗口
f1=tk.Frame(root)#创建frame框架
f2=tk.Frame(root,width=100)

i = random.randint(0, 3)
msg = tk.Label(f2, text=name_list[i], font=14)  # 创建文本控件
def call():
    global msg
    i = random.randint(0, 3)
    msg = tk.Label(f2, text=name_list[i], font=14)  # 创建文本控件
    msg.pack()

def start_call():
    msg.forget()
    call()

bt1=tk.Button(f2,text='start',command=start_call,bd=4,width=20,font=14)#开始
bt1.pack(pady=10)
f2.pack(padx=100)
f1.pack(pady=50)

root.mainloop()
