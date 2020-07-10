# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: hoemwork_for_day4
# Author: TangJianjun
# Date: 2020/7/10
# Description:
#-----------------------------------------------------------------------------------
# 1、随机抽取人名：方法随机，提示其中一种可以用random中的选择方法
import random
name_list=['甲','乙','丙','丁']
num=random.randint(1,4)
num-=1
print(name_list[num])
# 2、使用while循环输出 1 2 3 4 5 6 8 9 10
i=0
while i <10:
    i += 1
    if i==7:
        continue
    print(i)
# 3、有1、2、3、4个数字，能组成哪些互不相同且无重复数字的三位数？
set1=set()
for n1 in range(1,5):
    for n2 in range(1,5):
        for n3 in range(1, 5):
            if n1!=n2 and n1!=n3 and n2!=n3:
                 s=str(n1)+str(n2)+str(n3)
                 set1.add(s)
print(set1)
# 4、输出0到100之间被3整除的整数，如果这个数能被5整除则不输出
set2=set()
for i in range(0,101):
    if i%3==0 and i%5!=0:
        set2.add(i)
print(set2)
# 5、写出九九乘法表（方法不限）
for a in range(1,10):
    for b in range(1,10):
        if a<=b:
            s=a*b
            print(str(a)+"*"+str(b)+"="+str(s))
# 6、定义一个函数，练习不同的传参方法。
# 7、复习进入的内容，巩固每天的知识点。