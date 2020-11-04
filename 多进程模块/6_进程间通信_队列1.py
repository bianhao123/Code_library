# -*- encoding: utf-8 -*-
'''
@File    :   6_进程间通信_队列.py
@Time    :   2020/11/01 01:05:20
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   队列使用
'''

# here put the import lib
""" 
虽然可以用文件共享数据实现进程间通信，但问题是：

1）效率低（共享数据基于文件，而文件是硬盘上的数据） 2）需要自己加锁处理

因此我们最好找寻一种解决方案能够兼顾：1）效率高（多个进程共享一块内存的数据）2）帮我们处理好锁问题。

mutiprocessing模块为我们提供的基于消息的IPC通信机制：队列和管道。

1 队列和管道都是将数据存放于内存中

2 队列又是基于（管道+锁）实现的，可以让我们从复杂的锁问题中解脱出来， 我们应该尽量避免使用共享数据，尽可能使用消息传递和队列，避免处理复杂的同步和锁问题，而且在进程数目增多时，往往可以获得更好的可获展性 
"""


"""  
Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。 
maxsize是队列中允许最大项数，省略则无大小限制。    

"""




from multiprocessing import Process,Queue
import time
q=Queue(3)


#put ,get ,put_nowait,get_nowait,full,empty
q.put(3)
q.put(3)
q.put(3)
print(q.full()) #满了

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #空了

