# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: call_name
# Author: TangJianjun
# Date: 2020/8/4
# Description:
#-----------------------------------------------------------------------------------
import datetime
import json
import random

import openpyxl


class CallName:
    _name_list=None
    def __init__(self,eccel_file=r'.\\name.xlsx',sheet_name='Sheet1'):
        '''
        :description:获取花名册
        :param eccel_file: excel文件路径
        :param sheet_name:excel工作表表名
        '''
        get_wb=openpyxl.load_workbook(eccel_file)
        get_sheet = get_wb[sheet_name]
        first_row=True
        name_list=[]
        for get_row in get_sheet:
            if first_row:
                first_row = False
                continue
            for get_cell in get_row:
                name_list.append(get_cell.value)
        self._name_list=name_list
    def call_name(self):
        i=random.randint(0,len(self._name_list)-1)
        name=self._name_list[i]
        return name
    def set_records(self,record=r'.\\record.json'):
        '''
        :description:创建并初始化记录
        :param record: 文件存储路径
        :return:
        '''
        tm = datetime.datetime.now().date()
        name_dict={"日期":str(tm)}
        for i in self._name_list:
            name_dict[i]=0
        with open(record,mode='w',encoding='utf-8') as jf:
            json.dump(name_dict, jf, indent=2, sort_keys=True, ensure_ascii=False)
    def read_records(self,record=r'.\\record.json'):
        '''
        :description:读取记录
        :param record:
        :return:
        '''
        with open(record,mode='r',encoding='utf-8') as jf:
            records=json.load(jf)
        return records
    def update_records(self,record=r'.\\record.json',**new_dict):
        old_date=self.read_records()
        for k,v in new_dict.items():
            old_date[k]=v
        with open(record,mode='w',encoding='utf-8') as jf:
            json.dump(old_date, jf, indent=2, sort_keys=True, ensure_ascii=False)

    def max_call_times(self):
        dta=self.read_records()
        del dta['日期']
        s = None
        lv=[]
        for k in dta:
            v = dta[k]
            lv.append(v)
            if s < v:
                s, v = v, s
            else:
                continue
        ck=list(set(list(lv)))
        if len(ck)==1:
            s='equal'
        return s

    def start_call(self):
        record=None
        while 1:
            try:
                record=self.read_records()
            except:
                self.set_records()
                continue
            last_call = datetime.datetime.strptime(record['日期'],'%Y-%m-%d')
            name=self.call_name()
            dt1=last_call+datetime.timedelta(days=7)
            dnow=datetime.datetime.today().date()
            if dnow.__ge__(dt1):
                self.set_records()
                continue

            max_call = self.max_call_times()
            if record[name]!=max_call and max_call != 0:
                return name
            else:
                continue



if __name__ == '__main__':
    cn=CallName()
    # cn.set_records()
    # print(cn.read_records())
    # str1='2020-07-30'
    # dt1=datetime.datetime.strptime(str1,'%Y-%m-%d')
    # dt1=dt1+datetime.timedelta(days=7)
    # dt2=datetime.datetime.today().date()
    # if dt2.__ge__(dt1):
    #     print('hh')
    # else:
    #     print(dt2)

