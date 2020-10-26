https://www.cnblogs.com/yyds/p/6901864.html

日志等级是从上到下依次升高的，即：DEBUG < INFO < WARNING < ERROR < CRITICAL，而日志的信息量是依次减少的


**组件名称	对应类名	功能描述
日志器	Logger	提供了应用程序可一直使用的接口
处理器	Handler	将logger创建的日志记录发送到合适的目的输出
过滤器	Filter	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器	Formatter	决定日志记录的最终输出格式**

1.使用Python代码显式的创建loggers, handlers和formatters并分别调用它们的配置函数；
2.创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容；
3.创建一个包含配置信息的dict，然后把它传递个dictConfig()函数；

