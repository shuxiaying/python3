# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: homework_for_day2
# Author: TangJianjun
# Date: 2020/7/7
# Description:Homework for the study of Python3, day 2ed
#-----------------------------------------------------------------------------------
#-----------------------------------作业0707----------------------------------------
"""1、给出数据：星期1到星期7，天气为晴天，阴天，雨天，雾天，冰雹天，狂风暴雨天，雷电交加天，
老王分别要在这7天做7件事（事情个人自定义），
用格式化（%s %d）和.format()函数的输出方式把这7天的内容输出：
如：星期1，天气为晴天，老王今天要去游泳！
"""
import random#导入random函数
date=[1,2,3,4,5,6,7]#定义日期对象
weather=["晴","阴","雨","雾天","冰雹","暴雨","雷阵雨"]#定义天气对象
event=["阅读","看电影","健身","购物","聚会","吃火锅","打麻将"]#定义事件对象
a,i=0,0 #初始化
print("1) 使用格式化（%s %d）输出：")
#使用while循环输出
while i<7:
    b = random.randint(0, 6)#产生随机天气
    c = random.randint(0, 6)#产生随机事件
    print("星期%d，天气%s，老王今天要去%s"%(date[a],weather[b],event[c]))#组合日期、天气、事件输出
    i+=1
    a+=1
print("2) 使用.format()函数输出：")
g,t=0,0#初始化
while t<7:
    b = random.randint(0, 6)#产生随机天气
    c = random.randint(0, 6)#产生随机事件
    print("星期{0}，天气{1}，老王今天要去{2}".format(date[g],weather[b],event[c]))#组合日期、天气、事件输出
    t+=1
    g+=1
#2、给出数据：name = "老王"； age = 109；height = 170；weight = '50kg'；用',' 和'+'两种方式进行拼接输出，语句自己造句
name,age,height,weight="老王","109","170","50kg"
print("1) 使用\',\'拼接输出：")
print(name,"今年",age,"岁了，身高",height,"体重",weight,"，倍儿棒！")
print("2) 使用\'+\'拼接输出：")
print(name+"今年"+str(age)+"岁了，身高"+str(height)+"，体重"+weight+"，倍儿棒！")
"""
3、给出数据：s = 'HelloStudentsGoodMorning'；s2 = '商品名单价数量总价'；s3 = '皮鞋992198'；s4= '大衣108101080'；
用转义字符输出如下格式：
Hello
Students
Good
Morning
商品名    单价    数量    总价
皮鞋      99      2      198
大衣      108     10     1080
"""
print("Hello\rStudents\rGood\rMorning")
print("商品名\t\t单价\t数量\t总价")
print( "皮鞋\t\t99\t\t2\t\t198")
print("大衣\t\t108\t\t10\t\t1080")
"""
4、声明一个字符串"helloworld@error.com",
要求对字符串进行截取操作，
截取出来的每个字符串放到一个新的列表中，
最终的结果是：['hello','world','error','com']
"""
str1="helloworld@error.com"
list1=[str1[0:5],str1[5:10],str1[11:16],str1[-3::],]
print(list1)