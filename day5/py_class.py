# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: py_class
# Author: TangJianjun
# Date: 2020/7/10
# Description:
#-----------------------------------------------------------------------------------
#类用class来定义，首写字母一般大写，多个单词用驼峰式命名
# 类的方法至少有一个参数self,表示指向类的本身
class Person:
    name="Tom"#成员变量
    height="180cm"
    weight="70kg"
    sex="男"
    def speck(self):#成员方法
        print("%s，%s，身高%s，体重%s"%(Person.name,Person.sex,Person.height,Person.weight))
#对象：创建对象的过程称为实例化，当一个对象被创建后，包含对象的属性和行为
# 对象的属性和行为与类的成员变量和成员方法相对应。
# 类的实例化
infor=Person()
infor.speck()#Tom，男，身高180cm，体重70kg
print("%s，%s，身高%s，体重%s"%(infor.name,infor.sex,infor.height,infor.weight))
#Tom，男，身高180cm，体重70kg
class Tom:
    _name="Tom"#私有化属性，类对象和子类可以访问
    __height="180cm"#私有化属性，名字重整，类外不可访问
    def speck(self):#成员方法
        print(Tom._name,Tom.__height)
    def _height(self):#私有化方法，类对象和子类可以访问
        print("height 180cm")
    def __weight(self):#私有化方法，名字重整，类外不可访问
        print("weight 70kg")
tm=Tom()
tm.speck()#Tom 180cm
print(tm._name)#Tom
tm._height()#height 180cm
#构造方法
"""
析构方法:是对类执行资源的释放，构造函数与析构函数，
简单的可以理解为构造函数是对类进行初始化操作，
析构函数是对类中的方法执行完成后，对类的资源进行清理工作。
"""
#__del__是析构函数，析构函数也是可选的
