__author__ = 'jordankidd'

from pydoc import help
from Square import Square
from Triangle import Triangle
from Circle import Circle
#NOTE: must pull the CLASS from their NAMESPACE (file name)! "from NS imp CL"


def main():
    """Start of program for shapes and inheritance"""

    print("\nShapes and inheritance practice in Python (v3.3.5)")

    circ = Circle(3)
    tri = Triangle(4, 5, 7, 5.7)
    sq = Square(11)

    #To print out pydocs: print(help(circ))
    print("Circle area: " + str(circ.area()))
    print("Square area: " + str(sq.area()))
    print("Triangle area: " + str(tri.area()))
    print("Circle perimeter: " + str(circ.perimeter()))
    print("Square perimeter: " + str(sq.perimeter()))
    print("Triangle perimeter: " + str(tri.perimeter()))

if __name__ == '__main__':
    main()