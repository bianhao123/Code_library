# -*- encoding: utf-8 -*-
'''
@File    :   5_进程同步(锁).py
@Time    :   2020/11/01 00:54:18
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   不加锁：多个进程共享同一打印终端
'''

# here put the import lib

#并发运行,效率高,但竞争同一打印终端,带来了打印错乱
from multiprocessing import Process
import os,time

def work():
    print('%s is running' %os.getpid())
    time.sleep(2)
    print('%s is done' %os.getpid())

if __name__ == '__main__':
    for i in range(3):
        p=Process(target=work)
        p.start()

