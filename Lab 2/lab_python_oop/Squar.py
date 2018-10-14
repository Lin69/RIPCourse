from lab_python_oop.Colours import Colours
from lab_python_oop.Rectangle import Rect


class Squar(Rect):
    figure = "Квадрат"

    def __init__(self, side, col):
        self._length_ = side
        self._width_ = side
        self.color = Colours(col)

    def repr(self):
        return '{} цвета {} со стороной {} и площадью  {}'.format(self.figure, self.color.colour, self._width_,
                                                                  self.find_square())
