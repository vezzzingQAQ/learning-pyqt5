'''
2021.2.1,IVICX D.S. C130;装载GIF动画
'''
import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie#装载GIF动画

class LoadingGif(QWidget):
    def __init__(self):
        super(LoadingGif, self).__init__()

        self.setWindowFlags(Qt.Dialog|Qt.CustomizeWindowHint)

        self.label=QLabel("",self)
        self.movie=QMovie("./images/G1.gif")

        self.label.setMovie(self.movie)

        self.setFixedSize(608, 488)

        self.movie.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LoadingGif()
    main.show()
    sys.exit(app.exec_())