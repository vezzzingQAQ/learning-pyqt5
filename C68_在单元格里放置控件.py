'''
2021.1.24,IVICX D.S. C68;在单元格里放置控件
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class PlaceControlEXPForm(QWidget):
    def __init__(self):
        super(PlaceControlEXPForm, self).__init__()
        self.setWindowTitle("在单元格里放置控件")
        self.resize(500,300)

        layout=QHBoxLayout()

        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        tableWidget.setHorizontalHeaderLabels(["姓名","性别","啥啥啥"])
        #放置文本********************************************************
        textitem=QTableWidgetItem("Vzzz")
        tableWidget.setItem(0,0,textitem)#行列对象
        #放置一个下拉列表**************************************************
        combox=QComboBox()
        combox.addItem("♂")
        combox.addItem("♀")
        #QSS样式，类似CSS语法设置控件属性
        combox.setStyleSheet("QComboBox{margin:5px};")#QSS设置边距
        tableWidget.setCellWidget(0,1,combox)#添加到表格
        #放置一个按钮*****************************************************
        button=QPushButton("修改")
        button.setDown(True)#默认为按下状态
        button.setStyleSheet("QPushButton{margin:5px};")
        tableWidget.setCellWidget(0,2,button)
        #***************************************************************
        layout.addWidget(tableWidget)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PlaceControlEXPForm()
    main.show()
    sys.exit(app.exec_())