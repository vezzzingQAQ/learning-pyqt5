'''
2021.1.31,IVICX D.S. C123;QSS选择器
'''
import sys
from PyQt5.QtWidgets import *

class QssSelector(QWidget):
    def __init__(self):
        super(QssSelector, self).__init__()

        self.setWindowTitle("QSS选择器")

        layout=QVBoxLayout()

        self.btn1=QPushButton("COMMAND1")
        self.btn2=QPushButton("COMMAND2")
        self.btn3=QPushButton("COMMAND3")

        #****************
        #给控件一个属性标签:属性名,属性值
        self.btn2.setProperty("name","btn2")
        self.btn3.setProperty("name","btn3")
        #****************

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QssSelector()
    #在这里修改所有控件的QSS样式**************************
    #选择器:[]:值设置btn2
    #不同设置之间用;分隔
    qssStyle='''
        QPushButton[name="btn2"]{
            background-color:blue;
            color:yellow;
            height:120;
            font-size:60px;
        }
        QPushButton[name="btn3"]{
            background-color:green;
            color:red;
            height:120;
            font-size:60px;
        }
    '''
    main.setStyleSheet(qssStyle)
    #*************************************************
    main.show()
    sys.exit(app.exec_())