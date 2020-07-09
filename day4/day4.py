# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: day4
# Author: TangJianjun
# Date: 2020/7/9
# Description:
#-----------------------------------------------------------------------------------
#range(n1,n2,【step】) ,在范围 [n1,n2) 以步长为step取值
list1=[]
for i in range(0,10,2):#在范围[0,10]以步长为2，从左向右取值
    list1.append(i)
print(list1)#[0, 2, 4, 6, 8]
list2=[]
for i in range(10,0,-2):#在范围[0,10]以步长为2，从右向左取值
    list2.append(i)
print(list2)#[10, 8, 6, 4, 2]
k=4
# for i in range(1,k+1,1):
    # print("*"*i)
    # print("*"*(2*i-1))
    # print(" "*int(k-i)+"*"*int(2*i-1))
k2=8
for i in range(1,k2+1,1):
    if i==1:
        print(" " * int(k2 - i) + "*" + " " * int(2 * i - 3))
    elif i==k2:
        print("*"*(2*i-1))
    else:
        print(" "*int(k2-i)+"*"+" "*int(2*i-3)+"*")
