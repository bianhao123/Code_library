# -*- encoding: utf-8 -*-
'''
@File    :   5_进程同步(锁).py
@Time    :   2020/11/01 00:54:18
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   加锁：多个进程共享同一文件
'''

# here put the import lib

#文件db的内容为：{"count":1}
#注意一定要用双引号，不然json无法识别
#购票行为由并发变成了串行，牺牲了运行效率，但保证了数据安全
from multiprocessing import Process,Lock
import time,json,random
def search():
    dic=json.load(open('db.txt'))
    print('\033[43m剩余票数%s\033[0m' %dic['count'])

def get():
    dic=json.load(open('db.txt'))
    time.sleep(0.1) #模拟读数据的网络延迟
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(0.2) #模拟写数据的网络延迟
        json.dump(dic,open('db.txt','w'))
        print('\033[43m购票成功\033[0m')

def task(lock):
    search()
    lock.acquire()   #获取锁
    get()
    lock.release()   #释放锁
if __name__ == '__main__':
    lock=Lock()
    for i in range(100): #模拟并发100个客户端抢票
        p=Process(target=task,args=(lock,))
        p.start()

