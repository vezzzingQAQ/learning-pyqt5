'''
2021.2.1,IVICX D.S. C131;QSS标签为按钮和标签添加背景图和圆角
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LbaelButtonBackground(QWidget):
    def __init__(self):
        super(LbaelButtonBackground, self).__init__()

        self.setWindowTitle("QSS标签为按钮和标签添加背景图和圆角")

        vbox=QVBoxLayout()

        self.label1=QLabel("<>")
        self.label1.setToolTip("这是一个文本标签")
        self.label1.setStyleSheet('''QLabel{
            border-image:url(./images/x1.jpg);
        }''')#对所有label设置图片
        pix2=QPixmap("./images/x1.jpg")
        self.label1.setFixedSize(pix2.size())

        self.btn1=QPushButton()
        self.btn1.setObjectName("btn1")
        pix1=QPixmap("./images/P2.png")
        self.btn1.setFixedSize(pix1.size())

        style='''
        #btn1{
            border-radius:4px;
            background-image:url('./images/P2.png');
        }
        #btn1:Pressed{
            background-image:url('./images/P4.png');
        }
        '''#设置圆角，分别设置按下与松开的图片
        self.btn1.setStyleSheet(style)

        vbox.addWidget(self.label1)
        #vbox.addStretch()#增加空行
        vbox.addWidget(self.btn1)
        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LbaelButtonBackground()
    main.show()
    sys.exit(app.exec_())
