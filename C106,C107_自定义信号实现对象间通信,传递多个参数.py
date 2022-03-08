'''
2021.1.28,IVICX D.S. C106;自定义信号实现对象间通信
2021.1.29,IVICX D.S. C107;传递多个参数
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class mytypeSignal(QObject):
    #定义一个信号
    sendMessage=pyqtSignal(object)
    sendMessage2=pyqtSignal(str,int,int)
    def run(self):
        self.sendMessage.emit("Hello PyQt5")
    def run1(self):
        self.sendMessage2.emit("hello",2,3)

class mytypeSlot(QObject):
    def get(self,message):
        print("信息"+message)
    def get1(self,message,a,b):
        print(message,a,b)

if __name__ == "__main__":
    send=mytypeSignal()
    slot=mytypeSlot()

    send.sendMessage.connect(slot.get)
    send.sendMessage2.connect(slot.get1)

    send.run()
    send.run1()

    send.sendMessage.disconnect(slot.get)#断开连接

    send.run()