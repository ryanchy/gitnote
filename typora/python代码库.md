

# xrang迭代器

```
def xrange(min,max=0):
    o = 0
    if max == 0:
        while o < min:
            yield o
            o += 1
    else:
        if min < max:
            while min < max:
                yield min
                min += 1
        else:
            print("输入值非法")
```

# logging用法

```
import logging  #导入logging模块
logger = logging.getLogger(__name__)#创建logger对象
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(massage)s')#统一日志格式

# 参数：作用

# %(levelno)s：打印日志级别的数值

# %(levelname)s：打印日志级别的名称

# %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]

# %(filename)s：打印当前执行程序名

# %(funcName)s：打印日志的当前函数

# %(lineno)d：打印日志的当前行

# %(asctime)s：打印日志的时间

# %(thread)d：打印线程ID

# %(threadName)s：打印线程名称

#%(process)d：打印进程ID
#%(message)s：打印日志信息
FD = logging.FileHandler("1.log")#创建日志文件处理对象
SD = logging.StreamHandler()#创建控制台日志处理对象
logger.setLevel(logging.DEBUG)
logger.addHandler(FD)
logger.addHandler(SD)
logger.debug("let us go")
# logger.info("show info message")
#抓取traceback
try: 
    pass   
except Exception:
#     logger.exception("something error")
    logger.error("soemthing wrong",exc_info=True)

# logger.info("show info message")
"""pytest.ini中添加如下代码：
[pytest]
log_cli = true
log_cli_level = DEBUG
log_format = %(asctime)s (%(filename)-16s:%(lineno)-3s) %(levelname)-8s %(message)s
log_date_format = %Y-%M-%D %H:%M:%S
"""

```

