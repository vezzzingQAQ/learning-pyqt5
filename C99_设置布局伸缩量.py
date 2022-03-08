'''
2021.1.27,IVICX D.S. C99;设置布局伸缩量
'''
'''
addStretch()方法
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class stretch(QWidget):
    def __init__(self):
        super(stretch, self).__init__()
        self.setWindowTitle("设置布局伸缩量")

        layout=QHBoxLayout()

        self.btn1=QPushButton("command1")
        self.btn2=QPushButton("command2")
        self.btn3=QPushButton("command3")

        #layout.addStretch(1)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addStretch(2)
        layout.addWidget(self.btn3)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = stretch()
    main.show()
    sys.exit(app.exec_())