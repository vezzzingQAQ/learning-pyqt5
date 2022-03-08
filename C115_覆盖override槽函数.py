'''
2021.1.29,IVICX D.S. C115;覆盖槽函数
'''
'''
ex:覆盖键盘按下的槽
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class OverrideSlot(QMainWindow):
    def __init__(self):
        super(OverrideSlot, self).__init__()
        self.setWindowTitle("覆盖槽函数")
        self.label1=QLabel(self)
        self.setCentralWidget(self.label1)
    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Escape:
            self.close()#按ESC键关闭窗口
        elif e.key()==Qt.Key_Alt:
            self.setWindowTitle("A")
        else:
            self.label1.setText(str(e.key()))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = OverrideSlot()
    main.show()
    sys.exit(app.exec_())