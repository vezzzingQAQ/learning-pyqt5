'''
2021.2.2,IVICX D.S. C135;用QpropertyAnimation实现动画效果改变窗体尺寸
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Animwindow(QWidget):
    def __init__(self):
        super(Animwindow, self).__init__()

        self.originalHeight=50
        self.changedHeight=250

        self.setGeometry(QRect(500,400,150,self.originalHeight))

        layout=QVBoxLayout()

        self.btn=QPushButton("展开")
        self.btn.clicked.connect(self.change)

        layout.addWidget(self.btn)
        self.setLayout(layout)

    def change(self):
        currentHeight=self.height()
        if self.originalHeight==currentHeight:
            startHeight=self.originalHeight
            endHeight=self.changedHeight
            self.btn.setText("折叠")
        else:
            startHeight=self.changedHeight
            endHeight=self.originalHeight
            self.btn.setText("展开")
        self.animation=QPropertyAnimation(self,b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(500,400,150,startHeight))
        self.animation.setEndValue(QRect(500,400,150,endHeight))
        self.animation.start()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Animwindow()
    main.show()
    sys.exit(app.exec_())