# -*- coding:utf8 -*- #
#-----------------------------------------------------
# ProjectName: python3 
# FileName: pytest_sum
# Author:TangJianjun
# Date: 2020/8/13 
# Description:
#-----------------------------------------------------
import pytest

# 使用pytest参数化
@pytest.fixture(scope='function', params=[(1,3,4),(1,3,5),[3,7,10]])
def fix2(request):
    yield request.param

def test_sum(fix2):
    result=sum(fix2)
    print(fix2,result)


# def fix1(data):
#     @pytest.fixture(scope='function', params=data)
#     def fix3(request):
#         print(request.param)
#         yield request.param
#     yield fix3
#
# def test_1():
#     fix1([(1,3,4),(1,3,5),[3,7,10]])

if __name__ == '__main__':
    pytest.main()