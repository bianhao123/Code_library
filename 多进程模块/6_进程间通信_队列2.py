# -*- encoding: utf-8 -*-
'''
@File    :   6_进程间通信_队列.py
@Time    :   2020/11/01 01:05:20
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   基于队列的生产者消费者模型，生产者在生产完毕后发送结束信号None 
'''

# here put the import lib
from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        if res is None:break #收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))
    # q.put(None) #发送结束信号 way1
if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))

    #开始
    p1.start()
    c1.start()

    # way2:主进程在生产者生产完毕后发送结束信号None
    p1.join()
    q.put(None) #发送结束信号

    
    print('主')
    # q.put(None) #发送结束信号


