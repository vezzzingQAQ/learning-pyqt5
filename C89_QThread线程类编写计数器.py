'''
2021.1.26,IVICX D.S. C89;QThread线程类编写计数器
'''
'''
从QThread派生子类->定义一个def run(self):方法在里面做近似的..死循环..循环一次
调用sleep休眠一秒钟
*******
在窗口上显示一个QLCDNumber,和一个按钮
点击按钮启动线程，一秒钟数1，一直到5
*******
>>【自定义信号】
通过自定义信号在两个控件之间交互
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

sec=0#计数:全局变量
class workThread(QThread):#工作线程*******************
    #编写自定义信号************************************
    timeout=pyqtSignal()#定义一个相当于timer的timeout的信号
    end=pyqtSignal()#计时结束通知主程序弹出对话框
    def run(self):
        while True:
            self.sleep(1)#休眠1秒
            if sec==5:
                self.end.emit()#发送end信号，调用与end信号绑定的槽方法
                break#退出循环
            self.timeout.emit()#循环一次发送一次timeout信号

class counter(QWidget):
    def __init__(self):
        super(counter, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("计数器")
        self.resize(300,120)

        layout=QVBoxLayout()

        self.lcd=QLCDNumber()
        self.btn=QPushButton("start count down")

        layout.addWidget(self.lcd)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        #*************************************
        self.workThread=workThread()#实例化一个工作线程

        self.btn.clicked.connect(self.btnclicked)
        self.workThread.timeout.connect(self.countTime)
        self.workThread.end.connect(self.end)

        #写两个槽方法关联信号
    def countTime(self):#改变LCD的显示数字
        global sec#声明全局变量
        sec+=1
        self.lcd.display(sec)
    def end(self):
        QMessageBox.information(self,"消息","计数结束",QMessageBox.Ok)
    def btnclicked(self):
        global sec
        sec=0
        self.workThread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = counter()
    main.show()
    sys.exit(app.exec_())
