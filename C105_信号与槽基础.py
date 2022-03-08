'''
2021.1.28,IVICX D.S. C105;信号与槽基础
'''

from PyQt5.QtWidgets import *
import sys

class signalSlotEXPForm(QWidget):
    def __init__(self):
        super(signalSlotEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("信号与槽基础")

        self.btn=QPushButton("COMMAND1",self)
        self.btn.clicked.connect(self.clicked)

    def clicked(self):
        self.btn.setText("信号已经发出")
        self.btn.setStyleSheet("QPushButton(max-width:200px;min-width:200px)")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = signalSlotEXPForm()
    main.show()
    sys.exit(app.exec_())