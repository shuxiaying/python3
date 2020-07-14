
# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName: python3
# FileName: day7
# Author: TangJianjun
# Date: 2020/7/14
# Description:
#-----------------------------------------------------------------------------------
import os
# if __name__ == '__main__':
#     while 1:
#         if os.path.exists('c:\\poem'):
#             if os.path.exists('c:\\poem\\jingyesi.txt'):
#                 with open('c:\\poem\\jingyesi.txt',mode='r') as fl1:
#                     with open('c:\\poem\\jingyesi2.txt',mode='w')as fl_new:
#                         fl_new.write(str(fl1.read()))
#                 break
#             else:
#                 with open('c:\\poem\\jingyesi.txt',mode='w') as fl:
#                     fl.write('静夜思\n窗前明月光，\n疑似地上霜。\n举头望明月，\n低头思故乡。')
#                 continue
#         else:
#             os.mkdir('c:\\poem')
#             continue
class CreatCopy:
    def cp(self,filepath,filepath_new,*content):
        while 1:
            if os.path.exists(filepath):
                with open(filepath, mode='r') as fl1:
                    with open(filepath_new, mode='w') as fl_new:
                        fl_new.write(str(fl1.read()))
                        break
            else:
                with open(filepath, mode='w') as fl:
                    fl.write(str(*content))
                continue
import time
import datetime
print(datetime.date(1996,8,1).weekday())
import calendar
cal=calendar.month(1996,8)
print(cal)
with open('c:\\calendar.txt',mode='w',encoding='utf8') as fl:
    fl.write(cal)