# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: tk_destory
# Author: TangJianjun
# Date: 2020/8/4
# Description:
#-----------------------------------------------------------------------------------
import tkinter as tk

root=tk.Tk(className='destory')
lb=tk.Label(root,text='测试',font=24)
lb.pack(padx=20,pady=10)

def sh():
    lb.pack(padx=20,pady=10)
def des():
    lb.forget()
    sh()
bt=tk.Button(root,text="start",command=des)
bt.pack()

root.mainloop()
