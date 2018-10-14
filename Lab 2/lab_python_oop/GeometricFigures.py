from abc import ABCMeta, abstractmethod


class GeometricFigures():
    __metaclass__ = ABCMeta
    _square_ = 0

    @abstractmethod
    def find_square(self):
        pass
