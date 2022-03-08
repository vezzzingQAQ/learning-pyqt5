'''
2021.1.26,IVICX D.S. C88;让程序定时关闭
'''
'''
QTimer.singleShot:在某段时间之后只调用某段代码一次即可
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

if __name__=="__main__":
    app=QApplication(sys.argv)

    label=QLabel("<font color=red size=140><b>Hello World:窗口在5秒后自动关闭</b></font>")
    label.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)#无框窗体
    label.show()
    QTimer.singleShot(5000,app.quit)

    sys.exit(app.exec_())


