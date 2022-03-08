'''
2021.1.30,IVICX D.S. C117;多窗口交互：使用信号和槽
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from C117_DateDialogClass import DateTimeDialog
class MultiWindow2(QWidget):
    def __init__(self):
        super(MultiWindow2, self).__init__()

        self.resize(400,90)
        self.setWindowTitle("多窗口交互：使用信号和槽")

        grid=QGridLayout()

        self.openBtn=QPushButton("获取时间")
        self.lineEdit_inner=QLineEdit()
        self.lineEdit_emit=QLineEdit()

        self.lineEdit_inner.setText("接收子窗口内置信号")
        self.lineEdit_emit.setText("接收子窗口自定义信号")

        self.openBtn.clicked.connect(self.openDialog)

        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)
        grid.addWidget(self.openBtn)
        self.setLayout(grid)
    def openDialog(self):
        dialog=DateTimeDialog(self)
        dialog.dateTime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        dialog.signal.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self,date):
        self.lineEdit_inner.setText(date.toString())
    def deal_emit_slot(self,date):
        self.lineEdit_emit.setText(date)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MultiWindow2()
    main.show()
    sys.exit(app.exec_())