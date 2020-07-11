# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: day2
# Author: TangJianjun
# Date: 2020/7/7
# Description:Notes for the study of Python, day 2ed.
#-----------------------------------------------------------------------------------
#1. 格式化字符串: format():可通过下标或指定变量名引用参数
print("今天{0}，天气{1},空气质量{2}".format("7月7日","多云","佳"))
#output：今天7月7日，天气多云,空气质量佳
print("今天{date}，天气{weather},空气质量{quality}".format(date="7月7日",weather="多云",quality="佳"))
#output：今天7月7日，天气多云,空气质量佳
#2. 标准输入：input()：接受键盘输入，按Enter确认，返回数据为str类型
# passwd=input("请输入密码：")
# print(type(passwd),passwd)
#3. 常用转义字符：\'、\"、\\等，表示取消本身具有的含义，转化为普通字符
#print('I'm Tom.') #报错
print('I\'m Tom.') #output：I'm Tom.
print("这是英文双引号""") #output:这是英文双引号
print("这是英文双引号\"\"") #output:这是英文双引号""
print("这是反斜线\\") #output:这是反斜线\
# 4. 其它转义字符：
# 续行符：\ 表示一行未结束，转到下行继续
print("这是第一行，\
      这是第二行")
# output:这是第一行，      这是第二行

# 换行符：\n 表示换行
print("这是\n第一行")
# output:
# 这是
# 第一行
# 回车符：\r 该行只显示后面的内容
print("这真的\r是第一行")#output：是第一行
print("这\n真的\r是第一行")
# output：
# 这
# 是第一行
# 水平制表符：\t 用于横向跳到下一制表位，默认tab=4
print("12\n\t345\n\t\t6789")
# output:
# 12
# 	345
# 		6789
# 响铃：\a ASCII中的响铃字符，如何显示由控制台程序决定，windows下的cmd终端和Linux下的终端显示为一声铃响，IDLE显示为一个方块
print("\a",len("\a"))
# output： 1
# 退格符：\b 向左退一个字符输出
print("hello\b\b",len("hello\b\b"))
# output：hel 7
#转义符使用注意：当\后面跟的是数字或英文时，很容易引起误会，需谨慎使用，如：
# \0 表示空，占一个字符
print("he\0llo",len("he\0llo")) #output：he llo 6
print("12\34567")#output：12å67
print("12\01267")#\0dd,dd为八进制数，\012表示换行
#output：
# 12
# 67
print("12\x0a67")#\xhh,hh为十六进制数，\012表示换行
#output：
# 12
# 67
#5. python中常用算术运算符：加+、减-、乘*、除/、取余%、整除//、幂**
print(1+1)#output：2
print(2-1)#output：1
print(2*2)#output：4
print(7/2)#output：3.5
print(7/2)#output：3.5
print(7%2)#output：1
print(7//2)#output：3
print(7**2)#output：49
#6. python中常用比较运算符：大于>，大于等于>=，小于<，小于等于<=，等于==，不等于!=；比较结果为真则返回True，否则返回False
print(2>1)#output：True
print(2>=2)#output：True
print(2<1)#output：False
print(1<=2)#output：True
print(2==2)#output：True
print(2!=2)#output：False
#7. python中常用逻辑运算符：
# 逻辑与and
print(1<2 and 2<3)#True
print(1<2 and 2>3)#False
# 逻辑或or
print(1<2 or 2<3)#True
print(1<2 or 2>3)#True
# 逻辑非not
print(not 1<2)#False
print(not 2>3)#True
#8. python中的进制转换运算：
# 在python中，其整形的数据默认是十进制数
# 二进制前加0b转十进制
print(0b1000)#8
# 使用bin()把十进制转二进制
print(bin(8))#0b1000
# 八进制前加0o转十进制
print(0o10)#8
# 使用oct()把十进制转八进制
print(oct(8))#0o10
# 十六进制前加0x转十进制
print(0x10)#16
# 使用hex()把十进制转十六六进制
print(hex(16))#0x10
#还可使用int(x,base=y)，把y进制的字符串x转换成十进制的整数
#9. python中的位运算符：
# 与运算&:1&1结果是1, 1&0结果是0, 0&1结果是0,0&0结果还是0；与运算，只要有0 就是0
a=0b1100
b=0b0110
print(bin(a&b))#0b0100
# 或运算 | ：1|1结果是1, 1|0结果是1, 0|1结果是1,0|0结果是0；或运算，只要有1 就是1
print(bin(a|b))#0b1110
# 异或 ^ ：相同则为0，不同则为1
print(bin(a^b))#0b1010
# 非：~1结果是0，~0结果是1 加1取反
print(bin(~a))#-0b1101
# 左移位<<，向左移动n位
print(bin(a<<3))#0b1100000
# 右移位>>，向右移动n位
print(bin(a>>3))#0b0001
#10. python中的赋值运算符：
a=1
b=2
c=b#c=b=2
a+=b#加赋值a=a+b=1+2=3
a-=b#减赋值a=a-b=3-2=1
a*=b#乘赋值a=a*b=1*2=2
a/=b#除赋值a=a/b=2/2=1
a%=b#取余赋值a=a%b=1%2=1
c**=b#幂赋值c=c**b=2**2=4
c//=b#取整赋值c=c//b=4//2=2
a=0b1100
b=0b0110
c=0b1010
a&=b#按位与赋值a=a&b=0b0100
a|=b#按位或赋值a=a|b=0b0110
a^=b#按位异或赋值a=a^b=0b0
b<<=3#左移赋值b=b<<1=0b0
c>>=3#右移赋值c=c>>3=0b0
#11. python中的成员运算符：
# 测试实例中包含了一系列的成员，包括字符串，列表或元组。
# in：如果在指定的对象中找到值返回 True，否则返回 False
# not in:如果在指定的序列中没有找到值返回 True，否则返回 False
a,a2=1,'1'
b,c,d,e=[1,2,3],{1,2,3},(2,3,4),'step1'
print(a in b)#True
print(a in c)#True
print(a in d)#False 不能用于集合
print(a not in d)#True
print(a2 in e)#True
#12. python中的身份运算符：身份运算符用于比较两个对象的存储单元
# is：判断两个标识符是不是引用自一个对象；= = 用于判断引用变量的值是否相等（内存地址，id() 函数用于获取对象内存地址）
# is not： 判断两个标识符是不是引用自不同对象
#13. 拼接：使用','或'+'进行拼接：
# 使用逗号进行拼接时，对象格式可以不一致，对象和对象直接会有一个空格
print("我的ID是",1012)#我的ID是 1012
# 使用加号进行拼接时，对象格式必须不一致，如不一致需要转换数据类型再拼接
print("我的ID是"+"1012")#我的ID是1012
print("我的ID是"+str(1012))#我的ID是1012
#7. 数据类型转换：
# 整型int()
print("我的年龄是",int(18.00))#output：我的年龄是 18
# 浮点型float()
print("门票价格为￥",float(18))#output：门票价格为￥ 18.0
# 字符型str()
print("我的年龄是"+str(18),"门票价格为￥"+str(18.00))#output：我的年龄是18 门票价格为￥18.0
#repr(x)，将x转换为表达式字符串
print(repr(1+1))#output：2
#eval(str)，计算在字符串中的有效python表达式，并返回一个对象
print(eval("1+1"))#output：2
#chr(x)，将ASCALL码x转换为一个字符
print(chr(49))#output：1
#ord(x)，将一个字符x转换为对应的ASCALL码
print(ord("1"))#output：49
#hex(x)，将一个整数x转换为一个十六进制字符串
print(hex(17),len(hex(17)))#output：0x11 4
#oct(x)，将一个整数x转换为一个八进制字符串
print(oct(9),len(oct(9)))#output：0o11 4
#complex([real[, imag]])，转换成复数输出：z=a+bj,a为实部，b为虚部，j为虚部单位
