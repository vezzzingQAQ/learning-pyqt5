'''
2021.1.24,IVICX D.S. C73;合并单元格
2021.1.24,IVICX D.S. C74;设置单元格尺寸
'''
'''
QTableWidget.setSpan(起始行,起始列,要合并的行数，要合并的列数)
鼠标拉动可以改变单元格尺寸
单元格高宽改变只能改变整行整列
'''
from PyQt5.QtWidgets import *
import sys

class spanEXPForm(QWidget):
    def __init__(self):
        super(spanEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("合并单元格,改变单元格大小")

        layout=QVBoxLayout()

        self.table=QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(5)
        #改变单元格大小**********************************************
        self.table.setColumnWidth(4,80)
        self.table.setRowHeight(4,120)

        newitem=QTableWidgetItem("VEZING")
        self.table.setItem(0, 0, newitem)
        self.table.setSpan(0,0,3,1)#3行1列>>>>>>>>>>>>>>>>>>>>>>>>>

        newitem=QTableWidgetItem("VEZINh")
        self.table.setItem(0, 1, newitem)
        self.table.setSpan(0,1,2,1)#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        newitem=QTableWidgetItem("VEZINj")
        self.table.setItem(0, 2, newitem)

        layout.addWidget(self.table)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = spanEXPForm()
    main.show()
    sys.exit(app.exec_())