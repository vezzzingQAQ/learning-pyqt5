'''
2021.1.24,IVICX D.S. C69;在表格中快速定位到特定的行
'''
'''
1.数据的定位【找到第一个满足条件的单元格】:findItems(返回列表【取第一个值】)
2.如果找到满足条件的单元格->定位到单元格所在的行:setSliderPosition(row)
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在表格中快速定位到特定的行")
        self.resize(600,800)

        layout=QHBoxLayout()

        self.table=QTableWidget()
        self.table.setRowCount(40)
        self.table.setColumnCount(4)

        for i in range(40):
            for j in range(4):
                itemContent=(f"<{str(i)},{str(j)}>")
                self.table.setItem(i,j,QTableWidgetItem(itemContent))

        #搜索满足条件的cell************************************************
        #匹配模式>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #text="<13,1>"
        #items=self.table.findItems(text,Qt.MatchExactly)#有多种搜索方式
        #这里选择精确搜索【必须完全一样才能匹配】
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        text="<1"
        items=self.table.findItems(text,Qt.MatchStartsWith)#开头一样
        if len(items)>0:#找到了
            item=items[0]#符合条件的第一个值
            item.setBackground(QBrush(QColor(0,0,200)))#找到的格子背景刷蓝
            item.setForeground(QBrush(QColor(255,0,0)))
        #定位到指定的行****************************************************
        row=item.row()
        self.table.verticalScrollBar().setSliderPosition(row)#滚动条滚动到指定位置
        #***************************************************************
        layout.addWidget(self.table)
        self.setLayout(layout)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DataLocation()
    main.show()
    sys.exit(app.exec_())