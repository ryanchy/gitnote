# PYQT示例
"""
import sys
from PyQt6.QtWidgets import (QWidget, QToolTip, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit)
from PyQt6.QtGui import QFont,QIcon,QAction
from PyQt6.QtCore import QCoreApplication
  ###***提示文本***## #
class PromptText(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        menubar = self.statusBar()#第一次调用这个方法创建了一个状态栏。随后方法返回状态栏对象。
        menubar.showMessage('Ready')
        #然后用showMessage()方法在状态栏上显示一些信息。
        exitAction = QAction(QIcon('t2.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        self.setGeometry(700, 100, 600, 600) # 窗口在屏幕上显示，并设置了它的尺寸。resize()和remove()合而为一的方法。
      # 前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        self.setWindowTitle('menubar') # 创建一个窗口标题
        self.setWindowIcon(QIcon('t1.jpg')) # 创建一个QIcon对象并接收一个我们要显示的图片路径作为参数。
        self.setToolTip('This is a <b>QMainWindow</b> widget')  # 调用setTooltip()方法创建提示框。
        # 可以在提示框中使用富文本格式。
        QToolTip.setFont(QFont('SansSerif', 10))  # 这个静态方法设置了用于提示框的字体。
        # 这里使用10px大小的SansSerif字体。
        btn = QPushButton('Button', self)  # 创建按钮
        #QPushButton(string text, QWidget parent = None)
        # text参数是将显示在按钮中的内容。
        # parent参数是一个用来放置我们按钮的组件。在下文例子中将会是QWidget组件。
        # 一个应用的组件是分层结构的。在这个分层内，大多数组件都有父类。没有父类的组件是顶级窗口。
        btn.setToolTip('This is a <b>QPushButton</b> widget')  # 设置按钮提示框
        btn.resize(btn.sizeHint())  # 改变按钮大小
        btn.move(0,0)  # 移动按钮位置
        qbtn = QPushButton('Quit', self)  # 创建了一个按钮。按钮是一个QPushButton类的实例。
        # 构造方法的第一个参数是显示在button上的标签文本。第二个参数是父组件。
        # 父组件是Example组件，它继承了QWiget类。
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 在PyQt5中，事件处理系统由信号&槽机制建立。如果我们点击了按钮，信号clicked被发送。
        # 槽可以是Qt内置的槽或Python 的一个方法调用。QCoreApplication类包含了主事件循环；
        # 它处理和转发所有事件。instance()方法给我们返回一个实例化对象。注意QCoreAppli类由QApplication创建。
        # 点击信号连接到quit()方法，将结束应用。事件通信在两个对象之间进行：发送者和接受者。
        # 发送者是按钮，接受者是应用对象。
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(500, 00)
        self.show()
        
    def closeEvent(self, event):
 
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButtons.No|
                                     QMessageBox.StandardButtons.Yes, QMessageBox.StandardButtons.No)
        if reply == QMessageBox.StandardButtons.Yes:
            event.accept()
        else:
    
            event.ignore()
# ##***Message Box***## #
class MessageBox(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        qbtn = QPushButton('Quit', self)  # 创建了一个按钮。按钮是一个QPushButton类的实例。
        # 构造方法的第一个参数是显示在button上的标签文本。第二个参数是父组件。
        # 父组件是Example组件，它继承了QWiget类。
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(500, 50)
        self.setGeometry(300, 100, 600, 600)
        self.setWindowTitle('excise')
        self.show()
 
    def closeEvent(self, event):
 
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PromptText()
    sys.exit(app.exec())
"""
# Header转字典
def header_dict(): 
    headers = dict([line.split(": ",1) for line in """{}""".format(input("输入要转换为字典的字符串:\r")).split("\n")])    
    return headers
header_dict()


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

# selenium避开反扒策略
```
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time
from pyquery import PyQuery

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get("https://blog.csdn.net/perfect_red/article/details/81562776")
js = 'window.scrollTo(0,document.body.scrollHeight)'
driver.execute_script(js)
time.sleep(5)
page_text = driver.page_source
# driver.execute_script("window.open('https://www.baidu.com')")
# driver.switch_to.window(window_name=driver.window_handles[0])
time.sleep(5)
driver.quit()
title_text = PyQuery(page_text)("title")
print(title_text.text())
```

# hook js 油猴脚本
1
油猴hook脚本可以像数组一样遍历函数名，
虽然有点碰运气但还是可以尝试。
打印出加密函数的返回值，也就是直接hook到结果。
多写了一个正则，匹配出加密函数内部调用的函数名。
```

// ==UserScript==
// @name         HOOK 二层函数名 end
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  day day up!
// @author       FY
// @include      *
// @grant        none
// @run-at       document-end
// ==/UserScript==

(function() {
    'use strict';
    var source = ['decodeData','base64decode','md5','decode','btoa','MD5','RSA','AES','CryptoJS','encrypt','strdecode',"encode",'decodeURIComponent','_t','JSON.stringify','String.fromCharCode','fromCharCode'];
    console.log("开始测试是否有解密函数");
    let realCtx, realName;
    function getRealCtx(ctx, funcName) {
        let parts = funcName.split(".");
        let realCtx = ctx;
        for(let i = 0; i < parts.length - 1; i++) {
            realCtx = realCtx[parts[i]];
        }
        return realCtx;
    }
    function getRealName(funcName) {
        let parts = funcName.split(".");
        return parts[parts.length - 1];
    }
    function hook(ctx, funcName, level, originFunc) {
        ctx[funcName] = function(a){
            console.log("level:" + level + " function:" + funcName,a);
            let regexp = / [\S]*\(.*\)\;/g;
            let match = originFunc.toString().match(regexp)
            console.log(match);
            debugger;
            return originFunc(a);
        };
    }
    function test(ctx, level) {
        for(let i = 0; i < source.length; i++) {
            let f = source[i];
            let realCtx = getRealCtx(ctx, f);
            let realName = getRealName(f);
            let chars = realCtx[realName];
            hook(realCtx, realName, level, chars);
        }
    }
    test(window, 1);
})();

```


2
##数字密码
num_dic = {"0":"呼啦圈",
"1":"蜡烛",
"2":"鹅",
"3":"耳朵",
"4":"帆船",
"5":"钩子",
"6":"勺子",
"7":"镰刀",
"8":"墨镜",
"9":"哨子",
"00":"望远镜",
"01":"小树",
"02":"铃儿",
"03":"凳子",
"04":"轿车",
"05":"手套",
"06":"手枪",
"07":"锄头",
"08":"溜冰鞋",
"09":"猫",
"10":"棒球",
"11":"梯子",
"12":"椅儿",
"13":"医生",
"14":"钥匙",
"15":"鹦鹉",
"16":"石榴",
"17":"仪器",
"18":"糖葫芦",
"19":"衣钩",
"20":"香烟",
"21":"鳄鱼",
"22":"双胞胎",
"23":"和尚",
"24":"闹钟",
"25":"二胡",
"26":"河流",
"27":"耳机",
"28":"恶霸",
"29":"饿囚",
"30":"三轮车",
"31":"鲨鱼",
"32":"扇儿",
"33":"猩猩",
"34":"三丝",
"35":"珊瑚",
"36":"山鹿",
"37":"山鸡",
"38":"妇女",
"39":"山丘",
"40":"司令",
"41":"蜥蜴",
"42":"柿儿",
"43":"石山",
"44":"蛇",
"45":"师傅",
"46":"饲料",
"47":"司机",
"48":"石板",
"49":"湿狗",
"50":"武林",
"51":"工人",
"52":"鼓儿",
"53":"乌沙帽",
"54":"青年",
"55":"火车",
"56":"蜗牛",
"57":"武器",
"58":"尾巴",
"59":"蜈蚣",
"60":"榴莲",
"61":"儿童",
"62":"牛儿",
"63":"流沙",
"64":"螺丝",
"65":"老虎",
"66":"溜溜球",
"67":"氯气",
"68":"喇叭",
"69":"太极",
"70":"麒麟",
"71":"机翼",
"72":"企鹅",
"73":"花旗参",
"74":"骑士",
"75":"西服",
"76":"汽油",
"77":"机器",
"78":"青蛙",
"79":"气球",
"80":"巴黎铁塔",
"81":"白蚁",
"82":"拉菲",
"83":"芭蕉扇",
"84":"巴士",
"85":"保姆",
"86":"八路",
"87":"白旗",
"88":"麻花辫",
"89":"八角",
"90":"酒瓶",
"91":"球衣",
"92":"球儿",
"93":"旧伞",
"94":"首饰",
"95":"酒壶",
"96":"蝴蝶",
"97":"旧旗",
"98":"酒杯",
"99":"钻石",}


input_number = input("输入数字:")
input_number_char = list(str(input_number).replace(" ", "").replace(".", ""))
output_char = ""
output_number = ""
num_len = len(input_number_char)

if num_len/2 > num_len//2:

	for i in range(num_len//2):
		# print(input_number_char[i])
		output_char += num_dic[(input_number_char[2*i] + input_number_char[2*i+1])]
		output_char += "~"
		output_number += (input_number_char[2 * i] + input_number_char[2 * i + 1])
		output_number += "~"
	output_char += num_dic[(input_number_char[2*i + 2])]
else:
	for i in range(num_len // 2):
		# print(input_number_char[i])
		output_char += num_dic[(input_number_char[2 * i] + input_number_char[2 * i + 1])]
		output_char += "~"
		output_number += (input_number_char[2 * i] + input_number_char[2 * i + 1])
		output_number += "~"
print(output_number)
print(output_char)
