# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: day1
# Author: TangJianjun
# Date: 2020/7/6
# Description:Notes for the study of Python3, day 1st.
#-----------------------------------------------------------------------------------
# python学习第一天
"""
1. pycharm 使用：
    快速复制粘贴行：ctrl + d
    快速换行：shift + Enter
    注释快捷键：ctrl + /
2.赋值：
    单个变量赋值：
        a="变量1"
        b=1
        c=2.12
    批量赋值： a,b,c=1,"a","法国红酒"
3.打印输出：print()
    输出字符串：print("你好")
    输出变量：print(a)
    计算输出：
        print("正"*5)'执行5次输出操作'
        print("2+3="，2+3)
    打印不换行：
        print("第一行",end='')
        print("第二行")
4. 格式化字符串：
    %s 格式化为str类型
    %d 格式化为int类型
    %f 格式化为float类型
    三个一起用时，需要一一对应
        import math
        print("今天7月%d日，天气%s，PM2.5指数%0.2f" %(6,"",100.00))
"""
print("hello Monday!")
a, b, c = 1, "a", "法国红酒"
print(a)
print(b)
print(c)

import math
print("今天7月%d日，天气%s，PM2.5指数%0.2f" %(6,"",100.00))

print("第一行",end='')
print("第二行")

