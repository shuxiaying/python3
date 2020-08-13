# -*- coding:utf8 -*- #
#-----------------------------------------------------
# ProjectName: python3 
# FileName: pytest_sum
# Author:TangJianjun
# Date: 2020/8/13 
# Description:
#-----------------------------------------------------
import pytest

# @pytest.fixture()
# def decorator():
#     @pytest.fixture(params=[1,2,3])
#     def wraptor(request):
#         results=request.param
#         return results
#     return wraptor

@pytest.fixture()
def decorator(data):
    def wraptor(func):
        @pytest.fixture(params=data)
        def param_func(request):
            print(request.param)
            results = func(request.param)
            return results
        print(param_func)
        return param_func
    return wraptor


# def decorator(dta):
#     def fix1(func):
#         # @parameterized.expand(dta)
#         def wraptor(avg):
#             print('2',avg)
#             return func(avg)
#         print('1',wraptor(dta))
#         return wraptor
#     return fix1

@decorator([(1, 3, 4), (1, 3, 5), [3, 7, 10]])
def test_1(*argv):
    print(argv)


# @decorator
# def test_sum(argv):
#     print(argv)