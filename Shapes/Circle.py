__author__ = 'jordankidd'

from Shape import Shape
from math import pi as piconst
#NOTE: must pull Shape CLASS from the Shape NAMESPACE!!


class Circle(Shape):
    """Circle shape"""

    radius = 0.0

    def __init__(self, r):
        self.radius = r

    def perimeter(self):
        """2 * pi * r"""
        return 2 * piconst * self.radius

    def area(self):
        """pi * r^2"""
        return piconst * self.radius * self.radius