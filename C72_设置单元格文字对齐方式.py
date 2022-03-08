'''
2021.1.24,IVICX D.S. C72;设置单元格文本对齐方式
'''
'''
setTextAlignment
Qt.AlignRight|Qt.AlignBottom
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random

class AliEXPForm(QWidget):
    def __init__(self):
        super(AliEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格文本对齐方式")

        layout=QVBoxLayout()

        self.table=QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(3)

        newitem=QTableWidgetItem("Vezing")
        newitem.setTextAlignment(Qt.AlignRight|Qt.AlignBottom)
        self.table.setItem(0, 0, newitem)

        newitem=QTableWidgetItem("Meiling")
        newitem.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(0, 1, newitem)

        newitem=QTableWidgetItem("RS")
        newitem.setTextAlignment(Qt.AlignRight|Qt.AlignTop)
        self.table.setItem(0, 2, newitem)

        layout.addWidget(self.table)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AliEXPForm()
    main.show()
    sys.exit(app.exec_())