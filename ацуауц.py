import sys
from PIL import Image, ImageDraw
# создание изображения
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QColorDialog, QWidget, QLabel
from PyQt5 import uic

class ImageScroller(QDialog):
    def __init__(self):
        self.chosen_points = []
        super(ImageScroller, self).__init__()
        self._image = QPixmap("new_image.jpg")

    def paintEvent(self, paint_event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self._image)
        pen = QPen()
        pen.setWidth(20)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        for pos in self.chosen_points:
            painter.drawPoint(pos)

    def mouseMoveEvent(self, cursor_event):
        self.chosen_points.append(cursor_event.pos())
        self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = ImageScroller()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())