'''
2021.1.24,IVICX D.S. C65;列表控件
'''
'''
数据源:Model
需要创建QListlView实例和一个数据源，然后将两者关联
MVC Model Viewer Controller
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class listViewEXPForm(QWidget):
    def __init__(self):
        super(listViewEXPForm, self).__init__()
        self.setWindowTitle("QListView使用")
        self.resize(500,300)

        layout=QVBoxLayout()

        self.listView=QListView()
        self.listModel=QStringListModel()#建立一个空的模型
        self.list=["列表项1"]
        for i in range(2,100):
            self.list.append("列表项"+str(i))
        self.listModel.setStringList(self.list)
        self.listView.setModel(self.listModel)

        self.listView.clicked.connect(self.clicked)

        layout.addWidget(self.listView)
        self.setLayout(layout)

    def clicked(self,item):#第二个参数为对象
        QMessageBox.information(self,"QListView","选择的是:"+self.list[item.row()])
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = listViewEXPForm()
    main.show()
    sys.exit(app.exec_())