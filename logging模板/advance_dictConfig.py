# -*- encoding: utf-8 -*-
'''
@File    :   advance_dictConfig.py
@Time    :   2020/10/26 15:03:08
@Author  :   bianhao 
@Contact :   2017212127@mail.hfut.edu.cn
@Desc    :   None
'''

# here put the import lib
import logging
import logging.config
import yaml

with open('logging.yml', 'r') as f_conf:
    dict_conf = yaml.load(f_conf)
logging.config.dictConfig(dict_conf)

logger = logging.getLogger('simpleExample')
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

rootLogger = logging.getLogger()
rootLogger.debug('rootLogger debug message')
rootLogger.info('rootLogger info message')
rootLogger.warn('rootLogger warn message')
rootLogger.error('rootLogger error message')
rootLogger.critical('rootLogger critical message')