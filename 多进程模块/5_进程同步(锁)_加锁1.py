# -*- encoding: utf-8 -*-
'''
@File    :   5_进程同步(锁).py
@Time    :   2020/11/01 00:54:18
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   加锁：多个进程共享同一打印终端
'''

# here put the import lib

#由并发变成了串行,牺牲了运行效率,但避免了竞争
from multiprocessing import Process,Lock
import os,time
def work(lock):
    lock.acquire()
    print('%s is running' %os.getpid())
    time.sleep(2)
    print('%s is done' %os.getpid())
    lock.release()
if __name__ == '__main__':
    lock=Lock()
    for i in range(3):
        p=Process(target=work,args=(lock,))
        # p.daemon=True # 加了守护进程的话，主进程运行结束，子线程就结束运行。因为加了同步锁，所以后续的两个子进程没有执行
        p.start()

