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
import random
import tkinter as tk

import openpyxl


class Call_Name:
    # 私有化变量
    _namelist = None
    # 花名册文件路径
    _excel_file_path = r"./花名册.xlsx"
    # 记录存储文件路径
    _file_path = r"./name_record.json"

    # 读取花名册
    def __init__(self):
        wb = openpyxl.load_workbook(self._excel_file_path)
        get_sheet = wb["Sheet1"]
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
        name_record = {"date": dls, "last_use": dy, "record": record,"stat":0}
        return name_record

    # 创建记录
    def mk_record(self):
        jf_dict = self._re_reset()
        with open(file=self._file_path, mode='w', encoding='utf-8') as jf:
            json.dump(jf_dict, jf, indent=2, sort_keys=True, ensure_ascii=False)

    # 读取记录
    def read_record(self):
        with open(file=self._file_path, mode='r', encoding='utf-8') as jf:
            jf_data = json.load(jf)
        return jf_data

    # 产生随机姓名
    def call_name(self):
        ll = len(self._namelist)
        num = random.randint(1, ll)
        call_name = self._namelist[num - 1]
        return call_name

    # 修改记录-----warning!!!
    def re_mod(self, name=None, re_date=None,stat=None):
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
        if stat:
            jf_data["stat"]=stat
        with open(file=self._file_path, mode='w', encoding='utf-8') as jf:
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
    _cname=None
    _re_date=None
    def __init__(self):
        try:
            cname = Call_Name()
        except:
            print("未找到文件：./花名册.xlsx")
        else:
            try:
                record = cname.read_record()  # 读取记录
            except:
                cname.mk_record()  # 读取异常则重新创建记录
                record = cname.read_record()
            self._re_date=record["date"]  # 获取使用日期记录
            # 每5天初始化一次记录
            if len(self._re_date) > 5:
                cname.mk_record()  # 重新创建记录
        self._cname=cname
    # 开始点名，输出有效姓名：姓名对应记录不为最大次数
    def start(self):
        times = self._cname.re_times()  # 获取记录次数
        max_times = max(times)  # 获取记录最大次数
        min_times = min(times)  # 获取记录最小次数
        td = str(datetime.datetime.today().date())  # 获取当前日期
        if not td in re_date:
            self._cname.re_mod(re_date=td)
        while True:
            name = self._cname.call_name()  # 产生随机姓名
            times = self._cname.call_times(name)  # 获取被点到成员记录次数
            if max_times != min_times:
                if times < max_times:
                    self._cname.re_mod(name=name)  # 修改记录
                    return name
                else:
                    continue
            else:
                self._cname.re_mod(name=name)  # 修改记录
                return name

    # 查看花名册
    def open_name_excel(self):
        pass

    # 查看点名记录
    def open_record(self):
        pass


    # 获取花名册名单
    def get_name_list(self):
        try:
            file_path = Call_Name()._excel_file_path
        except:
            return "未找到花名册"
        else:
            wb = openpyxl.load_workbook(file_path)
            get_sheet = wb["Sheet1"]
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

    # 获取按钮状态
    def get_stat(self):
        record=self._cname.read_record()
        return record["stat"]
    # 修改按钮状态
    def mod_stat(self,n):
        self._cname.re_mod(stat=n)

# 创建窗口
root = tk.Tk(className="点名工具")
# 设置窗口大小
setWidth = 300
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
MenuBar.add_command(label='花名册', command=open_name_excel)
MenuBar.add_command(label='点名记录', command=open_record)
# 将子菜单加入菜单栏中
m1.add_cascade(label='查看', menu=MenuBar)
m1.add_command(label='Exit', command=root.quit)
# 将菜单栏添加到窗口
root.config(menu=m1)
# 创建文本显示
f1 = tk.Frame(root, bd=1, height=100, width=200)
f1.pack(pady=10)
v = tk.StringVar()  # 创建变量
v.set("别紧张")
msg = tk.Label(f1, textvariable=v, font=('', 48), fg="green")  # 创建文本控件
msg.pack()
f2 = tk.Frame(root)
f2.pack(pady=20)
# 创建开始按钮
w = tk.StringVar()  # 创建变量
w.set("开始点名喽")

# 循环随机显示花名册名单
name_list=get_name_list()
def info():
    t = random.randint(1, len(name_list))
    v.set(name_list[t - 1])
    msg.after(500, info)

stat = datetime.datetime.now().time()
def bt_func():
    m=get_stat()
    if m==0:
        root.after(500, info)
        w.set("就决定是你了")
    else:
        root.after_cancel(1)
        name = start()
        v.set(name)
        w.set("开始")
bt = tk.Button(f2, textvariable=w, command=bt_func, bd=4, width=20, font=14)
bt.pack()
root.mainloop()
