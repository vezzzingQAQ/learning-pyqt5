'''
2021.1.31,IVICX D.S. C127;实现异形窗口
'''
'''
mask
透明PNG图像
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AbnormityWindow(QWidget):
    def __init__(self):
        super(AbnormityWindow, self).__init__()

        self.setWindowTitle("实现异形窗口")

        self.pix=QBitmap("./images/1.png")

        self.resize(self.pix.size())

        self.setMask(self.pix)

    def paintEvent(self, QPaintEvent):
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap("./images/a1.BMP"))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AbnormityWindow()
    main.show()
    sys.exit(app.exec_())