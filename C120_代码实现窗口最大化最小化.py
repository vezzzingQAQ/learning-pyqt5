'''
2021.1.30,IVICX D.S. C120;代码实现窗口最大化最小化
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class WindowMaxMin(QWidget):
    def __init__(self):
        super(WindowMaxMin, self).__init__()

        self.resize(300,400)
        self.setWindowTitle("代码实现窗口最大化最小化")
        self.setWindowFlags(Qt.WindowMaximizeButtonHint|Qt.WindowCloseButtonHint)

        layout=QVBoxLayout()

        self.maxButon=QPushButton("窗口最大化1")
        self.maxButon.clicked.connect(self.maxmized1)

        self.maxButton2=QPushButton("窗口最大化2")
        self.maxButton2.clicked.connect(self.showMaximized)

        self.minButton=QPushButton("窗口最小化")
        self.minButton.clicked.connect(self.showMinimized)

        layout.addWidget(self.maxButon)
        layout.addWidget(self.maxButton2)
        layout.addWidget(self.minButton)
        self.setLayout(layout)

    def maxmized1(self):#获取屏幕大小并填充[满屏显示没有顶栏]
        desktop=QApplication.desktop()#获得桌面
        rect=desktop.availableGeometry()#可用尺寸
        self.setGeometry(rect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowMaxMin()
    main.show()
    sys.exit(app.exec_())