def set_color(self):
    self.curr_image = Image.open(f"{file_name}.{type[1:]}")
    self.image = ImageQt(self.curr_image)
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
    while self.flag:
        prject().saveImage(f"{file_name}.{type[1:]}", 'JPG')
        self.flag = False
        continue
    p.end()
    self.update()