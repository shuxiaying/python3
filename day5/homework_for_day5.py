# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: homework_for_day5
# Author: TangJianjun
# Date: 2020/7/10
# Description:Homework for day 5th.
#-----------------------------------------------------------------------------------
# 1、给一个全局变量：shoe = "高跟鞋" 用global 修改全局变量 高跟鞋 为 高帮鞋
shoe= '高跟鞋'
def shoes():
    global shoe
    shoe='高帮鞋'
    print(shoe)
# shoes()
# 2、定义一个类，在类中定义4个函数，分别实现2个数的加、减、乘、除
class count_fun:
    def im_sum(self,a,b):
        print(a+b)
    def im_sub(self,a,b):
        print(a-b)
    def pro_duct(self,a,b):
        print(a*b)
    def di_vision(self,a,b):
        print(a/b)
# count=count_fun()
# count.im_sum(1,2)
# count.im_sub(1,2)
# count.pro_duct(1,2)
# count.di_vision(1,2)
# 3、写一个类，包含私有方法和私有变量和静态方法
# 定义类：Cat
class Cat_d5:
    color='yellow.'
    _name = 'July.'#私有化属性，类对象和子类可访问
    __master='Tom.'#私有化属性，外部不可直接访问
    def speak(self):
        print('Speak like miao~miao~miao~. ',end='')
    def __hobby(self):#私有化属性，外部不可直接访问
        hate='hate water.'
        return hate
    def _host(self):#私有化方法，类对象和子类可访问
        print('Master is',self.__master,self.__hobby())
# 定义类Tom,父类为Cat
class Tom_d5(Cat_d5):
    my_id='I\'m Tom, the master of the cat. My cat is'
cat=Cat_d5()#类Cat实例化
master=Tom_d5()#类Tom实例化
#定义函数实现子类Tom调用父类Cat
def tom_spk():
    print(master.my_id,master.color,'Its name is',master._name,end=' ')
    master.speak()
    master._host()
# 定义函数实现外部调用类对象
def cat_spk():
    print('I\'m',cat._name,'My color is',cat.color,end='')
    cat.speak()
    cat._host()
# tom_spk()
# cat_spk()
# 4、封装一个文件，文件中写五个类，父类的一个方法被4个子类重写，实现了不同的行为
# from book import Book_1,Book_2,Book_3,Book_4
# bk1=Book_1()
# bk2=Book_2()
# bk3=Book_3()
# bk4=Book_4()
# bk1.price()
# bk2.price()
# bk3.price()
# bk4.price()
# 5、完成以下图形的输出
# for i in range(1,6):
#     print('*'*i)
# for i in range(1,6):
#     print('*'*(5-i))
# 6、冒泡排序：
# 将list = [7, 4, 3, 67, 34, 1, 8]中的数据从小到大排序，最后输出结果为：[1, 3, 4, 7, 8, 34, 67]：提示冒泡排序，比较大小交换位置，或者用空杯交换原理
list1=[7, 4, 3, 67, 34, 1, 8]
list2=list1.copy()
for i in list1:
    for t in list2:
        if i<t:
            list2.remove(i)
            list2.insert(list2.index(t),i)
            break


# gs=len(list1)
# i=0
# while i<gs:
#     a=list1[i]
#     t=0
#     while t <gs:
#         b=list2[t]
#         if a<b:
#             list2.insert(t,a)
#             del list2[i]
#             i+=1
#             break
#         t+=1
#         if t==gs:
#             list2.insert(t, a)
#             del list2[i]
#             i += 1
#             break
print(list2)
# 7、求1-2+3-4+5 ... 99的所有数的和
s=0
for i in range(1,100):
    if i%2==0:
        i=0-i
    s+=i
# print(s)
# 8、小芳的妈妈每天给她2.5元钱，她都会存起来，从存钱开始，每过5天她就会花去6元钱，请问要到第几天，小芳才可以存满100元钱
# f(x)=2.5*x-6*(x//5)
x,s=0,0
while s<100:
    x+=1
    s = 2.5 * x - 6 * (x//5)
# print(x)

# print([i for i in range(1,101) if i%2!=0])
