'''
2021.1.29,IVICX D.S. C114;用partial对象传参
'''
from PyQt5.QtWidgets import *
import sys
from functools import partial

class lambdaSlotArg(QWidget):
    def __init__(self):
        super(lambdaSlotArg, self).__init__()

        self.setWindowTitle("用lambda表达式为槽函数传参")
        self.resize(200,100)

        layout=QVBoxLayout()

        self.btn1=QPushButton("COMMAND1")
        self.btn2=QPushButton("COMMAND2")
        self.label1=QLabel("<result>")

        self.btn1.clicked.connect(partial(self.onButtonClick,2,3))
        self.btn2.clicked.connect(partial(self.onButtonClick,-3,2.1))

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.label1)
        self.setLayout(layout)

    def onButtonClick(self,m,n):
        self.label1.setText(str(m)+"+"+str(n)+"="+str(m+n))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = lambdaSlotArg()
    main.show()
    sys.exit(app.exec_())