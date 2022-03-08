"""
2021.1.19:综合练习1，运用了几乎所学，至C22信号和槽,打算一直推进
"""
import sys
from PyQt5study import totalTraining1

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui= totalTraining1.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())