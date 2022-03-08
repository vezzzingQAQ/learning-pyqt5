'''
2021.1.24,IVICX D.S. C77;显示上下文菜单
'''
'''
1.弹出菜单
2.在满足条件的情况下弹出菜单
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random

class ContextMenuImageEXPForm(QWidget):
    def __init__(self):
        super(ContextMenuImageEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("显示上下文菜单")

        layout=QVBoxLayout()

        self.table=QTableWidget()
        self.table.setRowCount(50)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["按这一列","按这一列","不在这里"])

        for i in range(50):
            for j in range(3):
                itema=random.choice(["A","B","C","D","E","F"])
                self.table.setItem(i,j,QTableWidgetItem(itema))
        #********************************************************************
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)#允许右键弹出菜单
        self.table.customContextMenuRequested.connect(self.generateMenu)
        #绑定右键点击请求菜单事件##

        layout.addWidget(self.table)
        self.setLayout(layout)

    def generateMenu(self,pos):#第二位是传进来的鼠标坐标
        for i in self.table.selectionModel().selection().indexes():
            cNum=i.column()
            rNum=i.row()
        if cNum<=1:#弹出菜单
            menu=QMenu()
            item1=menu.addAction("菜单项1")
            item2=menu.addAction("菜单项2")
            item3=menu.addAction("菜单项3")
            screenPos=self.table.mapToGlobal(pos)
            #坐标转换成整个屏幕确保弹出位置为单击处
            #被阻塞除非单击某个菜单项
            action=menu.exec(screenPos)
            if action==item1:
                print('选择了第一个菜单项',self.table.item(rNum,cNum).text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ContextMenuImageEXPForm()
    main.show()
    sys.exit(app.exec_())