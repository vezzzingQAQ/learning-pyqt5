'''
2021.1.27,IVICX D.S. C96;水平盒布局
2021.1.27,IVICX D.S. C96;设置控件对齐方式
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class hboxlayoutEXPform(QWidget):
    def __init__(self):
        super(hboxlayoutEXPform, self).__init__()
        self.setWindowTitle("绝对布局,设置控件对齐方式")

        hlayout=QHBoxLayout()
        #占的比例，对齐方式
        hlayout.addWidget(QPushButton("command1"),2,Qt.AlignLeft|Qt.AlignTop)
        hlayout.addWidget(QPushButton("command2"),1,Qt.AlignLeft|Qt.AlignTop)
        hlayout.addWidget(QPushButton("command3"),1,Qt.AlignLeft|Qt.AlignTop)
        hlayout.addWidget(QPushButton("command4"),1,Qt.AlignRight|Qt.AlignBottom)
        hlayout.addWidget(QPushButton("command5"),1,Qt.AlignRight|Qt.AlignBottom)
        hlayout.addWidget(QPushButton("command6"),1,Qt.AlignRight|Qt.AlignBottom)

        hlayout.setSpacing(40)#设置控件间间距

        self.setLayout(hlayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = hboxlayoutEXPform()
    main.show()
    sys.exit(app.exec_())
