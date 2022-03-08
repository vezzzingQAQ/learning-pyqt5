'''
2021.1.30,IVICX D.S. C116;多窗口交互：强耦合:子类
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DateDialog(QDialog):
    def __init__(self,parent=None):
        super(DateDialog, self).__init__(parent)

        self.setWindowTitle("DateDialog")

        layout=QVBoxLayout()

        self.dateTime=QDateTimeEdit()
        self.dateTime.setCalendarPopup(True)
        self.dateTime.setDateTime(QDateTime.currentDateTime())

        self.buttons=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel,Qt.Horizontal)
        self.buttons.accepted.connect(self.accept)#表示点击确定按钮
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(self.dateTime)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def currentDateTime(self):
        return self.dateTime.dateTime()

