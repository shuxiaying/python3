# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: book
# Author: TangJianjun
# Date: 2020/7/11
# Description:Package for class Book_d5
#-----------------------------------------------------------------------------------
class Book_d5:
    def price(self):
        print('price is ￥50.00')
class Book_1(Book_d5):
    def price(self):
        print('price is ￥35.00')
class Book_2(Book_d5):
    def price(self):
        print('price is ￥75.00')
class Book_3(Book_d5):
    def price(self):
        print('price is ￥55.00')
class Book_4(Book_d5):
    def price(self):
        print('price is ￥105.00')