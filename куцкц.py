import sys
from PIL import Image, ImageDraw
# создание изображения
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QColorDialog, QWidget, QLabel, QPushButton
from PyQt5 import uic

SIZE = 0


class miniPhotoshop(QMainWindow):
    def __init__(self):
        super(miniPhotoshop, self).__init__()
        uic.loadUi('грг.ui', self)
        self.createbtn_2.clicked.connect(self.create_)

    def create_(self):
        self.dialog = clssCreater()
        self.dialog.show()


class clssCreater(QDialog):
    def __init__(self):
        super(clssCreater, self).__init__()
        uic.loadUi('creater.ui', self)
        self.btncreation.clicked.connect(self.getthis)

    def getthis(self):
        self.project = prject()
        self.project.show()


class prject(QDialog):
    def __init__(self):
        super(prject, self).__init__()
        uic.loadUi('Picture.ui', self)
        self.coords_ = []
        self.qp = QPainter()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Пятая программа')
        self.new_image = Image.new("RGB", (1000,1000), (0,255,255))
        self.new_image.save('new_image.jpg')
        self.pixmap = QPixmap('new_image.jpg')
        self.Picture = QLabel(self)
        self.Picture.resize(100,500)
        self.Picture.move(70,70)
        self.Picture.setPixmap(self.pixmap)
        self.coords =QLabel(self)
        self.coords.setText("Координаты: None , None")
        self.coords.move(30, 30)
        #self.button = QPushButton(self)
        #self.button.resize(100,100)
        #self.button.move(100,100)
        #self.button.clicked.connect(self.get_pict)
    #def get_pict(self):
        #self.Label.setPixmap(self.qp)
    def mouseMoveEvent(self, event):
        self.coords_.append(event.pos())                   #QPoint(int(event.x()), int(event.y()))
        self.update()

    def paintEvent(self,event):
        qp = QPainter(self)
        qp.drawImage(self.rect(), QImage('new_image.jpg'))
        print(QImage('new_image.jpg'))
        pen = QPen()
        pen.setWidth(2)
        qp.setPen(pen)
        qp.setRenderHint(QPainter.Antialiasing, True)
        for pos in self.coords_:
            qp.drawPoint(pos)
        #self.qp_= QPixmap(qp)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mp = miniPhotoshop()
    mp.show()
    sys.exit(app.exec())
