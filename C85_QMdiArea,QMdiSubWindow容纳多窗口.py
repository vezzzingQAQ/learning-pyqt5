'''
2021.1.26,IVICX D.S. C85;QMdiArea,QMdiSubWindow容纳多窗口
'''
'''
两种排列方式：层叠，平铺
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MultiWindows(QMainWindow):
    def __init__(self):
        super(MultiWindows, self).__init__()

        self.setWindowTitle("QMdiArea,QMdiSubWindow容纳多窗口")

        self.windowCount=0

        self.mdi=QMdiArea()
        self.setCentralWidget(self.mdi)

        bar=self.menuBar()
        file=bar.addMenu("File")
        file.addAction("新建子窗体")
        file.addAction("层叠显示")
        file.addAction("平铺显示")

        file.triggered.connect(self.windowAction)

    def windowAction(self,q):
        if q.text()=="新建子窗体":
            self.windowCount+=1
            sub=QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口"+str(self.windowCount))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text()=="层叠显示":
            self.mdi.cascadeSubWindows()
        elif q.text()=="平铺显示":
            self.mdi.tileSubWindows()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MultiWindows()
    main.show()
    sys.exit(app.exec_())