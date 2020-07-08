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
#7. python中常用逻辑运算符：逻辑与and、逻辑或or、逻辑非not
#8. python中的进制转换运算：
#9. python中位运算符：
#10. python中的赋值运算符：
#11. python中的成员运算符：
#12. python中的身份运算符：
#7. 拼接：使用','或'+'进行拼接：
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
