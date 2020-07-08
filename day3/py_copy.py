# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: py_copy
# Author: TangJianjun
# Date: 2020/7/8
# Description:Notes for Python project of copy, day 3th.
#-----------------------------------------------------------------------------------
"""深拷贝与浅拷贝,
深拷贝和浅拷贝都是对象的拷贝，
# 都会生成一个看起来相同的对象，
# 本质的区别是拷贝出来的对象的地址是否和原对象一样，
也就是地址的复制还是值的复制的区别
"""
import copy
list1=[1,2,3,['a','b','c']]
list2=list1
list3=copy.copy(list1)#对象拷贝，浅拷贝
list4=copy.deepcopy(list1)#对象拷贝，深拷贝
print("list1=",list1,"id(list1)=",id(list1),"id(list1[3])",id(list1[3]))
#list1= [1, 2, 3, ['a', 'b', 'c']] id(list1)= 1704673950408 id(list1[3]) 1704673988936
print("list2=",list2,"id(list2)=",id(list2),"id(list2[3])",id(list2[3]))
#list2= [1, 2, 3, ['a', 'b', 'c']] id(list2)= 1704673950408 id(list2[3]) 1704673988936
print("list3=",list3,"id(list3)=",id(list3),"id(list3[3])",id(list3[3]))
#list3= [1, 2, 3, ['a', 'b', 'c']] id(list3)= 1704674099848 id(list3[3]) 1704673988936
print("list4=",list4,"id(list4)=",id(list4),"id(list4[3])",id(list4[3]))
#list4= [1, 2, 3, ['a', 'b', 'c']] id(list4)= 1704674099912 id(list4[3]) 1704674099592