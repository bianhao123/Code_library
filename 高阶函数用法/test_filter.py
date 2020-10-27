# -*- encoding: utf-8 -*-
'''
@File    :   test_filter.py
@Time    :   2020/10/26 16:39:24
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   测试高阶函数filter
'''
# filter(f,iter):保留f返回true的iter元素

def isodd(x):
    return x % 2 == 1

L = list(filter(isodd, range(10)))
print('L=', L)  # L= [1, 3, 5, 7, 9]


def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:  # 一旦整除，x一定不是素数
            return False
    return True

L = list(filter(isprime, range(100)))
print('L=', L)
# 结果：L= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]