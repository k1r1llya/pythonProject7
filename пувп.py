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
type_file = ''
file_name = ''
flag_for_square = False
flag_for_triangle = False
flag_for_round = False
EVENTLOG = []
penwidth = 10


class miniPhotoshop(QMainWindow):
    def __init__(self):
        super(miniPhotoshop, self).__init__()
        uic.loadUi('грг.ui', self)
        self.createbtn_2.clicked.connect(self.create_)
        self.dwnld.clicked.connect(self.dwnld_)
        self.instruct_but.clicked.connect(self.instruct)

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
        global file_name
        global type
        h = int(self.height_b.text())
        w = int(self.width_b.text())
        file_name = self.lineEdit.text()
        type = self.comboBox.currentText()
        self.Drawer = PROJECT()
        self.Drawer.show()


class Drawerd(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        self.h = h
        self.w = w
        self.myPenColor = Qt.black
        self.myPenWidth = 10
        self.image = QImage(self.h, self.w, QImage.Format_RGB32)
        self.im = Image.new("RGB", (500, 500), (255, 255, 255))
        self.im.save("nwepict.jpg")
        self.path = QPainterPath()
        self.clearImage()

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
        self.myPenColor = QColorDialog.getColor()
        print(self.myPenColor)

    def mouseMoveEvent(self, event):
        global flag_for_square
        global flag_for_triangle
        global flag_for_round
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.myPenColor,
                      self.myPenWidth, Qt.SolidLine, Qt.RoundCap,
                      Qt.RoundJoin))
        print(self.myPenColor, self.myPenWidth)
        if flag_for_round == True:
            p.drawEllipse(event.x(), event.y(), 55, 43)
            flag_for_round = False
        if flag_for_square == True:
            p.drawRect(event.x(), event.y(), 55, 43)
            flag_for_square = False
        if flag_for_triangle == True:
            self.path.moveTo(event.x() - 50, event.y())
            self.path.lineTo(event.x(), event.y() + 50)
            self.path.lineTo(event.x() + 50, event.y())
            self.path.lineTo(event.x() - 50, event.y())
            p.drawPath(self.path)
            flag_for_triangle = False
        else:
            p.drawPath(self.path)
        p.end()
        self.saveImage("nwepict.jpg", "JPG")
        self.update()

    def clearImage(self):
        self.path = QPainterPath()
        self.image.fill(Qt.white)
        self.update()

    def set_pen_width(self):
        global penwidth
        self.pen_width_getter = penWIDTH()
        self.pen_width_getter.show()
        self.myPenWidth = penwidth

    def type_man(self):
        self.type_file = 0

    def saveImage(self, fileName, fileFormat):
        self.image.save(fileName, fileFormat)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def get_figure(self):
        self.figure_chooser = clssFigure_chooser()
        self.figure_chooser.show()


class PROJECT(QDialog):
    def __init__(self):
        super(PROJECT, self).__init__()
        uic.loadUi('Picture.ui', self)
        self.button_for_pen_color.clicked.connect(Drawerd(self).set_color)
        self.figure_Chooser.clicked.connect(Drawerd(self).get_figure)
        self.button_for_width.clicked.connect(Drawerd(self).set_pen_width)
        self.widhet = Drawerd(self)
        self.widhet.move(200, 200)
        self.widhet.resize(400, 400)


# class clssFigure_chooser(QDialog):
# def __init__(self):
# super(clssFigure_chooser, self).__init__()
# uic.loadUi('figureclass.ui', self)


class clasdwnld(QDialog):
    def __init__(self):
        super(clasdwnld, self).__init__()
        self.flag = None
        uic.loadUi('dwnldproject.ui', self)
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

    def keyPressEvent(self, event):
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

    def savve(self):
        pass


class clssInstruct(QDialog):
    def __init__(self):
        super(clssInstruct, self).__init__()
        uic.loadUi('instr.ui', self)
        self.btndwnldinstruct.clicked.connect(self.dwnld)

    def dwnld(self):
        file = open('dfdfdf')  # чек виз


class clssFigure_chooser(QDialog):
    def __init__(self):
        super(clssFigure_chooser, self).__init__()
        uic.loadUi('TRINGLECHOOSER.ui', self)
        self.OKman.clicked.connect(self.da)

    def da(self):
        global flag_for_square
        global flag_for_triangle
        global flag_for_round
        if self.figure.currentText() == 'Треугольник':
            flag_for_triangle = True
        elif self.figure.currentText() == 'Кружочек':
            flag_for_round = True
        elif self.figure.currentText() == 'Квадрат':
            flag_for_square = True
        # elif self.figure.itemText() :
        # flag_for_t
        # elif self.figure.itemText()


class log_creater(QWidget):
    def __init__(self):
        super(log_creater, self).__init__()
        uic.loadUi('logi.ui', self)
        # .......

    def yescreate(self):
        pass
        # csv

    def yescreatebutsql(self):
        pass
        # sql


class penWIDTH(QDialog):
    def __init__(self):
        super(penWIDTH, self).__init__()
        uic.loadUi('penwidther.ui', self)
        self.widebtn_2.clicked.connect(self.geetwid)

    def geetwid(self):
        global penwidth
        penwidth = int(self.widthline.text())
        print(penwidth)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mp = miniPhotoshop()
    mp.show()
    sys.exit(app.exec())
