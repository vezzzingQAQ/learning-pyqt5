'''
2021.1.31,IVICX D.S. C122;QSS基础
'''
'''
QSS:Qt Style Sheets
Qt样式表
用于设置控件的样式
ex:设置所有或一个button的背景色
'''
import sys
from PyQt5.QtWidgets import *

class BasicQss(QWidget):
    def __init__(self):
        super(BasicQss, self).__init__()

        self.setWindowTitle("QSS基础")

        layout=QVBoxLayout()

        self.btn1=QPushButton("COMMAND1")
        self.btn2=QPushButton("COMMAND2")

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BasicQss()
    #在这里修改所有控件的QSS样式**************************
    qssStyle='''
        QPushButton{
            background-color:blue
        }
    '''
    main.setStyleSheet(qssStyle)
    #*************************************************
    main.show()
    sys.exit(app.exec_())