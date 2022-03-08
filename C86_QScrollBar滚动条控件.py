'''
2021.1.26,IVICX D.S. C86;QScrollBar滚动条控件
'''
'''
QScrollBar滚动条控件的作用
1.通过滚动条值得变化控制其他控件的状态
2.控制窗口上控件的上下左右滑动
$>>>>>>>>>>>>>>>>>>>>>>>>>>>>
布局嵌套，label上色，透明度
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class ScrollBarEXPForm(QWidget):
    def __init__(self):
        super(ScrollBarEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QScrollBar滚动条控件")
        self.setGeometry(300,300,300,200)

        layout=QGridLayout()
        layHout=QHBoxLayout()

        self.label=QLabel("<拖动滚动条改变文字颜色>")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("微软雅黑",20))
        self.label.setAutoFillBackground(True)

        self.scrollbar1=QScrollBar(Qt.Horizontal)
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.valueChanged.connect(self.slidermoved)

        self.scrollbar2=QScrollBar(Qt.Horizontal)
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.valueChanged.connect(self.slidermoved)

        self.scrollbar3=QScrollBar(Qt.Horizontal)
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.valueChanged.connect(self.slidermoved)

        self.scrollbar4=QScrollBar(Qt.Horizontal)
        self.scrollbar4.setMaximum(255)
        self.scrollbar4.valueChanged.connect(self.slidermoved)

        self.labelMove=QLabel()
        self.labelMove.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.Window,QColor(200,100,100,100))
        self.labelMove.setPalette(palette)
        self.y=self.labelMove.pos().y()

        self.scrollbar5=QScrollBar(Qt.Vertical)
        self.scrollbar5.setMinimum(-255)
        self.scrollbar5.setMaximum(255)
        self.scrollbar5.valueChanged.connect(self.poschange)

        layHout.addWidget(self.labelMove)

        layout.addWidget(self.label,0,0,1,4)
        layout.addWidget(self.scrollbar1,1,0,1,4)
        layout.addWidget(self.scrollbar2,2,0,1,4)
        layout.addWidget(self.scrollbar3,3,0,1,4)
        layout.addWidget(self.scrollbar4,4,0,1,4)
        layout.addWidget(self.scrollbar5,5,0,4,1)
        layout.addLayout(layHout,5,1,4,3)

        self.setLayout(layout)

    def slidermoved(self):
        self.label.setText(f"<R={str(self.scrollbar1.value())},G={str(self.scrollbar2.value())},B={str(self.scrollbar3.value())},A={str(self.scrollbar4.value())}>")
        palette=QPalette()
        color=QColor(self.scrollbar1.value(),self.scrollbar2.value(),self.scrollbar3.value(),self.scrollbar4.value())
        palette.setColor(QPalette.Window,color)
        self.label.setPalette(palette)
    def poschange(self):
        self.labelMove.move(self.labelMove.x(),self.y+self.scrollbar5.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ScrollBarEXPForm()
    main.show()
    sys.exit(app.exec_())

