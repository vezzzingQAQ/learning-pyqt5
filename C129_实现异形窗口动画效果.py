'''
2021.2.1,IVICX D.S. C129;实现异形窗口的动画效果
'''
'''
mask
透明PNG图像
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AnimationWindows(QWidget):
    def __init__(self):
        super(AnimationWindows, self).__init__()

        self.i=1

        self.m_drag=False
        self.m_dragPosition=None

        self.mypix()
        self.timer=QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timeChange)

        self.timer.start()

    def timeChange(self):
        self.i+=1
        self.mypix()

    def mypix(self):
        self.update()
        if self.i==5:
            self.i=1
        self.mypic={1:"./images/P1.png",
                    2:"./images/P2.png",
                    3:"./images/P3.png",
                    4:"./images/P4.png"}
        self.pix=QPixmap(self.mypic[self.i])
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap(self.mypic[self.i]))

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_dragPosition=QMouseEvent.globalPos()-self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))

        if QMouseEvent.button()==Qt.RightButton:
            self.close()
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_dragPosition)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AnimationWindows()
    main.show()
    sys.exit(app.exec_())