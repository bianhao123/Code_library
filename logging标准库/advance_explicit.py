# -*- encoding: utf-8 -*-
'''
@File    :   advance_explicit.py
@Time    :   2020/10/26 12:21:17
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   使用python代码显示的创建loggers, handlers和formatters并分别调用它们的配置函数；
'''

# here put the import lib
import logging
import logging.handlers
import datetime

# 1 创建一个日志器logger并设置其日志级别为DEBUG
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 2.1 创建一个往文件输出日志信息的TimedRotatingFileHandler
rf_handler = logging.handlers.TimedRotatingFileHandler(filename='all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
# 创建一个格式器formatter并将其添加到处理器handler
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# 2.2 创建一个往文件输出错误信息的FileHandler
f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 2.3 创建一个往控制台打印信息的StreamHandler
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
c_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# 3 为日志器logger添加上面创建的处理器handler
logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.addHandler(c_handler)

# 4 日志输出
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')