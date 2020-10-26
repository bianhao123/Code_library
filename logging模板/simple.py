# -*- encoding: utf-8 -*-
'''
@File    :   simple.py
@Time    :   2020/10/25 23:34:36
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
'''

# here put the import lib
import logging

# way1
print('way1')
# 默认格式：日志级别:日志器名称:日志内容
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")


# way2
print('\nway2')
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")