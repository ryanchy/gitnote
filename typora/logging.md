# python的logging日志模块(二)

![img](https://csdnimg.cn/release/blogv2/dist/pc/img/reprint.png)

[langb2014](https://langbin.blog.csdn.net/) 2016-11-29 19:04:14 ![img](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes.png) 9522 ![img](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect.png) 收藏 3

分类专栏： [Python](https://blog.csdn.net/langb2014/category_2495401.html)

晚上比较懒，直接搬砖了。



### 1.简单的将日志打印到屏幕

 

```
import logginglogging.debug('This is debug message')logging.info('This is info message')logging.warning('This is warning message')` `**屏幕上打印:**WARNING:root:This is warning message
```



默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。

### 2.通过logging.basicConfig函数对日志的输出格式及方式做相关配置

```
import logginglogging.basicConfig(level=logging.DEBUG,        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',        datefmt='%a, %d %b %Y %H:%M:%S',        filename='myapp.log',        filemode='w')  logging.debug('This is debug message')logging.info('This is info message')logging.warning('This is warning message')` `**./myapp.log文件中内容为:**Sun, 24 May 2009 21:48:54 demo2.py[line:11] DEBUG This is debug messageSun, 24 May 2009 21:48:54 demo2.py[line:12] INFO This is info messageSun, 24 May 2009 21:48:54 demo2.py[line:13] WARNING This is warning message
```

logging.basicConfig函数各参数:
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

### 3.将日志同时输出到文件和屏幕

```
import logginglogging.basicConfig(level=logging.DEBUG,        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',        datefmt='%a, %d %b %Y %H:%M:%S',        filename='myapp.log',        filemode='w')##################################################################################################定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#console = logging.StreamHandler()console.setLevel(logging.INFO)formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')console.setFormatter(formatter)logging.getLogger('').addHandler(console)#################################################################################################logging.debug('This is debug message')logging.info('This is info message')logging.warning('This is warning message')` `**屏幕上打印:**root    : INFO   This is info messageroot    : WARNING This is warning message``***\*./myapp.log文件中内容为:\** **Sun, 24 May 2009 21:48:54 demo2.py[line:11] DEBUG This is debug messageSun, 24 May 2009 21:48:54 demo2.py[line:12] INFO This is info messageSun, 24 May 2009 21:48:54 demo2.py[line:13] WARNING This is warning message
```

### 4.logging之日志回滚

```
import loggingfrom logging.handlers import RotatingFileHandler##################################################################################################定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10MRthandler = RotatingFileHandler('myapp.log', maxBytes=10*1024*1024,backupCount=5)Rthandler.setLevel(logging.INFO)formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')Rthandler.setFormatter(formatter)logging.getLogger('').addHandler(Rthandler)################################################################################################
```

从上例和本例可以看出，logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的。
logging的几种handle方式如下：

 

logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件 logging.FileHandler: 日志输出到文件日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler logging.handlers.BaseRotatingHandler logging.handlers.RotatingFileHandler logging.handlers.TimedRotatingFileHandlerlogging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets logging.handlers.DatagramHandler: 远程输出日志到UDP sockets logging.handlers.SMTPHandler: 远程输出日志到邮件地址 logging.handlers.SysLogHandler: 日志输出到syslog logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志 logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器

 

由于StreamHandler和FileHandler是常用的日志处理方式，所以直接包含在logging模块中，而其他方式则包含在logging.handlers模块中，
上述其它处理方式的使用请参见python2.5手册！

### 5.通过logging.config模块配置日志

```
#logger.conf``###############################################``[loggers]keys=root,example01,example02``[logger_root]level=DEBUGhandlers=hand01,hand02``[logger_example01]handlers=hand01,hand02qualname=example01propagate=0``[logger_example02]handlers=hand01,hand03qualname=example02propagate=0``###############################################``[handlers]keys=hand01,hand02,hand03``[handler_hand01]class=StreamHandlerlevel=INFOformatter=form02args=(sys.stderr,)``[handler_hand02]class=FileHandlerlevel=DEBUGformatter=form01args=('myapp.log', 'a')``[handler_hand03]class=handlers.RotatingFileHandlerlevel=INFOformatter=form02args=('myapp.log', 'a', 10*1024*1024, 5)``###############################################``[formatters]keys=form01,form02``[formatter_form01]format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)sdatefmt=%a, %d %b %Y %H:%M:%S``[formatter_form02]format=%(name)-12s: %(levelname)-8s %(message)sdatefmt=
```

上例3：

```
import loggingimport logging.configlogging.config.fileConfig("logger.conf")logger = logging.getLogger("example01")logger.debug('This is debug message')logger.info('This is info message')logger.warning('This is warning message')
```

上例4：

```
import loggingimport logging.configlogging.config.fileConfig("logger.conf")logger = logging.getLogger("example02")logger.debug('This is debug message')logger.info('This is info message')logger.warning('This is warning message')
```

### 6.logging是线程安全的

from:http://blog.csdn[.NET](http://lib.csdn.net/base/dotnet)/yatere/article/details/6655445

原文地址：[Python 模块 Logging HOWTO 官方文档](https://docs.python.org/2/howto/logging.html)

## 一、Logging简介

Logging是一种当软件运行时对事件的追踪记录方式，软件开发者通过在代码中调用Logging的相关方法来提示某些事件的发生。事件可以通过描述信息描述，当然描述信息中也可以包含变量，因为对于事件的每次触发，描述信息可能不同。

## 二、简单的例子

一个简单的例子：

```
import logging



logging.warning('Watch out!')  # 信息会打印到控制台



logging.info('I told you so')  # 不会打印任何信息，因为默认级别高于info1234
```

如果你将上述代码存入[Python](http://lib.csdn.net/base/python)文件，然后运行：

```
WARNING:root:Watch out!
12
```

INFO的信息没有出现在控制台，**因为默认的级别为WARNING高于INFO**。日志信息包含日志级别和事件描述信息，暂且别太在意输出中的root，稍后会有介绍。实际的输出可以让你任意的定制，格式设置会在稍后介绍。

## 三、将日志信息存入文件

在应用中我们常常需要将日志信息存入文件。请重新创建一个新文件，不要接在上面的python文件中。

```
import logging



logging.basicConfig(filename='example.log',level=logging.DEBUG)



logging.debug('This message should go to the log file')



logging.info('So should this')



logging.warning('And this, too')123456
```

运行他，然后会生成一个日志文件example.log，打开它就能看到具体的日志信息：

```
DEBUG:root:This message should go to the log file



INFO:root:So should this



WARNING:root:And this, too1234
```

在这个例子中，我们看到了如何设置日志级别，**这是一个阈值**，用于控制日志的输出。
如果你想要通过命令行来设置日志级别，你可以这样做：

```
--log=INFO
12
```

并且 你也可以获取传递给–log的参数，你可以这样做：

```
getattr(logging, loglevel.upper())
12
```

你可以通过basicConfig()方法来设置日志级别——传递level参数。你可能想要检查level参数值的合法性，可以像下面这样：

```
# assuming loglevel is bound to the string value obtained from the



# command line argument. Convert to upper case to allow the user to



# specify --log=DEBUG or --log=debug



numeric_level = getattr(logging, loglevel.upper(), None)



if not isinstance(numeric_level, int):



    raise ValueError('Invalid log level: %s' % loglevel)



logging.basicConfig(level=numeric_level, ...)12345678
```

basicConfig()方法的调用先于debug(),info()等方法。因为它是一次性的工作：第一次调用是有效的，后面的调用都是无效的空操作。

如果你多次运行上面的代码，日志信息会追加到原有的日志信息上。如果你想要每次的日志信息都覆盖掉之前的，那么可以通过配置filemode参数为’w’即可：

```
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
12
```

新的日志信息会覆盖掉旧的。

## 四、多模块Logging

如果你的工程包含多个模块，你可以像下面的这种方式组织logging：

```
# myapp.py



import logging



import mylib



 



def main():



    logging.basicConfig(filename='myapp.log', level=logging.INFO)



    logging.info('Started')



    mylib.do_something()



    logging.info('Finished')



 



if __name__ == '__main__':



    main()12345678910111213
```

–

```
# mylib.py



import logging



 



def do_something():



    logging.info('Doing something')123456
```

如果你运行myapp.py，你会在myqpp.log中看到如下信息：

```
INFO:root:Started



INFO:root:Doing something



INFO:root:Finished1234
```

这正是你想要看到的。你可以将他们组织到你的多个模块中，通过使用mylib.py的模板。注意：使用这种方式，除了通过查看事件描述，你不能判断这个信息从何而来。如果你想要追踪信息来源，你需要参照更加高级的教程-[Logging进阶](http://test.com/)

## 五、Logging变量信息

为了生成包含变量的日志，你需要使用**格式化的字符串**，通过将变量当成参数传递给描述信息，例如：

```
import logging



logging.warning('%s before you %s', 'Look', 'leap!')123
```

会生成：

```
WARNING:root:Look before you leap!
12
```

正如你看到的，通过使用格式化字符创将变量合并到描述信息中。这种方式是向后兼容的：logging包中有更新的格式化可选方法，例如str.format() and string.Template。这些新的格式化方法都是支持的，但是研究它们的使用不在本文的讨论范围内。

## 六、修改显示日志信息的格式

你可以更改显示日志信息的格式，像这样：

```
import logging



logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)



logging.debug('This message should appear on the console')



logging.info('So should this')



logging.warning('And this, too')123456
```

运行代码会打印出：

```
DEBUG:This message should appear on the console



INFO:So should this



WARNING:And this, too1234
```

注意到没有？先前出现在日志信息中的root不见了！你可以通过格式化方式生成几乎全部的东西，这部分内容你可以参考LogRecord的文档。但是对于简单的应用，你只需要知道日志级别，日志信息（包含变量的日志信息），或者再加上事件的发生时间。这些将在下一节中讲到。

## 七、在日志信息中显示日期时间

为了在日志信息中显示日期时间，你需要使用**%(asctime)s**格式字符串。例如：

```
import logging



logging.basicConfig(format='%(asctime)s %(message)s')



logging.warning('is when this event was logged.')1234
```

运行会生成：

```
2010-12-12 11:41:42,612 is when this event was logged.
12
```

默认的日期时间显示标准是ISO8601。如果你想要定制自己的格式，可以通过传递参数datefmt给basicConfig()方法，如下：

```
import logging



logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



logging.warning('is when this event was logged.')1234
```

会生成：

```
12/12/2010 11:46:36 AM is when this event was logged.   
12
```

datefmt参数的格式和[time.strftime()](https://docs.python.org/2/library/time.html#time.strftime)是相似的。

以上是Logging 的基础教程，如果你的需求比较简单，上面介绍的用法应该能够满足你的需求。

如果想更深入了解Logging模块请转到Logging高级教程。

# 常用handlers的使用





## 一、StreamHandler

流handler——包含在logging模块中的三个handler之一。

能够将日志信息输出到sys.stdout, sys.stderr 或者类文件对象（更确切点，就是能够支持write()和flush()方法的对象）。

只有一个参数：

```
class logging.StreamHandler(stream=None)
```

日志信息会输出到指定的stream中，如果stream为空则默认输出到sys.stderr。

## 二、FileHandler

logging模块自带的三个handler之一。继承自StreamHandler。将日志信息输出到磁盘文件上。

构造参数：

```
class logging.FileHandler(filename, mode='a', encoding=None, delay=False)
```

模式默认为append，delay为true时，文件直到emit方法被执行才会打开。默认情况下，日志文件可以无限增大。

## 三、NullHandler

空操作handler，logging模块自带的三个handler之一。
没有参数。

## 四、WatchedFileHandler

位于logging.handlers模块中。用于监视文件的状态，如果文件被改变了，那么就关闭当前流，重新打开文件，创建一个新的流。由于newsyslog或者logrotate的使用会导致文件改变。这个handler是专门为[Linux](http://lib.csdn.net/base/linux)/unix系统设计的，因为在windows系统下，正在被打开的文件是不会被改变的。
参数和FileHandler相同：

```
class logging.handlers.WatchedFileHandler(filename, mode='a', encoding=None, delay=False)
```

## 五、RotatingFileHandler

位于logging.handlers支持循环日志文件。

```
class logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0)
```

参数maxBytes和backupCount允许日志文件在达到maxBytes时rollover.当文件大小达到或者超过maxBytes时，就会新创建一个日志文件。上述的这两个参数任一一个为0时，rollover都不会发生。也就是就文件没有maxBytes限制。backupcount是备份数目，也就是最多能有多少个备份。命名会在日志的base_name后面加上.0-.n的后缀，如example.log.1,example.log.1,…,example.log.10。当前使用的日志文件为base_name.log。

## 六、TimedRotatingFileHandler

定时循环日志handler，位于logging.handlers，支持定时生成新日志文件。

```
class logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False)
```

参数when决定了时间间隔的类型，参数interval决定了多少的时间间隔。如when=‘D’，interval=2，就是指两天的时间间隔，backupCount决定了能留几个日志文件。超过数量就会丢弃掉老的日志文件。

when的参数决定了时间间隔的类型。两者之间的关系如下：

```
 'S'         |  秒







 'M'         |  分



 



 'H'         |  时







 'D'         |  天



 



 'W0'-'W6'   |  周一至周日







 'midnight'  |  每天的凌晨
```

utc参数表示UTC时间。

## 七、其他handler——SocketHandler、DatagramHandler、SysLogHandler、NtEventHandler、SMTPHandler、MemoryHandler、HTTPHandler

这些handler都不怎么常用，所以具体介绍就请参考官方文档 [其他handlers](https://docs.python.org/2/library/logging.handlers.html)

下面使用简单的例子来演示handler的使用：

## 例子一——不使用配置文件的方式（StreamHandler）：

```
import logging



 



# set up logging to file - see previous section for more details



logging.basicConfig(level=logging.DEBUG,



                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',



                    datefmt='%m-%d %H:%M',



                    filename='/temp/myapp.log',



                    filemode='w')



# define a Handler which writes INFO messages or higher to the sys.stderr



# 



console = logging.StreamHandler()



console.setLevel(logging.INFO)



# set a format which is simpler for console use



#设置格式



formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')



# tell the handler to use this format



#告诉handler使用这个格式



console.setFormatter(formatter)



# add the handler to the root logger



#为root logger添加handler



logging.getLogger('').addHandler(console)



 



# Now, we can log to the root logger, or any other logger. First the root...



#默认使用的是root logger



logging.info('Jackdaws love my big sphinx of quartz.')



 



# Now, define a couple of other loggers which might represent areas in your



# application:



 



logger1 = logging.getLogger('myapp.area1')



logger2 = logging.getLogger('myapp.area2')



 



logger1.debug('Quick zephyrs blow, vexing daft Jim.')



logger1.info('How quickly daft jumping zebras vex.')



logger2.warning('Jail zesty vixen who grabbed pay from quack.')



logger2.error('The five boxing wizards jump quickly.')
```

输出到控制台的结果：

```
root        : INFO     Jackdaws love my big sphinx of quartz.



myapp.area1 : INFO     How quickly daft jumping zebras vex.



myapp.area2 : WARNING  Jail zesty vixen who grabbed pay from quack.



myapp.area2 : ERROR    The five boxing wizards jump quickly.
```

## 例子二——使用配置文件的方式(TimedRotatingFileHandler) :

log.conf 日志配置文件：

```
[loggers]



keys=root,test.subtest,test



 



[handlers]



keys=consoleHandler,fileHandler



 



[formatters]



keys=simpleFormatter



 



[logger_root]



level=INFO



handlers=consoleHandler,fileHandler



 



[logger_test]



level=INFO



handlers=consoleHandler,fileHandler



qualname=tornado



propagate=0



 



[logger_test.subtest]



level=INFO



handlers=consoleHandler,fileHandler



qualname=rocket.raccoon



propagate=0



 



[handler_consoleHandler] #输出到控制台的handler



class=StreamHandler



level=DEBUG



formatter=simpleFormatter



args=(sys.stdout,)



 



[handler_fileHandler] #输出到日志文件的handler



class=logging.handlers.TimedRotatingFileHandler



level=DEBUG



formatter=simpleFormatter



args=('rocket_raccoon_log','midnight')



 



[formatter_simpleFormatter]



format=[%(asctime)s-%(name)s(%(levelname)s)%(filename)s:%(lineno)d]%(message)s



datefmt=



 



logging.config.fileConfig('conf/log.conf')



logger = getLogging()
```

获取logger方法：

```
def getLogging():



    return logging.getLogger("test.subtest")
```

配置logger并且调用：

```
logging.config.fileConfig('conf/log.conf')



logger = getLogging()



logger.info("this is an example!")
```

控制台和日志文件中都会输出：

```
[2016-07-01 09:22:06,470-test.subtest(INFO)main.py:55]this is an example!
```



[Python](http://lib.csdn.net/base/python) 模块中的logging模块的handlers大致介绍就是这样。

在配置文件中为Logger配置多个handler



## 使用样例

读取配置文件：

```
logging.config.fileConfig("log.conf")    # 采用配置文件  
12
```

创建logger：

```
logger = logging.getLogger("simpleExample")  
12
```

log.conf文件：

```
[loggers] #loggers列表



keys=root,main



 



[handlers] #handlers列表



keys=consoleHandler,fileHandler



 



[formatters] #formatters列表



keys=fmt



 



[logger_root] #root logger



level=DEBUG



handlers=consoleHandler,fileHandler #将root logger的日志信息输出到文件和控制台



 



[logger_main] #main logger



level=DEBUG



qualname=main



handlers=fileHandler



 



[handler_consoleHandler] #控制台handler



class=StreamHandler



level=DEBUG



formatter=fmt



args=(sys.stdout,)



 



[handler_fileHandler] #循环日志文件



class=logging.handlers.RotatingFileHandler



level=DEBUG



formatter=fmt



args=('tst.log','a',20000,5,) #参数是RotatingFileHandler的__init__()的参数



 



[formatter_fmt] #格式



format=%(asctime)s - %(name)s - %(levelname)s - %(message)s



datefmt=12345678910111213141516171819202122232425262728293031323334
```

上述文件中，用逗号将handler隔开就可以将日志输出到多个目的地：

```
handlers=consoleHandler,fileHandler #将root logger的日志信息输出到文件和控制台
12
```

=========================================================================================================

参考：

http://blog.csdn.net/yypsober/article/details/51775787

http://blog.csdn.net/yypsober/article/details/51782281

http://blog.csdn.net/yypsober/article/details/51800120

http://blog.csdn.net/yypsober/article/details/50832754