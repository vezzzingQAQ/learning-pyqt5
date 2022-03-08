'''
2021.1.30,IVICX D.S. C118;设置窗口控件风格
'''
'''
setStyle
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class WindowStyle(QWidget):
    def __init__(self):
        super(WindowStyle, self).__init__()

        self.setWindowTitle("设置窗口风格")

        layout=QGridLayout()

        self.seyleLabel=QLabel("设置窗口风格")
        self.styleCombox=QComboBox()
        self.styleCombox.addItems(QStyleFactory.keys())
        #获取当前窗口的风格,设置为默认的选项
        currentStyle=QApplication.style().objectName()
        index=self.styleCombox.findText(currentStyle,Qt.MatchFixedString)
        self.styleCombox.setCurrentIndex(index)

        layout.addWidget(self.seyleLabel,0,0)
        layout.addWidget(self.styleCombox,0,1)
        layout.addWidget(QLineEdit(),1,0)
        layout.addWidget(QTextEdit(),1,1)
        self.setLayout(layout)

        self.styleCombox.activated[str].connect(self.handelStyleChanged)
    def handelStyleChanged(self,style):
        QApplication.setStyle(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowStyle()
    main.show()
    sys.exit(app.exec_())