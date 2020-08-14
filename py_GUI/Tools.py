# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: Tools
# Author: TangJianjun
# Date: 2020/8/11
# Description:
# -----------------------------------------------------------------------------------
import datetime
import os
import tkinter as tk


class MyTools:
    def __init__(self):
        now_date = datetime.datetime.today().date()
        # 检查日志文件
        try:
            # 获取日志所有行
            with open('./start.log', mode='r', encoding='utf-8') as lf:
                contents = lf.readlines()  # 以列表形式返回每行内容（上一行以‘\n’结尾）
            #生成今日启动日志
            with open('./start.log', mode='r', encoding='utf-8') as lf:
                all_txt = lf.read()#读取所有内容，返回字符串
            if not str(now_date) in all_txt:
                with open('./start.log', mode='a', encoding='utf-8') as lf:
                    today_log='\n'+str(now_date)
                    lf.write(today_log)
            # 总行数大于1000行则删除包含第一行内容的行
            try:
                assert len(contents) < 1000
            except:
                # 获取第一行内容，一般为日期：xxxx-xx-xx
                with open('./start.log', mode='r', encoding='utf-8') as lf:
                    first_line = lf.readline(-1)
                    first_line = str(first_line)[:first_line.find('\n')]  # 去除换行符‘\n’
                # 遍历每行内容，不包含第一行内容或不为空行则重新写入
                with open('./start.log', mode='w', encoding='utf-8') as lf:
                    for i in contents:
                        if not first_line in i and i != '\n':
                            lf.write(i)
        except:
            # 如文件不存在则重新创建文件
            with open('./start.log', mode='w', encoding='utf-8') as lf:
                lf.write(str(now_date))

    # 生成日志
    def _make_logs(self, msg):
        now_time = datetime.datetime.now()
        contents = '\n' + str(now_time) + ': ' + msg
        with open('./start.log', mode='a', encoding='utf-8') as lf:
            lf.write(contents)

    def ranzi(self):
        os.system('C:\\ranzi\\xampp\\ranzi.bat')
        self._make_logs('C:\\ranzi\\xampp\\ranzi.bat')

    def fiddler(self):
        os.system('C:\\Fiddler\\Fiddler\\Fiddler.bat')
        self._make_logs('C:\\Fiddler\\Fiddler\\Fiddler.bat')

    def jmeter(self):
        os.system('start jmeter.bat')
        self._make_logs('cd C:\\jmeter\\apache-jmeter-5.2.1\\bin & jmeter.bat')

    def webtours(self):
        os.system('start webtours.bat')
        self._make_logs('cd c:\\WebTours & StartServer.bat')

    def terminal(self):
        os.system('start cd C:\\Users\\Administrator')
        self._make_logs('start cd C:\\Users\\Administrator')

    def screen_shot(self):
        os.system('start C:\\Windows\\system32\\SnippingTool.exe')
        self._make_logs('start C:\\Windows\\system32\\SnippingTool.exe')

    def Calculater(self):
        os.system('calc')
        self._make_logs('calc')

    def local_events(self):
        os.system('start C:\\Windows\\system32\\eventvwr.exe')
        self._make_logs('start C:\\Windows\\system32\\eventvwr.exe')

    def open_logs(self):
        os.system('start.log')


#生成启动日志
MyTools()._make_logs("start using......")

# 创建窗口
root = tk.Tk(className='SetUp Tool')
# 设置窗口大小
setWidth = 250
setHeight = 220
# 获取屏幕分辨率
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = int((screenWidth - setWidth) / 2)
y = int((screenHeight - setHeight) / 2)
# 设置窗口初始位置屏幕居中
root.geometry("%sx%s+%s+%s" % (setWidth, setHeight, x, y))
# 设置窗口宽高固定
root.resizable(0, 0)
# 创建菜单栏
m1 = tk.Menu(root, tearoff=False)

# 创建子菜单，不显示分窗
MenuBar = tk.Menu(m1, tearoff=False)
MenuBar.add_command(label='Terminal', command=MyTools().terminal)
MenuBar.add_command(label='ScreenShot', command=MyTools().screen_shot)
MenuBar.add_command(label='Calculator', command=MyTools().Calculater)
MenuBar.add_command(label='Local_Events', command=MyTools().local_events)
# 将子菜单加入菜单栏中
m1.add_cascade(label='SystemTools', menu=MenuBar)

m1.add_command(label='Logs', command=MyTools().open_logs)
# 将菜单栏添加到窗口
root.config(menu=m1)

f1 = tk.Frame(root, width=40)
f2 = tk.Frame(f1, width=40)
f3 = tk.Frame(f1, width=40)
f4 = tk.Frame(f1, width=40)
f5 = tk.Frame(f1, width=40)
f6 = tk.Frame(f1, width=40)

lable1 = tk.Label(f1, text="Welcome to using the fast setup tool~", font=14)
lable1.pack(padx=8)

bt1 = tk.Button(f2, text='System of ranzi ', command=MyTools().ranzi, bd=3, font=14, width=18)
bt2 = tk.Button(f3, text='Fiddler v5.4', command=MyTools().fiddler, bd=3, font=14, width=18)
bt3 = tk.Button(f4, text='JMeter 5.2.1', command=MyTools().jmeter, bd=3, font=14, width=18)
bt4 = tk.Button(f5, text='Web Tours 1.0', command=MyTools().webtours, bd=3, font=14, width=18)
bt5 = tk.Button(f6, text='Exit', command=root.quit, bd=3, font=14, width=18)

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
