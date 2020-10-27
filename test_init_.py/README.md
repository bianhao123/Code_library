
参考网址：<https://www.cnblogs.com/tp1226/p/8453854.html>

对__init__.py的认识：
    有了__init__.py文件，所在的文件夹python认为是一个模块。在用import mypackage导入模块时，python会自动执行mypackage目录的__init__.py。

    运行from mypackage import *时，会执行mypackpage下的__init__.py和导入subpackage_1和subpackage_2,同时会导入subpackage_1下的__init__.py，但不会导入相关的.py文件
