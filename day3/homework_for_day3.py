# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: homework_for_day3
# Author: TangJianjun
# Date: 2020/7/8
# Description:Homework for the stydy of Python, day 3th.
#-----------------------------------------------------------------------------------
# 1、计算1到100的总和。
i,s=0,0
while i <= 100:
    s+=i
    i+=1
else:
    print(s)
#2、从键盘输入一个数，如果是奇数，就打印奇数，如果是偶数，就打印偶数
# num=int(input("请输入一个整数："))
# print("偶数" if num%2==0 else "奇数")
#从键盘输入一个整数，判断这个整数是正数还是负数，如果是正偶数则输出是正偶数，否则输出不是正偶数
# num1=int(input("请输入一个整数："))
# print("正偶数" if num1>0 and num1%2==0 else "不是正偶数")
""""
4、一共5次机会，5次机会用完之后，不管猜中不猜中都退出程序，如果5次内猜中就直接退出程序
猜数字游戏，给一个数字，
如果小于就提示：您预测的数字小了，还剩下x次机会！
如果大于就提示：您预测的数字大了，还剩下x次机会！，
如果刚好猜中，提示您真幸运，恭喜您猜中了。
"""
# import random#导入random函数
# right=random.randint(1,100)#赋值right为1到100的随机数
# i,s=0,5#初始化i与s的值，s为总游戏次数
# while i<s:
#     num2=int(input("请输入数字："))#标准输入
#     i+=1
#     if num2 == right:
#         print("您真幸运，恭喜您猜中了。")
#         break
#     elif num2 > right:
#         print("您预测的数字大了，还剩下"+str(s-i)+"次机会！")
#     else:
#         print("您预测的数字小了，还剩下"+str(s-i)+"次机会！")
# print("游戏结束")
"""
5、打印水仙花数：
水仙花数是指一个 n 位数（n≥3 ），它的每个位上的数字的 n 次幂之和等于它本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
利用for循环输出1000以内得水仙花数。 
"""
i,t=100,100#初始化i,t的值为100
list1=[]#定义列表list1装载1000以内的n位数（n≥3 ）
list2=[]#定义列表list2装载1000以内的水仙花数
#遍历[100,1000]的数
while i <=1000:
    list1.append(i)#将遍历的数添加到list1中
    i+=1
list3=[]
# list3.extend(range(100,1000,1))
for i in range(100,1000,1):
    t=str(i)
    if i==(int(t[0])**3+int(t[1])**3+int(t[2])**3):
        list3.append(i)
print(list3)
def func(n):
    list4=[]#存放水仙花数
    for i in range(10**(n-1),10**n,1):#遍历所有n位数
        num=str(i)
        s = 0
        for t in num:#获取每个位上的数字的 n 次幂之和
            s+=(int(t)**n)
        if i==s:
            list4.append(i)
    return list4
print(func(4))

#遍历list1中的数
for t in list1:
    #判断为数字为3位数还是4位数
    if t < 1000:
        g=t%10#输出个位数
        b=t//100#输出三位数中的百位数
        s=(t//10)%10#输出十位数
        if t == (g**3+s**3+b**3):#判断每个位上的数字的 n 次幂之和是否等于它本身
            list2.append(t)#满足水仙花数条件，输出到list2中
    elif t == 1000 :
        g = t % 10#输出个位数
        q=t//1000#输出四位数千位数
        b=(t//100)%10#输出三位数中的百位数
        s=(t//10)%10#输出十位数
        if t == (g**3+s**3+b**3+q**3):
            list2.append(t)
print(list2)#输出1000以内的水仙花数