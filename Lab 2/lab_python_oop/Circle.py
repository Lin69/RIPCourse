from lab_python_oop.Colours import Colours
from lab_python_oop.GeometricFigures import GeometricFigures
from math import pi


class Circle(GeometricFigures):
    _radius_ = 0
    _square_ = 0
    figure = "Круг"

    def __init__(self, radius, col):
        self._radius_ = radius
        self.color = Colours(col)

    def find_square(self):
        self._square_ = pi * self._radius_ * self._radius_
        return self._square_

    def repr(self):
        return '{} цвета {} с радиусом {} и площадью {}'.format(self.figure, self.color.colour, self._radius_,
                                                                self.find_square())
