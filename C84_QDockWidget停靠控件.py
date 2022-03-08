'''
2021.1.26,IVICX D.S. C84;QDockWidget停靠控件
'''
'''
可以切换:停靠在各个位置/悬浮为独立窗口
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QDockWidgetEXPForm(QMainWindow):
    #也可以单独创建
    def __init__(self):
        super(QDockWidgetEXPForm, self).__init__()
        self.setWindowTitle("QDockWidget停靠控件")
        self.setGeometry(300,50,10,10)

        self.items=QDockWidget("Dockable",self)

        self.listWidget=QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        for i in range(100):
            self.listWidget.addItem(str(i)+"*******************")

        self.items.setWidget(self.listWidget)

        self.setCentralWidget(QTextEdit())

        #self.items.setFloating(True)#默认设为悬浮状态
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)#默认停靠在右侧

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QDockWidgetEXPForm()
    main.show()
    sys.exit(app.exec_())