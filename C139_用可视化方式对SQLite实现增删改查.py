'''
2021.2.2,IVICX D.S. C139;操作显示本地QSQLITE数据库
'''
'''
QTableView<-QSqlTableModel
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

def initializeModel(model):
    model.setTable("people")
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0,Qt.Horizontal,"ID")
    model.setHeaderData(1,Qt.Horizontal,"name")
    model.setHeaderData(2,Qt.Horizontal,"place")

def creatView(title,model):
    view=QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def findRow(i):
    delrow=i.row()
    print(f"del row={str(delrow)}")

def addRow():
    ret=model.insertRows(model.rowCount(),1)#行数，一行
    print(f"insert row={str(ret)}")

if __name__=="__main__":
    app=QApplication(sys.argv)
    db=QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("./db/db1.db3")
    model=QSqlTableModel()
    delrow=-1

    initializeModel(model)
    view=creatView("展示数据",model)

    view.clicked.connect(findRow)

    dlg=QDialog()
    layout=QVBoxLayout()
    layout.addWidget(view)

    addbtn=QPushButton("添加一行")
    layout.addWidget(addbtn)
    addbtn.clicked.connect(addRow)

    delbtn=QPushButton("删除一行")
    layout.addWidget(delbtn)
    delbtn.clicked.connect(lambda :model.removeRow(view.currentIndex().row()))

    dlg.setLayout(layout)

    dlg.setWindowTitle("Database")
    dlg.resize(500,400)
    dlg.show()
    sys.exit(app.exec())



