# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: py_tuple
# Author: TangJianjun
# Date: 2020/7/8
# Description:Notes for Python project of tuple, day 3th.
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
# 6.复制元组
tuple_new3=tuple3*5
print(tuple_new3)#(1, 1, 1, 1, 1)

