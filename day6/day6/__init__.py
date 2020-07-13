# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: day6
# Author: TangJianjun
# Date: 2020/7/13
# Description:
#-----------------------------------------------------------------------------------
# 递归函数
sum_ls=0
def ls_sum(list):
    for i in list:
        if type(i)==int:
            global sum_ls
            sum_ls +=i
        elif type(i) ==str:
            print(i,'format error')
            pass
        else:
            return ls_sum(i)
    return sum_ls
# 条件代码入口
if __name__ == '__main__':
    # print(ls_sum([1, 2, 3, '2', [1, 2]]))
    class Person_d6:
        name='Tom'
        _age=18
        __num='086***21'
        def spk_name(self):
            print('I\'m %s.'%self.name)
        def _spk_age(self):
            print('I\'m %d years old.'%self._age)
        def __spk_num(self):
            print('My tel-number is %s'%self.__num)
if __name__ == '__main__':
    tom=Person_d6()
    # print(dir(tom))
    # tom._Person__spk_num()#强行调用私有变量与方法
#打开文件
dta=open('C:\\test1.csv',mode='r')#r 只读，w 重写，a 追加
# print(dta)
# 使用循环获取数据
# for i in dta:
#     print(i,end='')
# # 对文件操作后，需要关闭文件
# dta.close()
# 导入csv获取数据
import csv
## 以列表形式读取
# dta2=csv.reader(dta)
# for i in dta2:
#     if i[0]!='name':
#         print('%s, %s， %s岁'%(i[0],i[2],i[1]))
# dta.close()
## 以字典形式读取
# dta3=csv.DictReader(dta)
# for i in dta3:
#     print('%s, %s， %s岁'%(i['name'],i['sex'],i['age']))
dta.close()
##使用‘with open as 对象’结构打开文件，不需要单独写关闭语句，结构运行完自动关闭
# with open('C:\\test1.csv',mode='r') as dt:
#     gt=csv.DictReader(dt)
#     for i in gt:
#         print('%s, %s， %s岁' % (i['name'], i['sex'], i['age']))
# 封装与注释
class Get_Csv_Data:
    def csv_file(self,file_path):
        """
        Getting the data from csv file, display with dict
        :param file_path:
        :return:
        """
        with open(file_path,mode='r') as f:
            f=csv.DictReader(f)
            for i in f:
                return i
# 写文件
if __name__ == '__main__':
    with open('c:\\test2.csv',mode='w',newline='') as f:
        wf=csv.writer(f)
        wf.writerow(['name','age','sex'])
        data=[['小丽','10','女'],['小李','12','男'],['小力','9','男']]
        for i in data:
            wf.writerow(i)
# 覆盖文件写入
class Write_csv:
    def csv_file(self,filepath,data):
        """
        Writing data into the file,truncating the file first
        :param filepath:
        :param data:
        :return:
        """
        with open(filepath,mode='w',newline='') as f:
            f=csv.writer(f)
            for i in data:
                f.writerow(i)
#末尾追加写入
class Append_csv:
    def csv_file(self,filepath,data):
        """
        Appending to the end of the file if it exists
        :param filepath:
        :param data:
        :return:
        """
        with open(filepath,mode='a',newline='') as f:
            f=csv.writer(f)
            for i in data:
                f.writerow(i)

