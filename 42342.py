import sys

from PIL import Image
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Drawer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        h = 400
        w = 400
        self.myPenWidth = 10
        self.myPenColor = Qt.blue
        self.image = QImage(w, h, QImage.Format_RGB32)
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

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.myPenColor,
                      self.myPenWidth, Qt.SolidLine, Qt.RoundCap,
                      Qt.RoundJoin))
        p.drawPath(self.path)
        p.end()
        self.update()


    def set_color(self):
        Drawer().saveImage("image.png", "PNG")
        self.image = Image.open("image.png")
        self.myPenColor = QColorDialog.getColor()

    def sizeHint(self):
        return QSize(300, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    btnSave  = QPushButton("Сохранить изображение -> image.png")
    btnClear = QPushButton("Очистить холст")
    btncolor = QPushButton("цвет")
    drawer   = Drawer()

    w.setLayout(QVBoxLayout())
    w.layout().addWidget(btnSave)
    w.layout().addWidget(btnClear)
    w.layout().addWidget(drawer)
    w.layout().addWidget(btncolor)
    btnSave.clicked.connect(lambda: drawer.saveImage("image.png", "PNG"))
    btnClear.clicked.connect(drawer.clearImage)
    btncolor.clicked.connect(drawer.set_color)

    w.show()
    sys.exit(app.exec_())