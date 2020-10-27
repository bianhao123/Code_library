# -*- encoding: utf-8 -*-
'''
@File    :   test_map.py
@Time    :   2020/10/26 16:25:03
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   测试python的高阶函数map
'''

# here put the import lib


def f(x):
    return x*x

# 1.python3可将map转换为list：
r1 = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(r1)

# 2.使用 lambda 匿名函数
r2 = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(r2)

