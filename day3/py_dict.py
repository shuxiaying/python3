# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: day3
# Author: TangJianjun
# Date: 2020/7/8
# Description:
#-----------------------------------------------------------------------------------
"""
字典{}，字典是无序的对象集合，由键（key）和对应的值（value）组成，
键与值用冒号“:”隔开，键必须保持唯一性，值不必
"""
dict1={}#空字典
dict2={"a":100,"b":100,"c":101,"d":102,}#非空字典
print(dict2)#{'a': 100, 'b': 100, 'c': 101, 'd': 102}
#1. 添加对象，前提添加的key在列表中不存在
#使用update()添加
dict2.update({"e":103})
print(dict2)#{'a': 99, 'b': 100, 'c': 101, 'd': 102, 'e': 103}
#使用赋值添加
dict2["f"]="104"
print(dict2)
#2. 修改对象值dict[‘key’]= ‘新的值’
dict2['a']='99'#111
print(dict2['a'])#99
#3. 删除对象
# 使用del dict[key]删除
del dict2["e"]
print(dict2)#{'a': '99', 'b': 100, 'c': 101, 'd': 102, 'f': '104'}
# 使用pop(key)删除键值对并返回键值
print(dict2.pop("f"))#104
print(dict2)#{'a': '99', 'b': 100, 'c': 101, 'd': 102}
#使用popitem()删除字典最后一个键值对，并返回键值对
print(dict2.popitem())#('d', 102)
print(dict2)#{'a': '99', 'b': 100, 'c': 101}
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
#打印key值
for k in dict2:
    print(k)
#a
# b
# c
#打印value值
for v in dict2:
    print(dict2[v])
#99
# 100
# 101
#打印所有键值对
for k,v in dict2.items():
    print(k,":",v)
# a : 99
# b : 100
# c : 101
#打印指定key对应value值
for k in dict2:
    if k=='b':
        print(dict2[k])
#100
# 6. 使用字典的输出格式化
#引用key值对应输出value值
print("I\'m %(name)s, I\'m %(age)d years old. "%{'name':"Tom",'age':19})
#I'm Tom, I'm 19 years old.
print("I\'m {name}, I\'m {age} years old. ".format(name="Tom",age=19))
#I'm Tom, I'm 19 years old.
boy1={'Tom':19,'Jack':20,'Sam':18}
#遍历输出全部键值对
for n,a in boy1.items():
    print("I\'m %s, I\'m %d-year-old. "%(n,a))
    print("I\'m {0}, I\'m {1}-year-old. ".format(n,a))
# I'm Tom, I'm 19-year-old.
# I'm Tom, I'm 19-year-old.
# I'm Jack, I'm 20-year-old.
# I'm Jack, I'm 20-year-old.
# I'm Sam, I'm 18-year-old.
# I'm Sam, I'm 18-year-old.
#通过字典设置参数
site={'name':"百度",'url':"www.baidu.com"}
print("网站名:{name}\n地址:{url}".format(**site))
# 网站名:百度
# 地址:www.baidu.com
