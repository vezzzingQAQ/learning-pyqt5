'''
2021.1.24,IVICX D.S. C71;按列排序
'''
'''
1.按哪一列排序
2.排序类型
QtabelWidget>sortItems(列索引,排序类型)
#目前好像只会文本排序...
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random

class PXEXPForm(QWidget):
    def __init__(self):
        super(PXEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("按列排序")

        layout=QVBoxLayout()

        self.table=QTableWidget()
        self.table.setRowCount(1940)
        self.table.setColumnCount(5)
        #self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        for i in range(1940):
            value=random.randint(0,1000)
            self.table.setItem(i,0,QTableWidgetItem(str(value)))
            self.table.setItem(i,1,QTableWidgetItem(random.choice(["a","b","c","d","e"])))
            for j in range(3):
                self.table.setItem(i,j+2,QTableWidgetItem(str(value*(j+1))))

        self.button=QPushButton("排序")
        self.button.clicked.connect(self.order)

        self.orderType=Qt.DescendingOrder#实例化当前的排序模式

        layout.addWidget(self.table)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def order(self):#点一次改变一次排序模式
        if self.orderType==Qt.DescendingOrder:
            self.orderType=Qt.AscendingOrder
        else:
            self.orderType=Qt.DescendingOrder
        self.table.sortItems(1,self.orderType)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PXEXPForm()
    main.show()
    sys.exit(app.exec_())