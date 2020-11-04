# -*- encoding: utf-8 -*-
'''
@File    :   间接调用.py
@Time    :   2020/11/01 00:34:15
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   None
'''

# here put the import lib

#方法二 继承式调用
import time
import random
from multiprocessing import Process


class Run(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s runing' %self.name)
        time.sleep(random.randrange(1,5))
        print('%s runing end' %self.name)

if __name__ == "__main__":
    p1=Run('anne')
    p2=Run('alex')
    p3=Run('ab')
    p4=Run('hey')
    p1.start() #start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主线程')