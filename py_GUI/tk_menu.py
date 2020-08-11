# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: tk_menu
# Author: TangJianjun
# Date: 2020/8/11
# Description:
#-----------------------------------------------------------------------------------

import tkinter as tk

def ec():
    print('ranzi')
root=tk.Tk(className='快速启动工具')
f1=tk.Frame(root,height='30', width='200')
m1=tk.Menu(f1)
m1.add_command(label='然之系统',command=ec)
m1.add_command(label='然之系统',command=ec)
m1.add_command(label='然之系统',command=ec)
root.config(menu=m1)
f1.pack(padx=10,pady=20)
root.mainloop()
