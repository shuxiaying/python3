# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: py_if_for_while
# Author: TangJianjun
# Date: 2020/7/8
# Description:Notes for Python project of if,while and for, day 3th.
#-----------------------------------------------------------------------------------
#if语句
"""
if 条件 :
    [True]
else:
    [False]
"""
# num1=int(input("请输入第一个整数："))
# num2=int(input("请输入第二个整数："))
# if num1 == num2:
#     print(num1,"=",num2)
# else:
#     if num1>num2:
#         print(num1,">",num2)
#     else:
#         print(num1, "<", num2)
#if的三元运算：print(True if语句 False)
# year=int(input("请输入年份:"))
# print("闰年" if (year%4==0 and year%100!=0) or year%400==0 else "平年" )
# if year%100==0:
#     if year%400==0:
#         print("闰年")
#     else:
#         print("平年")
# else:
#     if year%4==0:
#         print("闰年")
#     else:
#         print("平年")
# print("闰年" if year%400==0 else "平年" if year%100==0 else "闰年" if year%4==0 else "平年")
i,s=0,0
while i <= 100:
    s+=i
    i+=1
else:
    print(s)
