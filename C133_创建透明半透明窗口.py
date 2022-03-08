'''
2021.2.1,IVICX D.S. C133;创建透明半透明窗口
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class WindowA(QWidget):
    def __init__(self):
        super(WindowA, self).__init__()

        self.setWindowTitle("缩放图片")

        self.setWindowOpacity(0.5)

        filename = "./images/5.jpg"
        img = QImage(filename)

        self.label1 = QLabel(self)
        self.label1.move(0, 0)
        self.label1.resize(self.width(), self.height())

        result = img.scaled(self.label1.width(), self.label1.height(),
                            Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # 忽略比例，平滑显示
        self.label1.setPixmap(QPixmap.fromImage(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowA()
    main.show()
    sys.exit(app.exec_())