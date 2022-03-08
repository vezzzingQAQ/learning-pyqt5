'''
2021.1.28,IVICX D.S. C102;栅格布局表单布局
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class gridForm(QWidget):
    def __init__(self):
        super(gridForm, self).__init__()

        self.setWindowTitle("栅格布局表单布局")
        self.resize(350,300)

        self.titleLabel=QLabel("标题")
        self.authorLabel=QLabel("作者")
        self.contentLbale=QLabel("内容")

        self.titleEdit=QLineEdit()
        self.authorEdit=QLineEdit()
        self.contentEdit=QTextEdit()

        grid=QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.titleLabel,1,0)
        grid.addWidget(self.titleEdit,1,1)
        grid.addWidget(self.authorLabel,2,0)
        grid.addWidget(self.authorEdit,2,1)
        grid.addWidget(self.contentLbale,3,0)
        grid.addWidget(self.contentEdit,3,1,5,1)

        self.setLayout(grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = gridForm()
    main.show()
    sys.exit(app.exec_())