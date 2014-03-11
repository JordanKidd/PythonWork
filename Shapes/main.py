__author__ = 'jordankidd'

from Square import Square
from Triangle import Triangle
from Circle import Circle
#NOTE: must pull the CLASS from their NAMESPACE (file name)! from NS imp CL


def main():
    """Start of program for shapes and inheritance"""

    print("Shapes and inheritance practice in Python (v3.3.4)")

    circ = Circle(2)
    tri = Triangle(19, 13.2)
    sq = Square(11)

    print("Circle area: " + str(circ.area()))
    print("Square area: " + str(sq.area()))
    print("Triangle area: " + str(tri.area()))
    print("")
    print("Circle perimeter: " + str(circ.perimeter()))
    print("Square perimeter: " + str(sq.perimeter()))
    print("Triangle perimeter: " + str(tri.perimeter()))

if __name__ == '__main__':
    main()