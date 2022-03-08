'''
2021.1.24,IVICX D.S. C75;图文混排单元格
2021.1.24,IVICX D.S. C76;改变单元格中图片尺寸
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class cellImageEXPForm(QWidget):
    def __init__(self):
        super(cellImageEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("图文混排单元格,改变单元格中图片尺寸")

        layout=QVBoxLayout()

        self.table=QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["图片再这里显示","不在这里","不在这里","不在这里"])
        #修改图片显示大小************************************************************
        self.table.setIconSize(QSize(300,300))
        #将单元格宽高修改至于图片一样**************************************************************
        for i in range(4):
            self.table.setColumnWidth(i,350)
        for i in range(5):
            self.table.setRowHeight(i,300)

        newitem=QTableWidgetItem(QIcon("images/2.BMP"), "这是图片")#图片,显示的文本
        self.table.setItem(0,0,newitem)


        layout.addWidget(self.table)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = cellImageEXPForm()
    main.show()
    sys.exit(app.exec_())