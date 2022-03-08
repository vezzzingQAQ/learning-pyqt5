'''
2021.1.29,IVICX D.S. C108;为类添加多个信号
'''

from PyQt5.QtCore import *
import sys

class multiSignal(QObject):
    signal1=pyqtSignal()
    signal2=pyqtSignal(int)
    signal3=pyqtSignal(int,str)
    signal4=pyqtSignal(list)
    signal5=pyqtSignal(dict)
    #声明一个重载版本的信号
    signal6=pyqtSignal([int,str],[str])#两选一即可

    def __init__(self):
        super(multiSignal, self).__init__()

        self.signal1.connect(self.signalcall1)
        self.signal2.connect(self.signalcall2)
        self.signal3.connect(self.signalcall3)
        self.signal4.connect(self.signalcall4)
        self.signal5.connect(self.signalcall5)

        #重载的关联方法***********************************
        self.signal6[str].connect(self.signalcall6_2)
        self.signal6[int,str].connect(self.signalcall6_1)

        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(1,"hello world")
        self.signal4.emit([1,2,3,4,5])
        self.signal5.emit({"name":"vezzing","age":"2000"})
        self.signal6[str].emit("dadawa")
        self.signal6[int,str].emit(100,"vervrv")

    def signalcall1(self):
        print("signal1 emitted")
    def signalcall2(self,val):
        print("signal2 emitted,value=",val)
    def signalcall3(self,val,text):
        print("signal3 emitted,value=",val,text)
    def signalcall4(self,val):
        print("signal4 emitted,value=",val)
    def signalcall5(self,val):
        print("signal5 emitted,value=",val)
    def signalcall6_1(self,val,text):
        print("signal6_1 emitted,value=",val,text)
    def signalcall6_2(self,text):
        print("signal6_2 emitted,value=",text)

if __name__ == "__main__":
    mul=multiSignal()
