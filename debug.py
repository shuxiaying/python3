# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: debug
# Author: TangJianjun
# Date: 2020/8/4
# Description:
#-----------------------------------------------------------------------------------
# a,b=1,2
# a,b=b,a
# print('a=',a,'\n','b=',b)

# str1='HELLOWORLD'
# print(str1[str1.index('L',str1.index('L')+1):])
#
# print(sum(range(1,101)))
#
# list1=[1,2,3,1,2,3]
# print(list(set((list1))))
# list1=['hello',10,[1,4],(9,),66]
# print(len(list1))
# # print(list1[5])
# print(list1[5:10])

# list3=[]
# list4=[]
# for i in range(2,100):
#     for t in range(2,i+1):
#         if i%t==0:
#             list3.append(t)
#     if len(list3)==1:
#         list4.append(list3[0])
#     list3.clear()
# print(list4)

dd={'a':5,'b':5,"c":5,'d':5}
s=0
n=None
for k in dd:
    v=dd[k]
    if s<v:
        s,v=v,s
        n=k
    else:
        continue
print({n:s})