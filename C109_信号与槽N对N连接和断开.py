'''
2021.1.29,IVICX D.S. C109;信号和槽的N对N连接和断开
'''

from PyQt5.QtCore import *
import sys

class NtoN(QObject):
    signal1=pyqtSignal()
    signal2=pyqtSignal(int)
    signal3=pyqtSignal()

    def __init__(self):
        super(NtoN, self).__init__()

        self.signal1.connect(self.call1)#一对多绑定
        self.signal1.connect(self.call11)

        self.signal3.connect(self.call1)

        self.signal1.emit()#调用
        self.signal3.emit()

        self.signal2.connect(self.call1)

        self.signal2.emit(2)#传入一个参数

        self.signal1.disconnect(self.call1)
        self.signal1.disconnect(self.call11)
        self.signal2.disconnect(self.call1)
        print("************************")
        self.signal1.connect(self.call1)
        self.signal2.connect(self.call2)

        self.signal1.emit()
        self.signal2.emit(100)

    def call1(self):
        print("signal1 emitted")
    def call11(self):
        print("signal1_1 emitted")
    def call2(self,val):
        print("signal2 emitted,value=",val)

if __name__ == "__main__":
    do=NtoN()