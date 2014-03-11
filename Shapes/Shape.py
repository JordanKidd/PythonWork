__author__ = 'jordankidd'

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """ Abstract class that defines methods needed for inherited
        classes, like triangle, square, etc.
        Note: metaclass=ABCMeta enforces that this class can't be instantiated"""

    @abstractmethod
    def area(self):
        """Each shape must have an area function. Error if override not used!"""
        pass

    @abstractmethod
    def perimeter(self):
        """Each shape must have a perimeter function. Error if override not used!"""
        pass
