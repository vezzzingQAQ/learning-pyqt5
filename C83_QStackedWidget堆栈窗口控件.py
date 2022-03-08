'''
2021.1.25,IVICX D.S. C83;QStackedWidget堆栈窗口控件
'''
'''
在EX下来列表，按钮...中选择某一项在右侧显示窗口，页和选项卡单独分开，通过索引获取
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QStackedWidgetEXPForm(QTabWidget):#可以把整个窗口作为标签页
    #也可以单独创建
    def __init__(self):
        super(QStackedWidgetEXPForm, self).__init__()
        self.setWindowTitle("QStackedWidget堆栈窗口控件")
        self.setGeometry(300,50,10,10)

        self.list=QListWidget()
        self.list.insertItem(0,"傻啥啥啥")
        self.list.insertItem(1,"啥傻啥啥")
        self.list.insertItem(2,"啥啥啥啥")

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()

        self.tab3UI()
        self.tab2UI()
        self.tab1UI()
        #创建堆栈窗口控件****************************************
        self.stack=QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        #*****************************************************
        hbox=QHBoxLayout()#左侧列表右侧堆栈
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)
        #为列表添加绑定事件***************************************
        self.list.currentRowChanged.connect(self.display)
    def display(self,index):
        self.stack.setCurrentIndex(index)
    #*********************************************************
    def tab1UI(self):#为tab1创建界面，封装成函数
        layout=QFormLayout()
        layout.addRow("姓名",QLineEdit())
        layout.addRow("地址",QLineEdit())
        self.stack1.setLayout(layout)
    def tab2UI(self):
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton("♂"))
        sex.addWidget(QRadioButton("♀"))
        layout.addRow("性别:",sex)
        layout.addRow("生日:",QLineEdit())
        self.stack2.setLayout(layout)
    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("啥啥啥"))
        layout.addWidget(QCheckBox("啥啥啥"))
        self.stack3.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QStackedWidgetEXPForm()
    main.show()
    sys.exit(app.exec_())