'''
2021.1.24,IVICX D.S. C70;设置单元格字体和颜色
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class CFsettingsEXPForm(QWidget):
    def __init__(self):
        super(CFsettingsEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格字体和颜色")

        layout=QVBoxLayout()

        self.table=QTableWidget()
        self.table.setRowCount(40)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["啥","啥","啥","啥"])

        #设置字体***************************************************
        newItem=QTableWidgetItem("Vezing")
        #字体，字号，相应的设置
        newItem.setFont(QFont("Times",14,QFont.Bold))
        #设置字的颜色************************************************
        newItem.setForeground(QBrush(QColor(0,0,255)))
        #**********************************************************
        self.table.setItem(0, 0, newItem)
        #设置背景色*************************************************
        newItem=QTableWidgetItem("Meiling")
        newItem.setBackground(QBrush(QColor(100,100,0)))
        self.table.setItem(0,1,newItem)
        #**********************************************************
        layout.addWidget(self.table)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CFsettingsEXPForm()
    main.show()
    sys.exit(app.exec_())