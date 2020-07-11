# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: count_py
# Author: TangJianjun
# Date: 2020/7/11
# Description:
#-----------------------------------------------------------------------------------
class count_fun:
    def im_sum(self,a,b):
        print(a,'+',b,'=',a+b)
    def im_sub(self,a,b):
        print(a,'-',b,'=',a-b)
    def pro_duct(self,a,b):
        print(a,'*',b,'=',a*b)
    def di_vision(self,a,b):
        print(a,'/',b,'=',a/b)
    def zh_chu(self,a,b):
        print(a,'//',b,'=',a//b)
    def qiu_yu(self,a,b):
        print(a,'%',b,'=',a % b)
    def qiu_mi(self,a,b):
        print(a,'**',b,'=',a ** b)
count=count_fun()
print('支持两个数的加+、减-、乘*、除/、整除//、求余%、幂**运算\n格式如：a*b，输入exit退出程序 ')
ask=input('点击Enter开始')
while ask !='exit':
    ask = input('请输入：')
    jia=ask.find('+')
    jan=ask.find('-')
    ch=ask.find('*')
    chu=ask.find('/')
    zc=ask.find('//')
    qy=ask.find('%')
    mi=ask.find('**')
    #加法
    if jia != -1:
        a=ask[:jia]
        b=ask[jia+1::]
        try:
            int(a)
            int(b)
        except:
            ask=input('格式错误，请重新输入：')
        else:
            a=int(a)
            b=int(b)
            count.im_sum(a, b)
            continue
    #减法
    elif jan != -1:
        a=ask[:jan]
        b=ask[jan+1::]
        try:
            int(a)
            int(b)
        except:
            ask=input('格式错误，请重新输入：')
        else:
            a=int(a)
            b=int(b)
            count.im_sub(a, b)
            continue
    #幂
    elif mi != -1:
        a = ask[:mi]
        b = ask[mi + 2::]
        try:
            int(a)
            int(b)
        except:
            ask = input('格式错误，请重新输入：')
        else:
            a = int(a)
            b = int(b)
            count.qiu_mi(a, b)
            continue
    #整除
    elif zc != -1:
        a = ask[:zc]
        b = ask[zc + 2::]
        try:
            int(a)
            int(b)
        except:
            ask = input('格式错误，请重新输入：')
        else:
            a = int(a)
            b = int(b)
            count.zh_chu(a, b)
            continue
    #乘法
    elif ch != -1:
        a = ask[:ch]
        b = ask[ch + 1::]
        try:
            int(a)
            int(b)
        except:
            ask = input('格式错误，请重新输入：')
        else:
            a = int(a)
            b = int(b)
            count.pro_duct(a, b)
            continue
    # 除法
    elif chu != -1:
        a = ask[:chu]
        b = ask[chu + 1::]
        try:
            int(a)
            int(b)
        except:
            ask = input('格式错误，请重新输入：')
        else:
            a = int(a)
            b = int(b)
            count.di_vision(a, b)
            continue
    # 求余
    elif qy != -1:
        a = ask[:qy]
        b = ask[qy + 1::]
        try:
            int(a)
            int(b)
        except:
            ask = input('格式错误，请重新输入：')
        else:
            a = int(a)
            b = int(b)
            count.qiu_yu(a, b)
            continue
    else:
        print('暂不支持此类运算')
        break