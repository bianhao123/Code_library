# 资料记录
https://www.cnblogs.com/jiangfan95/p/11439207.html

# 笔记
- 进程加锁就是：并行处理->串行处理

# 问题记录
问题1：The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable
解决方法：从错误信息可以看出进程池相关代码应该放在if __name__ == '__main__'下面，代码修改如下：
参考链接：https://blog.csdn.net/xiemanR/article/details/71700531

