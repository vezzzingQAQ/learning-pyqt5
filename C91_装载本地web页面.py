'''
2021.1.27,IVICX D.S. C91;QWebEngineView装载本地web页面
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os

class QWebEngineViewEXPForm(QMainWindow):
    def __init__(self):
        super(QWebEngineViewEXPForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QWebEngineView装载本地web页面")
        self.resize(1355,730)
        self.center()

        self.browser=QWebEngineView()
        url=os.getcwd()+"/html/webLoadTest.html"
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)

    def center(self):#窗口居中函数
        screen=QDesktopWidget().screenGeometry()#得到屏幕坐标
        size=self.geometry()#得到窗口坐标系
        newLeft=int((screen.width()-size.width())/2)
        newTop=int((screen.height()-size.height())/2)
        self.move(newLeft,newTop)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QWebEngineViewEXPForm()
    main.show()
    sys.exit(app.exec_())
