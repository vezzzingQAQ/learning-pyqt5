'''
2021.1.28,IVICX D.S. C103;表单布局
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class formLayout(QWidget):
    def __init__(self):
        super(formLayout, self).__init__()

        self.setWindowTitle("表单布局")
        self.resize(350,300)

        flou=QFormLayout()

        self.titleLabel = QLabel("标题")
        self.authorLabel = QLabel("作者")
        self.contentLbale = QLabel("内容")

        self.titleEdit = QLineEdit()
        self.authorEdit = QLineEdit()
        self.contentEdit = QTextEdit()

        flou.addRow(self.titleLabel,self.titleEdit)
        flou.addRow(self.authorLabel,self.authorEdit)
        flou.addRow(self.contentLbale,self.contentEdit)

        self.setLayout(flou)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = formLayout()
    main.show()
    sys.exit(app.exec_())