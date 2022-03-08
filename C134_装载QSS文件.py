'''
2021.2.1,IVICX D.S. C134;装载QSS文件
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from C134_QssLoader import CommonQssLoader
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(477,258)
        self.setWindowTitle("装载QSS文件")

        vbox=QVBoxLayout()

        self.btn=QPushButton("LoadCSS")
        self.btn.setToolTip("装载CSS文件")

        vbox.addWidget(self.btn)
        self.setLayout(vbox)

        widget=QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(vbox)

        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        styleFile="./QSS/QSS1.qss"
        qssStyle=CommonQssLoader.readCss(styleFile)
        print(qssStyle)
        main.setStyleSheet(qssStyle)#提示文本变红，背景图

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

