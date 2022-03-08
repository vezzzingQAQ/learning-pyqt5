'''
2021.1.26,IVICX D.S. C87;QTimer多线程
'''
'''
耗时任务不要放到主线程（槽事件）防止阻塞
多CPU，单CPU代码无区别，底层自动调用
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QTimerEXPForm(QWidget):
    def __init__(self):
        super(QTimerEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTimer计时器")

        self.numbercount=0

        layout=QGridLayout()

        self.label=QLabel("<显示当前时间>")
        self.lcd=QLCDNumber()
        self.startButton=QPushButton("开始计时")
        self.stopButton=QPushButton("停止计时")

        self.startButton.clicked.connect(self.startTimer)
        self.stopButton.clicked.connect(self.stopTimer)
        #****************************************
        self.timer=QTimer()
        self.timer.timeout.connect(self.showtime)
        #****************************************

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.lcd,1,0,1,2)
        layout.addWidget(self.startButton,2,0)
        layout.addWidget(self.stopButton,2,1)

        self.setLayout(layout)

    def showtime(self):
        time=QDateTime.currentDateTime()
        timedisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")#格式化
        self.label.setText(timedisplay)
        self.numbercount+=1
        self.lcd.display(self.numbercount)

    def startTimer(self):
        self.timer.start(1)
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)

    def stopTimer(self):
        self.timer.stop()
        self.stopButton.setEnabled(False)
        self.startButton.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QTimerEXPForm()
    main.show()
    sys.exit(app.exec_())

