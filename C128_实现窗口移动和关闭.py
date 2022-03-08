'''
2021.1.31,IVICX D.S. C128;实现异形窗口的移动和关闭
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
        self.m_drag=False
        self.m_dragPosition=None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("窗口")

        layout = QVBoxLayout()

        self.label1 = QLabel("<>")
        self.label2 = QLabel("<>")
        self.label3 = QLabel("<>")

        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        self.setLayout(layout)

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
            self.label1.setText("<" + str(QMouseEvent.globalPos()) + ">")
            self.label2.setText("<" + str(QMouseEvent.pos()) + ">")
            self.label3.setText("<" + str(self.pos()) + ">")
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AbnormityWindow()
    main.show()
    sys.exit(app.exec_())
