'''
2021.1.29,IVICX D.S. C113;用lambda表达式为槽函数传参
'''
from PyQt5.QtWidgets import *
import sys
'''
匿名函数
fun=lambda :print("hello world")
fun()
#>hello world
fun1=lambda x,y:print(x*y)
fun1(2,3)
#>6
'''
class lambdaSlotArg(QWidget):
    def __init__(self):
        super(lambdaSlotArg, self).__init__()

        self.setWindowTitle("用lambda表达式为槽函数传参")
        self.resize(200,100)

        layout=QVBoxLayout()

        self.btn1=QPushButton("COMMAND1")
        self.btn2=QPushButton("COMMAND2")
        self.label1=QLabel("<result>")

        self.btn1.clicked.connect(lambda :self.onButtonClick(10,20))
        self.btn2.clicked.connect(lambda :self.onButtonClick(-20,12.2))

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