'''
2021.1.27,IVICX D.S. C98;垂直盒布局
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class vboxlayoutEXPform(QWidget):
    def __init__(self):
        super(vboxlayoutEXPform, self).__init__()
        self.setWindowTitle("垂直盒布局")

        hlayout=QVBoxLayout()
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
    main = vboxlayoutEXPform()
    main.show()
    sys.exit(app.exec_())
