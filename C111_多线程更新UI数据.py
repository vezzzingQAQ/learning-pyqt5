'''
2021.1.29,IVICX D.S. C111;多线程更新UI数据:在两个线程中传递数据
'''
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import sys

class BackenThread(QThread):#后台线程
    update=pyqtSignal(str)

    def run(self):
        while True:
            data=QDateTime.currentDateTime()
            currentTime=data.toString("yyyy-MM-dd hh:mm:ss")
            self.update.emit(str(currentTime))
            time.sleep(1)

class TimeWindow(QDialog):
    def __init__(self):
        super(TimeWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("显示时间")
        self.resize(400,100)

        self.input=QLineEdit(self)
        self.input.resize(400,100)

        self.backend=BackenThread()
        self.backend.update.connect(self.display)
        self.backend.start()

    def display(self,data):
        self.input.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TimeWindow()
    main.show()
    sys.exit(app.exec_())