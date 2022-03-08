'''
2021.1.30,IVICX D.S. C117;多窗口交互：使用信号和槽
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DateTimeDialog(QDialog):
    signal=pyqtSignal(str)#自定义一个信号>>指定只能传递一个字符串
    def __init__(self,parent=None):
        super(DateTimeDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DateTimeDialog")
        self.resize(200,100)

        layout=QVBoxLayout()

        self.dateTime_inner=QDateTimeEdit()
        self.dateTime_inner.setCalendarPopup(True)
        self.dateTime_inner.setDateTime(QDateTime.currentDateTime())

        self.dateTime_emit=QDateTimeEdit()
        self.dateTime_emit.setCalendarPopup(True)
        self.dateTime_emit.setDateTime(QDateTime.currentDateTime())

        self.btn1=QPushButton("确定")

        self.btn1.clicked.connect(self.closeW)

        layout.addWidget(self.dateTime_inner)
        layout.addWidget(self.dateTime_emit)
        layout.addWidget(self.btn1)
        self.setLayout(layout)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>绑定信号>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.dateTime_emit.dateTimeChanged.connect(self.emit_signal)
    def emit_signal(self):
        date_str=self.dateTime_emit.dateTime().toString()
        self.signal.emit(date_str)
    def closeW(self):
        self.close()