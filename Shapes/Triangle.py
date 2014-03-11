__author__ = 'jordankidd'

from Shape import Shape
#NOTE: must pull Shape CLASS from the Shape NAMESPACE!!


class Triangle(Shape):
    """Triangle shape"""

    height = 0.0
    sidea = 0.0
    sideb = 0.0
    sidec = 0.0

    def __init__(self, sidea, sideb, sidec, h):
        self.height = h
        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec

    def perimeter(self):
        """Adds the 3 sides and returns perimeter"""
        return self.sidea + self.sideb + self.sidec

    def area(self):
        """Base * Height * 1/2"""
        return self.base * self.height * 0.5
