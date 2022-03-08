'''
2021.1.28,IVICX D.S. C104;QSplitter控件边界的拖动
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class QSplitterEXPForm(QWidget):
    def __init__(self):
        super(QSplitterEXPForm, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QSplitter控件边界的拖动")
        self.setGeometry(300,300,300,200)
        hbox=QHBoxLayout()

        self.topLeft=QFrame()
        self.topLeft.setFrameShape(QFrame.StyledPanel)

        self.bottom=QFrame()
        self.bottom.setFrameShape(QFrame.StyledPanel)

        self.splitter1=QSplitter(Qt.Horizontal)#也是一个容器

        self.textEdit=QTextEdit()

        self.splitter1.addWidget(self.topLeft)
        self.splitter1.addWidget(self.textEdit)

        self.splitter1.setSizes([100,200])#设置默认高宽

        self.splitter2=QSplitter(Qt.Vertical)

        self.splitter2.addWidget(self.splitter1)
        self.splitter2.addWidget(self.bottom)

        hbox.addWidget(self.splitter2)

        self.setLayout(hbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QSplitterEXPForm()
    main.show()
    sys.exit(app.exec_())