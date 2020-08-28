# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: config
# Author: TangJianjun
# Date: 2020/8/27
# Description:
# -----------------------------------------------------------------------------------
import datetime
import json
import random
import openpyxl


class CallNameDriver:
    # 花名册文件名
    excel_file_path = "花名册.xlsx"
    # 工作表名
    excel_sheet = "Sheet1"
    # 记录存储文件名
    file_path = "name_record.json"

    # 读取花名册
    def __init__(self):
        wb = openpyxl.load_workbook(self.excel_file_path)
        get_sheet = wb[self.excel_sheet]
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
            list_data = ['空名单？']
        self.namelist = list_data

    # 初始化记录
    def _re_reset(self):
        # 记录使用日期
        dy = str(datetime.datetime.today().date())
        # 记录点名
        record = {}
        for i in self.namelist:
            record[i] = 0
        name_record = {"date": [dy], "last_use": dy, "record": record}
        return name_record

    # 创建记录
    def mk_record(self):
        jf_dict = self._re_reset()
        with open(file=self.file_path, mode='w', encoding='utf-8') as jf:
            json.dump(jf_dict, jf, indent=2, sort_keys=True, ensure_ascii=False)

    # 读取记录
    def read_record(self):
        with open(file=self.file_path, mode='r', encoding='utf-8') as jf:
            jf_data = json.load(jf)
        return jf_data

    # 获取记录的key
    def get_keys(self):
        record = self.read_record()["record"]
        keys = []
        keys.extend(record.keys())
        return keys

    # 产生随机姓名
    def call_name(self):
        call_name = random.choice(self.namelist)
        return call_name

    # 获取记录次数
    def re_times(self):
        times_list = []
        record = self.read_record()["record"]
        times_list.extend(record.values())
        return times_list  # 返回记录次数

    # 获取被点到成员记录次数
    def call_times(self, name):
        record = self.read_record()["record"]
        return record[name]

    # 修改记录-----warning!!!
    def re_mod(self, name=None, re_date=None, new_add=None, new_del=None):
        jf_data = self.read_record()
        # 如花名册有修改，则修改对应记录，默认次数为最小次数
        if new_add:
            min_times = min(self.re_times())
            for i in new_add:
                jf_data["record"][i] = min_times
        if new_del:
            for i in new_del:
                del jf_data["record"][i]
        # 有效点名，对应记录+1
        if name:
            jf_data["record"][name] += 1
        # 更新记录日期
        if re_date:
            jf_data["date"].append(re_date)
            jf_data["last_use"] = re_date
        with open(file=self.file_path, mode='w', encoding='utf-8') as jf:
            json.dump(jf_data, jf, indent=2, sort_keys=True, ensure_ascii=False)
