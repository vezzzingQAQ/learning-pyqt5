'''
2021.2.1,IVICX D.S. C132;缩放图片
'''
'''
QImage.scaled
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ScaleImage(QWidget):
    def __init__(self):
        super(ScaleImage, self).__init__()

        self.setWindowTitle("缩放图片")

        filename="./images/5.jpg"
        img=QImage(filename)

        self.label1=QLabel(self)
        self.label1.move(0,0)
        self.label1.resize(self.width(),self.height())

        result=img.scaled(self.label1.width(),self.label1.height(),
                          Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        #忽略比例，平滑显示
        self.label1.setPixmap(QPixmap.fromImage(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ScaleImage()
    main.show()
    sys.exit(app.exec_())