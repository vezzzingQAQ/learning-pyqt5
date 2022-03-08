'''
2021.1.25,IVICX D.S. C82;QTabWidget选项卡控件
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class TabWidgetEXPForm(QTabWidget):#可以把整个窗口作为标签页
    #也可以单独创建
    def __init__(self):
        super(TabWidgetEXPForm, self).__init__()

        self.setWindowTitle("QTabWidget选项卡控件")

        #创建用于显示界面的窗口
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        #绑定到选项卡
        self.addTab(self.tab1,"选项卡1")
        self.addTab(self.tab2,"选项卡2")
        self.addTab(self.tab3,"选项卡3")


    def tab1UI(self):#为tab1创建界面，封装成函数
        layout=QFormLayout()
        layout.addRow("姓名",QLineEdit())
        layout.addRow("地址",QLineEdit())
        self.changeTitle=QPushButton("改变标题")
        self.changeTitle.clicked.connect(self.changetab1title)
        layout.addWidget(self.changeTitle)
        self.tab1.setLayout(layout)
    def changetab1title(self):
        self.setTabText(0,"改变后的标题")#动态改变选项卡标题

    def tab2UI(self):
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton("♂"))
        sex.addWidget(QRadioButton("♀"))
        layout.addRow("性别:",sex)
        layout.addRow("生日:",QLineEdit())
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("啥啥啥"))
        layout.addWidget(QCheckBox("啥啥啥"))
        self.tab3.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TabWidgetEXPForm()
    main.show()
    sys.exit(app.exec_())