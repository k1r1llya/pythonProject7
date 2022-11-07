from PIL.ImageQt import ImageQt
from PyQt5 import uic
import sys
from PIL import Image, ImageDraw
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

SIZE = 0
h = 100
w = 100


class miniPhotoshop(QMainWindow):
    def __init__(self):
        super(miniPhotoshop, self).__init__()
        uic.loadUi('грг.ui', self)
        self.createbtn_2.clicked.connect(self.create_)
        self.dwnld.clicked.connect(self.dwnld_)
        #self.instruct_but.connect(self.instruct)

    def create_(self):
        self.dialog = clssCreater()
        self.dialog.show()

    def dwnld_(self):
        self.dwnld = clasdwnld()
        self.dwnld.show()

    def instruct(self):
        self.instruction = clssInstruct()
        self.instruction.show()


class clssCreater(QDialog):
    def __init__(self):
        super(clssCreater, self).__init__()
        uic.loadUi('creater.ui', self)
        self.btncreation.clicked.connect(self.getthis)

    def getthis(self):
        global h
        global w
        h = int(self.height_b.text())
        w = int(self.width_b.text())
        self.pr2ject = prject()
        self.pr2ject.show()


class clssInstruct(QDialog):
    def __init__(self):
        super(clssInstruct, self).__init__()
        #uic.loadUi('instruction.ui')

class prject(QDialog):
    def __init__(self):
        global h
        global w
        self.h = h
        self.w = w
        super(prject, self).__init__()
        uic.loadUi('Picture.ui', self)
        self.qp = QPainter()
        self.setGeometry(500, 200, 599, 599)
        self.setWindowTitle('Draw version 0.1')
        self.button_for_pen_color.clicked.connect(self.set_color)
        self.button_for_width.clicked.connect(self.set_pen_width)
        self.btnSave.clicked.connect(lambda: prject().image.save("image.png", "PNG"))
        self.pen_color = Qt.green
        self.pen_width = 10
        self.image = QImage(self.h, self.w, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.clearImage()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def clearImage(self):
        self.path = QPainterPath()
        self.image.fill(Qt.white)
        self.update()

    def set_pen_width(self):
        self.pen_width = 67

    def type_man(self):
        self.type_file = 0

    def saveImage(self, fileName, fileFormat):
        self.image.save(fileName, fileFormat)

    def set_color(self):
        prject().saveImage("image.png", "PNG")
        self.image = QImage("image.png")
        self.pen_color = QColorDialog.getColor()

    def get_figure(self):
        self.figure_chooser = clssFigure_chooser()
        self.figure_chooser.show()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.pen_color,
                      self.pen_width, Qt.SolidLine, Qt.RoundCap,
                      Qt.RoundJoin))
        p.drawPath(self.path)
        p.end()
        self.update()

class clssFigure_chooser(QDialog):
    def __init__(self):
        super(clssFigure_chooser, self).__init__()
        uic.loadUi('figureclass.ui', self)



class clasdwnld(QDialog):
    def __init__(self):
        super(clasdwnld, self).__init__()
        self.flag = None
        uic.loadUi('dwnldproject.ui',self)
        self.app = app
        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
        self.orig_image = Image.open(self.filename)
        self.curr_image = Image.open(self.filename)
        self.degree = 0
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image123.setPixmap(self.pixmap)
        self.change_color.clicked.connect(self.set_channel)
        self.change_color.clicked.connect(self.rotate)

    def keyPressEvent(self,event):
        if event.key() == Qt.Key_R:
            self.flag = 1
        elif event.key() == Qt.Key_G:
            self.flag = 2
        elif event.key() == Qt.Key_B:
            self.flag = 3

    def set_channel(self):
        self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if self.flag == 1:
                    pixels[i, j] = r, 0, 0
                if self.flag == 2:
                    pixels[i, j] = 0, g, 0
                if self.flag == 3:
                    pixels[i, j] = 0, 0, b
                else:
                    pass
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image123.setPixmap(self.pixmap)

    def rotate(self):
        self.degree += int(self.comboBox.currentText())
        degree = 90
        self.degree %= 360
        self.curr_image = self.curr_image.rotate(degree, expand=True)
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image123.setPixmap(self.pixmap)

    def except_hook(clc, exception, traseback):
        sys.__excepthook__(clc, exception, traseback)


    #class letters_modifier(QDialog):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mp = miniPhotoshop()
    mp.show()
    sys.exit(app.exec())
