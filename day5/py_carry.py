# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: py_carry
# Author: TangJianjun
# Date: 2020/7/10
# Description:
#-----------------------------------------------------------------------------------
#继承，私有方法，super函数，静态方法
#在继承中使用super函数，继承父类结构，重新定义neir
#静态方法@staticmethod：类名.方法名，被修饰的静态方法不用写self参数
from day5 import id
id()
class Dog:
    def honest(self):
        print("狗很忠诚")
class Pig(Dog):
    def fat(self):
        print("猪长得胖")
class Cat(Pig):
    def catch(self):
        print("猫抓老鼠")
class Bird(Dog):
    def fly(self):
        print("鸟会飞")
    def super__(self):
        print("狗不忠诚")
dg=Dog()
pg=Pig()
ct=Cat()
bd=Bird()
dg.honest()
pg.fat()
pg.honest()
ct.catch()
ct.fat()
ct.honest()
bd.fly()
bd.honest()
bd.super__()