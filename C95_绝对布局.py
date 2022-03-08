'''
2021.1.27,IVICX D.S. C95;绝对布局
'''

from PyQt5.QtWidgets import *
import sys

class absolutelayoutEXPform(QWidget):
    def __init__(self):
        super(absolutelayoutEXPform, self).__init__()
        self.setWindowTitle("绝对布局")

        self.label1=QLabel("这是一个标签",self)
        self.label1.move(15,20)

        self.label2=QLabel("这也是个标签",self)
        self.label2.move(35,40)

        self.label3=QLabel("这还是个标签",self)
        self.label3.move(55,80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = absolutelayoutEXPform()
    main.show()
    sys.exit(app.exec_())
