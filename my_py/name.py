# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: name
# Author: TangJianjun
# Date: 2020/7/9
# Description:
#-----------------------------------------------------------------------------------
import random
import time
# 创建点名册
namelist = ["唐建军", "孙家耀", "张辛碧", "宋羽"]
#获取当前时间-月份
re_month = time.localtime(time.time()).tm_mon
#获取当前时间-日
now = time.localtime(time.time()).tm_mday
#创建点名日志-日
list_date=[6,7,8]
#获取最新点名日期-日
last_date=max(list_date)
#创建记录
record = {"唐建军":0, "孙家耀":0, "张辛碧":0, "宋羽":0}
# 初始化记录
def re_reset():
    for i in namelist:
        record[i] = 0
    return record
#产生随机姓名
def call_name():
    num=random.randint(0,3)
    call_name=namelist[num]
    return call_name
#修改记录
def re_mod(n):
    if n in record:
        v=record[n]+1
        record[n]=v
        return record  # 返回修改后的表
    else:
        return record #返回未修改的表
#获取所有成员被点到记录次数
def re_times():
    times_list = []
    times_list.clear()
    times_set = set()
    times_set.clear()
    for k,v in re_mod(0).items():
        times_list.append(v)
    times_set.update(times_list)#利用集合去重
    return times_set #返回各个成员记录次数集合
#获取被点到记录最大次数
def max_call():
    k=max(re_times())
    return k
# 获取被点到成员今日记录次数
def call_times(n):
    record=re_mod(0)
    return record[n]
pass
start_call=input("点击Enter开始点名")
while start_call is str():
    # if now!=last_date:
    #     re_reset()
    #     list_date.append(now)
    #     print("已初始化")
    #     break
    n = call_name()#随机点名
    re_mod(0)
    s=call_times(n) #被点成员今日被点次数
    m=max_call() #今日点名记录最大次数
    if s==m and re_times() !=1: #判断是否为最大次数且各个成员记录次数是否不同
        continue
    else:
        print(call_name())#输出被点名成员
        re_new=re_mod(n)#修改记录，被点名成员记录次数加1
        print("当日被点次数：",call_times(n))#输出被点名成员今日记录次数
        next_call=input("点击Enter继续，输入任意内容点击Enter退出点名")
        if len(next_call)>0:
            print("为保证公平，关闭程序前请及时手动更新记录！！！")
            print(str(re_month)+"月"+str(now)+"日点名记录",re_new)
            i=input("我已保存 Y/N，删除数据")
            if i in 'yY':
               break
            else:
                i=input("我以保存 Y/N，删除数据")
        else:
            continue