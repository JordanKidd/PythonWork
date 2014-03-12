__author__ = 'jordankidd'

from Shape import Shape
#NOTE: must pull the CLASS from their NAMESPACE (file name)! "from NS imp CL"

class Square(Shape):
    """Square shape"""

    length = 0.0

    def __init__(self, l):
        """l is the length of a side"""
        self.length = l

    def perimeter(self):
        """Returns the perimeter of the square l*4"""
        return self.length * 4

    def area(self):
        """Returns the area of the square, l^2"""
        return self.length * self.length
