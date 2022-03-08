"""
2021.1.19:C8:在pycharm中显示设计的界面C布局器C20：设置控件伙伴关系
"""
import sys
from PyQt5study import VHmixedexperiment

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui= VHmixedexperiment.Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())