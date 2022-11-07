import sys
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *

class QColorButton(QPushButton):
    ''' Пользовательский виджет Qt, чтобы отобразить выбранный цвет.
    Щелчок левой кнопкой мыши на кнопке показывает выбор цвета, в то время как
    щелчок правой кнопкой мыши сбрасывает цвет до None (без цвета).         '''

    colorChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(QColorButton, self).__init__(*args, **kwargs)

        self._color = None
        self.setWindowTitle("QColorButton(QPushButton)")
        self.setText("""
      QColorButton:

    - сделайте Left-click
        или
    - сдулайте Right-click. """)
        self.pressed.connect(self.onColorPicker)

    def setColor(self, color):
        if color != self._color:
            self._color = color
            self.colorChanged.emit()

        if self._color:
            self.setStyleSheet("background-color: %s;" % self._color)
        else:
            self.setStyleSheet("")

    def color(self):
        return self._color

    def onColorPicker(self):
        '''  Диалоговое окно выбора цвета .
        По умолчанию Qt будет использовать собственный диалог.  '''

        dlg = QColorDialog(self)
        if self._color:
            dlg.setCurrentColor(QColor(self._color))

        if dlg.exec_():
            self.setColor(dlg.currentColor().name())

    def mousePressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.setColor(None)

        return super(QColorButton, self).mousePressEvent(e)

app    = QApplication([])
window = QColorButton()
window.show()
app.exec_()
