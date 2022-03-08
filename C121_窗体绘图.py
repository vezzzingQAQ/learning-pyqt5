'''
2021.1.31,IVICX D.S. C121;实现用鼠标在窗体上绘图
'''
'''
1.如何绘图:
在paintEvent中绘图，通过调用update方法触发paintEvent的调用
2.在哪里绘图:
在QPixmap对象里面
3.如何通过移动鼠标绘图【按住左键绘图，抬起后中断】
鼠标事件:按下/抬起/移动
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Drawing(QWidget):
    def __init__(self):
        super(Drawing, self).__init__()
        #self.pix=QPixmap()
        self.lastPoint=QPoint()
        self.endPoint=QPoint()
        self.pressed=False

        self.initUI()

    def initUI(self):
        self.setWindowTitle("绘图窗体")
        self.resize(600,600)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)  # 设置窗口置前
        #layout=QVBoxLayout()

        self.pix=QPixmap(600,600)
        self.pix.fill(Qt.white)

        #layout.addWidget(self.pix)
        #self.setLayout(layout)

    def paintEvent(self, Event):
        pp=QPainter(self.pix)
        pen = QPen(Qt.red, 2, Qt.SolidLine)  # 第二位为点宽，第三位绘图样式
        pp.setPen(pen)
        pp.drawLine(self.lastPoint,self.endPoint)

        self.lastPoint=self.endPoint

        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            self.lastPoint=QMouseEvent.pos()#获得坐标
            self.pressed=True

    def mouseMoveEvent(self, QMouseEvent):
        if self.pressed==True:
            self.endPoint=QMouseEvent.pos()
            self.update()#重新绘制

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            self.endPoint=QMouseEvent.pos()
            self.pressed=False
            self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Drawing()
    main.show()
    sys.exit(app.exec_())