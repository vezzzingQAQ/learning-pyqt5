"""
2021.1.19:C8:在pycharm中显示设计的界面
"""
import sys
from PyQt5study import experiment

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui= experiment.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())