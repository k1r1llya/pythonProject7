import sys

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Drawer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        self.h = 400
        self.w = 400
        self.myPenColor = Qt.green
        self.myPenWidth = 10
        self.image = QImage(self.h, self.w, QImage.Format_RGB32)
        self.im = Image.new("RGB", (500, 500), (255, 255, 255))
        self.im.save("nwepict.jpg")
        self.path = QPainterPath()
        self.clearImage()

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.path = QPainterPath()
        self.image.fill(Qt.white)
        self.update()

    def saveImage(self, fileName, fileFormat):
        self.image.save(fileName, fileFormat)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def set_color(self):
        self.path = QPainterPath()
        self.image.fill(Qt.white)
        self.curr_image = Image.open('nwepict.jpg')
        self.image = ImageQt(self.curr_image)
        print(self.image)
        self.myPenColor = QColorDialog.getColor()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.myPenColor,
                    self.myPenWidth, Qt.SolidLine, Qt.RoundCap,
                    Qt.RoundJoin))
        p.drawPath(self.path)
        p.end()
        Drawer().saveImage("nwepict.jpg", "JPG")
        self.update()



    def sizeHint(self):
        return QSize(300, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QDialog()
    btnSave  = QPushButton("Сохранить изображение -> image.png")
    btnClear = QPushButton("Очистить холст")
    drawer   = Drawer()

    w.setLayout(QVBoxLayout())
    w.layout().addWidget(btnSave)
    w.layout().addWidget(btnClear)
    w.layout().addWidget(drawer)

    btnSave.clicked.connect(drawer.set_color)#lambda: drawer.saveImage("image.jpg", "JPG"))
    btnClear.clicked.connect(drawer.clearImage)

    w.show()
    sys.exit(app.exec_())
