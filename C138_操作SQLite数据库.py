'''
2021.2.2,IVICX D.S. C138;创建本地QSQLITE数据库
'''
import sys
from PyQt5.QtSql import QSqlDatabase,QSqlQuery


def creatDB():
    db=QSqlDatabase.addDatabase("QSQLITE")#指定数据库类型【接口】

    #指定QSQLITE数据库文件,本地文件名,远程亦可
    db.setDatabaseName("./Db/db1.db3")
    if not db.open():
        print("无法建立连接")
        return False
    query=QSqlQuery()
    query.exec("create table people(id int primary key,name varchar(1000),address varchar(1000))")
    query.exec("insert into people values(1,'Vezzzing','esmmm')")#插入一条数据
    query.exec("insert into people values(2,'Merliiing','esmmm')")#插入一条数据
    db.close()
    return True
if __name__=="__main__":
    creatDB()