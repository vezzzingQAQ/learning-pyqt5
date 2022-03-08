'''
2021.1.28,IVICX D.S. C100;让按钮永远位于窗口右下角
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class rightBottomButton(QWidget):
    def __init__(self):
        super(rightBottomButton, self).__init__()

        self.setWindowTitle("让按钮永远位于窗口右下角")
        self.resize(400,300)

        self.okbutton=QPushButton("确定")
        self.cancelbutton=QPushButton("取消")

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okbutton)
        hbox.addWidget(self.cancelbutton)

        vbox=QVBoxLayout()
        self.btn1=QPushButton("command1")
        self.btn2=QPushButton("command2")
        self.btn3=QPushButton("command3")

        vbox.addStretch(0)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = rightBottomButton()
    main.show()
    sys.exit(app.exec_())
