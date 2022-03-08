'''
2021.1.25,IVICX D.S. C81;QTreeView与系统定制模式
'''
'''
与QTreeWidget区别：model装载
QDirModel操作系统的Model#显示当前目录的树结构
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

if __name__=="__main__":
    app=QApplication(sys.argv)
    model=QDirModel()
    tree=QTreeView()
    tree.setModel(model)

    tree.setWindowTitle("QTreeView")
    tree.resize(600,400)
    tree.show()

    sys.exit(app.exec_())