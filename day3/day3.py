# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: day3
# Author: TangJianjun
# Date: 2020/7/8
# Description:
#-----------------------------------------------------------------------------------
#元组 tuple
tuple1=()#空元组
tuple2=(1)#元组内只有一个非空元素时，要用‘,’隔开，否则会报错
tuple3=(1,)#非空元组，元素为1和空
print(type(tuple1),type(tuple2),type(tuple3))
#<class 'tuple'> <class 'int'> <class 'tuple'>
tuple4=(1,2,3,4,5)
# 1. 使用索引打印元组元素
print(tuple4[0])#output：1
# 2. 遍历打印元组
for i in tuple4:
    print(i)
#3. 切片打印元组
print(tuple4[:3])#(1, 2, 3)
#4. 删除元组
tuple_tmp=(1,2,3)
print("删除前",tuple_tmp)#删除前 (1, 2, 3)
del tuple_tmp
#print("删除后",tuple_tmp)#NameError: name 'tuple_tmp' is not defined
#5. 元组的拼接
tuple_new1=tuple3+tuple4
tuple_new2=(tuple3,tuple4)
print(tuple_new1)#(1, 1, 2, 3, 4, 5)tuple_new1=tuple3+tuple4
print(tuple_new2)#((1,), (1, 2, 3, 4, 5))
"""
字典{}，字典是无序的对象集合，由键（key）和对应的值（value）组成，
键与值用冒号“:”隔开，键必须保持唯一性，值不必
"""
dict1={}#空字典
dict2={"a":100,"b":100,"c":101,"d":102,}#非空字典
print(dict2)#{'a': 100, 'b': 100, 'c': 101, 'd': 102}
#1. 更改字典对象
dict2["a"]=99
print(dict2)#{'a': 99, 'b': 100, 'c': 101, 'd': 102}
#2. 添加对象
#dict2.update({"e":103})
print(dict2)#{'a': 99, 'b': 100, 'c': 101, 'd': 102, 'e': 103}
#3. 删除对象 del dict[]
#del dict2["c"]
print(dict2)#{'a': 99, 'b': 100, 'd': 102, 'e': 103}
#4. 删除字典del dict
# del dict2
# print(dict2)#NameError: name 'dict2' is not defined
#5. 打印字典
#使用dict.keys()打印所有key值，返回一个迭代器，可以用list()转换成列表
print(dict2.keys(),dict2.values())
#dict_keys(['a', 'b', 'c', 'd']) dict_values([99, 100, 101, 102])
print(list(dict2.keys()),list(dict2.values()))
#['a', 'b', 'c', 'd'] [99, 100, 101, 102]
#使用for循环打印
for k,v in dict2.items():
    print(k,":",v)
# a : 99
# b : 100
# c : 101
# d : 102