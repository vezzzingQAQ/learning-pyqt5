'''
2021.1.30,IVICX D.S. C119;设置窗口样式
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class WindowPattern(QMainWindow):
    def __init__(self):
        super(WindowPattern, self).__init__()

        self.setWindowTitle("设置窗口样式")
        self.resize(500,260)

        self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.WindowStaysOnTopHint)#设置窗口置前
        #self.setWindowFlags(Qt.FramelessWindowHint)#无边框窗口
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(images/2.BMP);}")#QSS
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowPattern()
    main.show()
    sys.exit(app.exec_())