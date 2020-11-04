# -*- encoding: utf-8 -*-
'''
@File    :   直接调用.py
@Time    :   2020/11/01 00:14:28
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   None
'''

# here put the import lib

#方法一 直接调用
import time
import random
from multiprocessing import Process

""" 
Process([group [, target [, name [, args [, kwargs]]]]])，由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）

强调：
1. 需要使用关键字的方式来指定参数
2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号 
"""

"""
group参数未使用，值始终为None
target表示调用对象，即子进程要执行的任务
args表示调用对象的位置参数元组，args=(1,2,'anne',)
kwargs表示调用对象的字典,kwargs={'name':'anne','age':18}
name为子进程的名称
 """

def run(name):
    print('%s runing' %name)
    time.sleep(random.randrange(1,5))
    print('%s running end' %name)



if __name__ == "__main__":
    p1=Process(target=run,args=('anne',)) #必须加,号 
    p2=Process(target=run,args=('alice',))
    p3=Process(target=run,args=('biantai',))
    p4=Process(target=run,args=('haha',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主线程')