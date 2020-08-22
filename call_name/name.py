# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: name
# Author: TangJianjun
# Date: 2020/7/9
# Description:
# -----------------------------------------------------------------------------------
import datetime
import json
import os
import random
import tkinter as tk

import openpyxl

# 花名册文件名
excel_file_path = "花名册.xlsx"
# 工作表名
excel_sheet = "Sheet1"
# 记录存储文件名
file_path = "name_record.json"


class Call_Name:
    # 私有化变量
    _namelist = None

    # 读取花名册
    def __init__(self):
        wb = openpyxl.load_workbook(excel_file_path)
        get_sheet = wb[excel_sheet]
        list_data = []
        first_row = True
        try:
            for row in get_sheet:
                # 忽略首行
                if first_row:
                    first_row = False
                    continue
                # 读取第一个单元格数据
                for lab in row:
                    list_data.append(lab.value)
                    break
        except:
            list_data=['空名单？']
        self._namelist = list_data

    # 初始化记录
    def _re_reset(self):
        # 记录使用日期
        dls = []
        dy = str(datetime.datetime.today().date())
        dls.append(dy)
        # 记录点名
        record = {}
        for i in self._namelist:
            record[i] = 0
        name_record = {"date": dls, "last_use": dy, "record": record}
        return name_record

    # 创建记录
    def mk_record(self):
        jf_dict = self._re_reset()
        with open(file=file_path, mode='w', encoding='utf-8') as jf:
            json.dump(jf_dict, jf, indent=2, sort_keys=True, ensure_ascii=False)

    # 读取记录
    def read_record(self):
        with open(file=file_path, mode='r', encoding='utf-8') as jf:
            jf_data = json.load(jf)
        return jf_data

    # 产生随机姓名
    def call_name(self):
        ll = len(self._namelist)
        num = random.randint(1, ll)
        call_name = self._namelist[num - 1]
        return call_name

    # 修改记录-----warning!!!
    def re_mod(self, name=None, re_date=None):
        jf_data = self.read_record()
        record = jf_data["record"]
        use_date = list(jf_data["date"])
        if name:
            v = record[name] + 1
            jf_data["record"][name] = v
        if re_date:
            use_date.append(re_date)
            jf_data["date"] = use_date
            jf_data["last_use"] = re_date
        with open(file=file_path, mode='w', encoding='utf-8') as jf:
            json.dump(jf_data, jf, indent=2, sort_keys=True, ensure_ascii=False)

    # 获取记录次数
    def re_times(self):
        times_list = []
        record = self.read_record()["record"]
        for k, v in record.items():
            times_list.append(v)
        return times_list  # 返回记录次数

    # 获取被点到成员记录次数
    def call_times(self, name):
        record = self.read_record()["record"]
        return record[name]


class ForGUI:
    # 初始化
    re_date = None

    def __init__(self):
        try:
            cname = Call_Name()
        except:
            msg["text"] = "未找到：%s" % excel_file_path
            msg.update()
        else:
            try:
                record = cname.read_record()  # 读取记录
            except:
                cname.mk_record()  # 读取异常则重新创建记录
                record = cname.read_record()
            self.re_date = record["date"]  # 获取使用日期记录
            # 每5天初始化一次记录
            if len(self.re_date) > 5:
                cname.mk_record()  # 重新创建记录

    # 开始点名，输出有效姓名：姓名对应记录不为最大次数
    def start(self):
        cname = Call_Name()
        times = cname.re_times()  # 获取记录次数
        max_times = max(times)  # 获取记录最大次数
        min_times = min(times)  # 获取记录最小次数
        td = str(datetime.datetime.today().date())  # 获取当前日期
        if not td in self.re_date:
            cname.re_mod(re_date=td)
        while True:
            name = cname.call_name()  # 产生随机姓名
            times = cname.call_times(name)  # 获取被点到成员记录次数
            if max_times != min_times:
                if times != max_times:
                    cname.re_mod(name=name)  # 修改记录
                    msg["text"] = name
                    msg.update()
                    break
                else:
                    continue
            else:
                cname.re_mod(name=name)  # 修改记录
                msg["text"] = name
                msg.update()
                break

    # 查看花名册
    def open_name_excel(self):
        try:
            os.system("start %s&exit" % excel_file_path)
        except:
            msg["text"]='\n未找到花名册╮(╯▽╰)╭\n'
            msg["font"] = ('', 18)
            msg.update()

    # 查看点名记录
    def open_record(self):
        try:
            os.system("start %s&exit" % file_path)
        except:
            msg["text"]='\n未找到点名记录╮(╯▽╰)╭\n'
            msg["font"] = ('', 18)
            msg.update()

    # 获取花名册名单
    def get_name_list(self):
        try:
            wb = openpyxl.load_workbook(excel_file_path)
            get_sheet = wb[excel_sheet]
        except:
            msg["text"] = "未找到：%s" % excel_file_path
            msg.update()
        else:
            list_data = []
            first_row = True
            for row in get_sheet:
                # 忽略首行
                if first_row:
                    first_row = False
                    continue
                # 读取第一个单元格数据
                for lab in row:
                    list_data.append(lab.value)
                    break
            return list_data


# 创建窗口
root = tk.Tk(className="点名工具")
# 设置窗口大小
setWidth = 300
setHeight = 180
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
MenuBar.add_command(label='查看名单', command=ForGUI().open_name_excel)
MenuBar.add_command(label='查看记录', command=ForGUI().open_record)
MenuBar.add_command(label='清空记录', command=Call_Name().mk_record)

# 将子菜单加入菜单栏中
m1.add_cascade(label='选项', menu=MenuBar)
m1.add_command(label='Exit', command=root.quit)
# 将菜单栏添加到窗口
root.config(menu=m1)
# 创建文本显示
f1 = tk.Frame(root, bd=1, height=150, width=200)
pass
f1.pack(pady=10)
msg = tk.Label(f1, text="\n别紧张(●ˇ∀ˇ●)\n", fg="green")  # 创建文本控件
msg.pack(pady=10)
msg["font"] = ('', 18)
f2 = tk.Frame(root)
f2.pack(pady=10)

# 循环随机显示花名册名单
name_list = ForGUI().get_name_list()


def info():
    t = random.randint(1, len(name_list))
    msg["font"] = ('', 44)
    msg["text"] = (name_list[t - 1])


def bt_listen():
    while bt["state"] == 'normal':
        bt['command'] = bt_start
        bt['text'] = "就决定是你了"
        root.after(500, info)
        bt.update()
        if bt['text'] == "开始":
            break


def bt_start():
    bt['command'] = bt_listen
    bt['text'] = "开始"
    fg = ForGUI()
    root.after(500, fg.start)
    bt.update()


# 创建开始按钮
bt = tk.Button(f2, text='开始点名喽', stat="normal", command=bt_listen, bd=4, width=20, font=18)
bt.pack()

root.mainloop()
