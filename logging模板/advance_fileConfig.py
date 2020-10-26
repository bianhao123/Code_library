# -*- encoding: utf-8 -*-
'''
@File    :   advance_fileConfig.py
@Time    :   2020/10/26 12:24:42
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   使用配置文件和fileConfig()函数实现日志配置
'''

# here put the import lib
import logging
import logging.config
# 读取日志配置文件内容
logging.config.fileConfig('logging.conf')

# 创建一个日志器logger
logger = logging.getLogger('simpleExample2')

# 日志输出
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')