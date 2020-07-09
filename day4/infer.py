# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: infer
# Author: TangJianjun
# Date: 2020/7/9
# Description:
#-----------------------------------------------------------------------------------
# 列表推导式：[结果 for 变量 in 可迭代对象] 或者
# [结果 for 变量 in 可迭代对象 if 布尔表达式]
list =[]
for i in range(1,10):
    if i%2==0:
        list.append(i)
print(list)
# 列表推导式
print([i for i in range(1,10) if i%2==0])
pass
#字典推导式：[结果 for 变量 in 可迭代对象] 或者
# [结果 for 变量 in 可迭代对象 if 布尔表达式]
dict1={'a':1,'b':2,'c':3,'d':4}
for k, v in dict1.items():
    print(k,v)
#字典推导式
print({k:v for k,v in dict1.items()})
# 集合推导式：{结果for 变量 in 迭代对象}
# 或者 {结果 for 变量 in 迭代对象 if 布尔表达式}
# 字典推导式的结果是键值对，集合推导式的结果是单个结果
# 如果类型相同并且值相同，打印的时候会去重
print({x for x in dict1.values()})
print({x for x in dict1.keys()})
print({x for x in dict1.items()})
# 迭代iteration:迭代就是重复运行一段代码语句块的能力，
# 就好比在一个容器中进行一层一层遍历数据，在应用过程中for循环最为突出

from collections.abc import Iterable, Iterator
list1 = [1, 3, 5, 7, 9]
print(isinstance(list1,Iterable))
print(isinstance(list1,Iterator))