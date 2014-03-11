__author__ = 'jordankidd'

from Shape import Shape
#NOTE: must pull the CLASS from their NAMESPACE (file name)! "from NS imp CL"


class Triangle(Shape):
    """Triangle shape"""

    height = 0.0
    base = 0.0
    sideb = 0.0
    sidec = 0.0

    def __init__(self, base, sideb, sidec, h):
        """Base, side B, side C, then height"""
        self.base = base
        self.sideb = sideb
        self.sidec = sidec
        self.height = h

    def perimeter(self):
        """Adds the 3 sides and returns perimeter"""
        return self.base + self.sideb + self.sidec

    def area(self):
        """Base * Height * 1/2"""
        return self.base * self.height * 0.5
