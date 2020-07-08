# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: py_dict
# Author: TangJianjun
# Date: 2020/7/8
# Description:Notes for Python project of set, day 3th.
#-----------------------------------------------------------------------------------
#集合,无序，自动去重，数据类型无限制；集合可以用{}和set()来创建
#空集合只能用set()创建，用{}创建的是空字典
set_null=set()
print(set_null)#set()
#非空集合
set1=set([1,5,6])
print(set1)
#{1, 5, 6}
set2={1,2,3,4,5}
#求交集&、intersection()，返回集合相同部分
print(set1&set2)#{1, 5}
print(set1.intersection(set2))#{1, 5}
#求并集 |、union()，取两个集合的元素，去除重复项输出
print(set1|set2)#{1, 2, 3, 4, 5, 6}
print(set1.union(set2))#{1, 2, 3, 4, 5, 6}
#差集 '-'、difference()，返回集合A减集合B，即集合A中不在集合B中的元素
print(set2-set1)#{2, 3, 4}
print(set2.difference(set1))#{2, 3, 4}
print(set1.difference(set2))#{6}
#非集合‘^’、symmetric_difference()，取A、B两个集合的交集，然后根据交集取在A、B集合的补集合并输出
print(set1^set2)#{2, 3, 4, 6}
print(set1.symmetric_difference(set2))#{2, 3, 4, 6}
#集合的添加
# add()，可添加单个元素或元组
set3=set()
print(set3)#set()
set3.add(1)
set3.add("s")
print(set3)#{1, 's'}
set3.add((2,3))
print(set3)#{1, 's', (2, 3)}
#update()，可添加元素，元素可以为列表、元组、字典
set4=set()
set4.update("hello")
print(set4)
#{'l', 'h', 'e', 'o'}
#添加字典，只能添加key值
set4.update({"name":"Tom"})
print(set4)
#{'e', 'l', 'name', 'h', 'o'}
#添加列表
set4.update([1,2,3])
print(set4)
#{'h', 1, 2, 3, 'o', 'e', 'name', 'l'}
#添加元组
set4.update((4,5))
print(set4)#{1, 2, 3, 4, 5, 'h', 'e', 'o', 'l', 'name'}
#集合的移除
# remove(x)，移除集合中的元素x，如不存在会报错
set4.remove("name")
print(set4)#{1, 'o', 2, 3, 4, 5, 'l', 'e', 'h'}
# discard(x)，移除集合中的元素x，如不存在不报错
set4.discard('l')
print(set4)#{1, 'o', 2, 3, 'h', 4, 5, 'e'}
# pop()，随机删除集合中的一个元素
set4.pop()
print(set4)#{2, 3, 4, 'h', 5, 'o', 'e'}
#del，删除整个集合
# del set4
# print(set4)#NameError: name 'set4' is not defined
# 计算集合长度len()
print(len(set4))#7
# 清空集合clear()
set4.clear()
print(set4)#set()