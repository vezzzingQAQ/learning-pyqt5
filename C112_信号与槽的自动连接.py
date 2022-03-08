'''
2021.1.29,IVICX D.S. C112;信号与槽的自动连接
'''
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class aytoSignalSlot(QWidget):
    def __init__(self):
        super(aytoSignalSlot, self).__init__()

        self.okbtn=QPushButton("OK",self)
        self.canbtn=QPushButton("CANCEL",self)

        self.okbtn.setObjectName("okbtn")#>>on__objectName_事件名
        self.canbtn.setObjectName("canbtn")#>>这里与on_xxx_clicked对应

        layout=QHBoxLayout()

        layout.addWidget(self.okbtn)
        layout.addWidget(self.canbtn)
        self.setLayout(layout)

        #self.okbtn.clicked.connect(self.on_okbtn_clicked)正常的写法
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()#标注这是一个槽
    def on_okbtn_clicked(self):
        print("点击了OK按钮")
    @pyqtSlot()
    def on_canbtn_clicked(self):
        print("点击了取消按钮")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = aytoSignalSlot()
    main.show()
    sys.exit(app.exec_())