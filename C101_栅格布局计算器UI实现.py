'''
2021.1.28,IVICX D.S. C101;栅格布局计算器UI实例
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class calculater(QWidget):
    def __init__(self):
        super(calculater, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("计算器界面&栅格布局")

        grid=QGridLayout()

        names=["cls","back","close",
               "7","8","9","/",
               "4","5","6","*",
               "1","2","3","-",
               "0",".","=","+"]
        position=[(i,j) for i in range(5) for j in range(4)]
        print(position)

        for position,names in zip(position,names):
            if names=="":
                continue
            print(position,names)
            button=QPushButton(names)
            #python元组前加*变为两个值
            grid.addWidget(button,*position)
        self.setLayout(grid)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = calculater()
    main.show()
    sys.exit(app.exec_())