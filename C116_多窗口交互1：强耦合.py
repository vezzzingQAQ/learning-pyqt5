'''
2021.1.30,IVICX D.S. C116;多窗口交互：强耦合
'''
'''
窗口数据交换-强耦合【直接调用控件，两个窗口紧密联系】/信号与槽【两个窗口相对独立】
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from C116_DateDialogClass import DateDialog
class MultiWindow(QWidget):
    def __init__(self):
        super(MultiWindow, self).__init__()

        self.setWindowTitle("主窗口")

        gridLayout=QGridLayout()

        self.lineEdit=QLineEdit()
        self.btn1=QPushButton("弹出对话框1")

        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.btn1)
        self.setLayout(gridLayout)

        self.btn1.clicked.connect(self.onBtn1Click)

    def onBtn1Click(self):
        dialog=DateDialog(self)
        result=dialog.exec()
        date=dialog.currentDateTime()#调用另一个窗口里的方法
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MultiWindow()
    main.show()
    sys.exit(app.exec_())
