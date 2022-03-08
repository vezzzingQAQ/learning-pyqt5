'''
2021.1.24,IVICX D.S. C66;扩展的列表控件
'''
'''
是QListView的子类
不仅可以从模型添加数据，也可直接添加
'''
from PyQt5.QtWidgets import *
import sys

class listWidgetEXPForm(QMainWindow):
    def __init__(self):
        super(listWidgetEXPForm, self).__init__()
        self.setWindowTitle("QListWidget使用")
        self.resize(500,300)

        self.listwidget=QListWidget()
        self.listwidget.resize(300,120)
        self.listwidget.addItem("item1")#支持直接添加数据
        self.listwidget.addItem("item2")#支持直接添加数据
        self.listwidget.addItem("item3")#支持直接添加数据
        self.listwidget.addItem("item4")#支持直接添加数据
        self.listwidget.addItem("item5")#支持直接添加数据

        self.listwidget.itemClicked.connect(self.cilcked)

        self.setCentralWidget(self.listwidget)
    def cilcked(self,index):
        QMessageBox.information(self,"QListWidget","选择了:"+self.listwidget.item(self.listwidget.row(index)).text())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = listWidgetEXPForm()
    main.show()
    sys.exit(app.exec_())