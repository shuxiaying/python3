# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: py_frame
# Author: TangJianjun
# Date: 2020/8/4
# Description:
#-----------------------------------------------------------------------------------
import random
import tkinter as tk

class Call_Name:
    name = None
    root = tk.Tk(className='Python 点名小程序')
    def call_name(self):
        name_list=['唐建军','孙家耀','张辛碧','宋羽']
        i=random.randint(0,3)
        return name_list[i]

    def new_call(self):
        self.root.destroy()
        self.root.quit()

    def start_call(self):
        frame1 = tk.Frame(self.root, height='30', width='200')
        frame2 = tk.Frame(self.root, height='30', width='200')
        frame3 = tk.Frame(self.root, height='100', width='200')
        for i in range(1,4):
            name=self.call_name()
        nm = tk.Label(frame3, text=self.name,font='44')
        nm.pack()
        label1 = tk.Label(frame1, text="开始点名", justify=tk.LEFT, font='24')
        label1.pack(side=tk.LEFT)
        hi = tk.Button(frame2, text='start', command=self.new_call, font='24')
        hi.pack()
        frame1.pack(padx=10, pady=10)
        frame2.pack(padx=10, pady=10)
        frame3.pack(padx=10, pady=40)
        self.root.mainloop()