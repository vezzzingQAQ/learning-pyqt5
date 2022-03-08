'''
2021.1.25,IVICX D.S. C78;树控件的基本用法
2021.1.25,IVICX D.S. C79;为树节点添加响应事件
2021.1.25,IVICX D.S. C80;为树控件增加删除修改节点
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class treeWidgetEXPFform(QWidget):
    def __init__(self):
        super(treeWidgetEXPFform, self).__init__()
        self.initUI()
        self.commandShowText=""

    def initUI(self):
        self.setWindowTitle("树控件的基本用法,为树节点添加响应事件,为树控件增加删除修改节点")

        layout=QGridLayout()

        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        self.tree=QTreeWidget()
        self.tree.setColumnCount(2)#指定列数
        self.tree.setHeaderLabels(["key","value"])#指定显示的值
        #****************************************************
        root=QTreeWidgetItem(self.tree)#增加一个根节点
        root.setText(0,"根节点")
        root.setIcon(0, QIcon("images/2.BMP"))
        #****************************************************
        self.tree.setColumnWidth(0,120)#设置第一列宽度
        #****************************************************
        #添加子节点1
        child1=QTreeWidgetItem(root)
        child1.setText(0,"子节点1")
        child1.setText(1,"子节点1的数据")
        child1.setIcon(0, QIcon("images/2.BMP"))
        #为节点添加复选框
        child1.setCheckState(0,Qt.Checked)

        #添加子节点2
        child2=QTreeWidgetItem(root)
        child2.setText(0,"子节点2")
        child2.setIcon(0, QIcon("images/2.BMP"))

        #为child2添加子节点
        child3=QTreeWidgetItem(child2)
        child3.setText(0,"子节点2—1")
        #****************************************************
        #展开所有的子数
        #self.tree.expandAll()
        #****************************************************
        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        self.tree.clicked.connect(self.ontreeclicked)

        self.addbtn=QPushButton("添加节点")
        self.addbtn.clicked.connect(self.addTree)
        self.updatebtn=QPushButton("修改节点")
        self.updatebtn.clicked.connect(self.updateTree)
        self.deletebtn=QPushButton("删除节点")
        self.deletebtn.clicked.connect(self.deleteTree)

        self.text1=QTextEdit()
        self.text1.setText("<commands will be listed there>")

        self.btonclear=QPushButton("清空操作数据")
        self.btonclear.clicked.connect(self.clearData)

        layout.addWidget(self.tree,0,0,1,3)
        layout.addWidget(self.addbtn,1,0)
        layout.addWidget(self.updatebtn,1,1)
        layout.addWidget(self.deletebtn,1,2)
        layout.addWidget(self.text1,2,0,1,3)
        layout.addWidget(self.btonclear,3,0,1,3)
        self.setLayout(layout)

    def clearData(self):
        self.commandShowText=""
        self.text1.setText(self.commandShowText)

    def ontreeclicked(self,index):
        item=self.tree.currentItem()
        self.commandShowText+=">clicked>\n"
        self.commandShowText+="<row="+str(index.row())+"\n"
        self.commandShowText+=(f"<key={item.text(0)},value={item.text(1)}\n")
        self.text1.setText(self.commandShowText)

    def addTree(self):#在选中位置下添加新节点
        self.commandShowText+=">add>\n"
        item=self.tree.currentItem()
        self.commandShowText+=f"current item={str(item)}\n"
        self.text1.setText(self.commandShowText)
        node=QTreeWidgetItem(item)
        node.setText(0,"新的节点")
        node.setText(1,"新节点的值")
    def updateTree(self):
        self.commandShowText+="update>\n"
        item=self.tree.currentItem()
        self.commandShowText += f"current item={str(item)}\n"
        self.text1.setText(self.commandShowText)
        item.setText(0,"修改节点")
        item.setText(1,"修改节点的值")
    def deleteTree(self):
        self.commandShowText+=">delete>\n"
        item=self.tree.currentItem()
        root=self.tree.invisibleRootItem()#顶级节点的不可见父节点
        self.commandShowText+=f"current item={str(item)}\n"
        for i in self.tree.selectedItems():
            (i.parent() or root).removeChild(i)#如果是父节点要逐一移除子节点
            #↑括号表示两个中又一个不为空即可执行
            self.commandShowText+=f">remove={i}"
        self.text1.setText(self.commandShowText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = treeWidgetEXPFform()
    main.show()
    sys.exit(app.exec_())