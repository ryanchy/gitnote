python logging 多进程/线程 使用方式

hx0hx 2018-02-13 08:32:06  5568  收藏 2
分类专栏： Python 文章标签： Python logging 日志模块 多进程 多线程
版权
0. 删除旧日志的工作务必交给操作系统的管理脚本执行，这样可以根据程序部署数量和磁盘空间随时调整保留量，而不需要改日志配置文件后重启程序。（神马？程序可以做到监控配置文件更改后重新载入？有这功夫写点别的代码不好吗）

1. UNIX/Linux 推荐使用 logging.handlers.WatchedFileHandler ，然后用shell脚本切割日志。

2. Windows 不支持 WatchedFileHandler ，可以写一个独立的logging进程统一打日志，其他进程将日志内容传入它的管道或者socket。

3. 还可以每个进程/线程写入自己的文件，就不会冲突啦。

trhandler = logging.handlers.TimedRotatingFileHandler('这里写唯一的文件名', when='midnight')
formatter = logging.Formatter("%(asctime)s - %(process)d:%(thread)d - %(name)s - %(levelname)s : %(message)s")
trhandler.setFormatter(formatter)
logger.addHandler(trhandler)
可是在代码里面设置日志策略并不是好的实践，想改策略的时候还得改代码，但是用配置文件，文件名是固定的啊。

如何在用配置文件的同时还能实现自定义文件名呢？

看一下 logging.FileHandler 的代码发现，配置文件里面的 filename 参数会被存入 baseFilename 属性：

self.baseFilename = os.path.abspath(filename)
这就是要写入日志的文件名了，那么我们只需要修改 baseFilename 就可以实现改名的目的了。


配置文件如下 test.yaml

---

version: 1

disable_existing_loggers: False

formatters:

    simple:
        format: "%(asctime)s - %(process)d:%(thread)d - %(name)s - %(levelname)s : %(message)s"

handlers:

    console:
        class: logging.StreamHandler
        stream: ext://sys.stdout
        level: INFO
        formatter: simple
    
    test_handler:
        class: logging.handlers.TimedRotatingFileHandler
        filename: ../log/testRename
        when: M
        interval: 5
        encoding: utf8
        delay: True  # 注意：这个参数必须设置成 True
        level: NOTSET
        formatter: simple

loggers:

    test:
        level: DEBUG
        handlers: [test_handler, console]
        propagate: False
    
    ..:
        level: INFO
        handlers: [console]
        propagate: False

...
代码如下：

import yaml
import logging.config

with open('../conf/test.yaml', 'r') as fd:
    conf = yaml.load(fd)

logging.config.dictConfig(conf)
logger = logging.getLogger("test")

logger.handlers[0].baseFilename += '唯一的后缀'  # 只需要多写这一行，就把文件名改了
delay 参数必须设置成 True，让 logger 在实际写日志的时候才创建文件，这样日志文件的名字才是修改后的文件名。如果是 False， logger 加载完成了就创建文件，文件名还是 filename，所有的进程/线程都把日志写进去，第一次轮换之后才写各自的文件。



4. 如果就想让多进程/线程写同一个文件，还能轮换的时候不出错，怎么办呢？

先研究一下为什么多进程/线程使用环境下 切换日志会出错

TimedRotatingFileHandler 和 RotatingFileHandler 的切换日志的函数 doRollover() 会根据 baseFilename 拼接一个新的文件名，把 baseFilename 文件改名，再以追加的方式打开一个新的 baseFilename 文件继续写日志，实现日志切换。

        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, timeTuple))  # 新文件名
        if os.path.exists(dfn):  # 如果 dfn 已存在，先删掉
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)  # 改名

比如线程1、2正在同时写 baseFilename，线程1开始改名，

Windows 下是改名失败（不让重命名正在使用的文件），线程1卡住了；

UNIX/Linux 下会改名成功，线程1开始写新建的 baseFilename 文件，线程2正在写的文件变成了 dfn，当线程2要改名的时候，发现 dfn 已经存在，会删掉它，【日志丢失！！！】，然后把 baseFilename 改名为 dfn，此时线程1正在写的文件变成了 dfn，线程2开始写新建的 baseFilename 文件，然后它俩就轮流删日志！！！





受这篇文章的启发，我们只需要改变一下切换日志的方式就可以避免这些问题了，（我这个写法比较偷懒）

import os, time
from logging.handlers import TimedRotatingFileHandler

class ConcurrentTRFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False,
                 atTime=None):
        TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay, utc, atTime)

        self.origin_filename = filename
     
    def getFilesToDelete(self):
        """
        Determine the files to delete when rolling over.
        More specific than the earlier method, which just used glob.glob().
        """
        dirName, baseName = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []
        prefix = self.origin_filename + "."  # 这里就不能用 baseName 了
        plen = len(prefix)
        for fileName in fileNames:
            if fileName[:plen] == prefix:
                suffix = fileName[plen:]
                if self.extMatch.match(suffix):
                    result.append(os.path.join(dirName, fileName))
        result.sort()
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result
     
    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        if self.utc:
            timeTuple = time.gmtime()
        else:
            timeTuple = time.localtime()
        
        # 以追加方式打开新的日志文件，没有改名和删除操作就不会冲突报错了。
        self.baseFilename = self.rotation_filename(os.path.abspath(self.origin_filename) + "." +
                                                   time.strftime(self.suffix, timeTuple))
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt
然后配置文件里改用 ConcurrentTRFileHandler ， delay: True ，然后代码里写上

logger.handlers[0].baseFilename += 时间戳
这样子正在写的文件名是 filename+时间戳。从使用上来说略有不便，要看最新的日志还得找到最新的文件。


按文件大小切换的已经有一个 ConcurrentLogHandler 了，pip install ConcurrentLogHandler
————————————————
版权声明：本文为CSDN博主「hx0hx」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/hx0hx/article/details/79319874