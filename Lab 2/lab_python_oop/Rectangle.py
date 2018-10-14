from lab_python_oop.Colours import Colours
from lab_python_oop.GeometricFigures import GeometricFigures

class Rect(GeometricFigures):
    _square_ = 0
    _width_ = 0
    _length_ = 0
    figure = "Прямоугольник"

    def __init__(self, leng, w, col):
        self._width_ = w
        self._length_ = leng
        self.color = Colours(col)

    def find_square(self):
        self._square_ = self._width_ * self._length_
        return self._square_

    def repr(self):
        return '{} цвета {} высотой {} и шириной {}, площадью  {}'.format(self.figure, self.color.colour, self._length_,
                                                                          self._width_, self.find_square())