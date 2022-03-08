'''
2021.1.31,IVICX D.S. C124;QSS子控件选择器
'''
'''
【有些控件ex:QcombBox由多个子控件组成:下拉列表+下拉按钮】
单独设置右侧的下拉按钮样式
【选择控件的一部分】
'''
import sys
from PyQt5.QtWidgets import *

class QssSubControl(QWidget):
    def __init__(self):
        super(QssSubControl, self).__init__()

        self.setWindowTitle("QSS子控件选择器")

        layout=QVBoxLayout()

        self.combo=QComboBox(self)
        self.combo.addItem("windows")
        self.combo.addItem("linux")
        self.combo.addItem("macosx")

        self.combo.setObjectName("cbo")

        layout.addWidget(self.combo)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QssSubControl()
    #在这里修改所有控件的QSS样式**************************
    #选择器:的另一种指定方式
    qssStyle='''
        QComboBox#cbo::drop-down{
            image:url(./images/3.jpg);
        }
    '''
    main.setStyleSheet(qssStyle)
    #*************************************************
    main.show()
    sys.exit(app.exec_())