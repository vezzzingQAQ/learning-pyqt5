'''
2021.1.24,IVICX D.S. C67;
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class tableWidgetEXPForm(QWidget):
    def __init__(self):
        super(tableWidgetEXPForm, self).__init__()
        self.setWindowTitle("QTableWidget使用")
        self.resize(500,300)

        layout=QVBoxLayout()

        self.table=QTableWidget()
        self.table.setRowCount(4)#设置行数列数
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["姓名","年龄","籍贯"])#设置水平头标签
        #***********************************************
        nameitem=QTableWidgetItem("VEZING")
        self.table.setItem(0,0,nameitem)

        ageitem=QTableWidgetItem("166666")
        self.table.setItem(0,1,ageitem)
        #设置为禁止编辑******************************************
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #整行选中***********************************************
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        #自动调节行列大小适合内容***********************************
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()
        #显示隐藏表格头****************************************
        self.table.horizontalHeader().setVisible(True)
        self.table.verticalHeader().setVisible(True)
        #设置垂直头标签**************************************
        self.table.setVerticalHeaderLabels(["a","b"])
        #隐藏表格线***************************************
        self.table.setShowGrid(False)
        #***********************************************
        layout.addWidget(self.table)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = tableWidgetEXPForm()
    main.show()
    sys.exit(app.exec_())