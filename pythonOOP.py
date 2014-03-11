#-------------------------------------------------------------------------------
# Name:        pythonOOP
# Purpose:     OO Python example
#              Shows the Python v3 way of doing OOP
#
# Author:      Jordan
#
# Created:     10/05/2013
# Copyright:   (c) Jordan 2013
#-------------------------------------------------------------------------------


class Person:
    """base class for all people"""
    name = ""
    age = 0
    weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def SayInformation(self):
        print("Hi my name is " + str(self.name) + ". I'm " + str(self.age) +
              " years old and weigh " + str(self.weight) + ".")


class CollegeStudent(Person):
    """Inherits from Person class. A student"""
    studentIDNum = -1
    major = ""
    minor = ""
    year = ""
    GPA = 0.0

    def __init__(self, name, age, studentIDNum, major, minor, year, gpa):
        self.name = name
        self.age = age
        self.studentIDNum = studentIDNum
        self.major = major
        self.minor = minor
        self.year = year
        self.GPA = gpa

    def SayInformation(self):
        print("My name is " + self.name + " and I'm studying " + self.major +
              " and " + self.minor + ". My ID Number is: " +
              str(self.studentIDNum) + ". My GPA is: " + str(self.GPA) + ".")


class Employee(Person):
    """This is an employee class, a child of Person"""
    employeeNumber = 0
    employeeSalary = 0

    def __init__(self, empId, salary, name, age, weight):
        self.employeeNumber = empId
        self.employeeSalary = salary
        self.name = name
        self.age = age
        self.weight = weight
        """passes the rest to the base constructor and fills in the info"""

    def sayNumber(self):
        print("My number is: " + str(self.employeeNumber))

    def saySalary(self):
        print("I make " + str(self.employeeSalary) + "!")


class StudentEmployee(CollegeStudent, Employee):
    """Student worker class that has 2 properties"""

    def __init__(self, empId, salary, name, age, weight, major, minor, gpa):
        self.empId = empId
        self.salary = salary
        self.name = name
        self.age = age
        self.weight = weight
        self.major = major
        self.minor = minor
        self.gpa = gpa

    def sayBoth(self):
        self.SayInformation()
        self.saySalary()


#------------MAIN------------------------


def main():
    """Your normal main()"""
    jordan = Person("Jordan", 23, 132)
    jordan.SayInformation()
    print('')

    corey = Person("Corey", 26, 115)
    corey.SayInformation()
    print('')

    ManagerBob = Employee(54285, 120000, "Manager Bob", 40, 180)
    ManagerBob.SayInformation()
    ManagerBob.saySalary()
    ManagerBob.sayNumber()
    print('')

    StudentKelly = CollegeStudent("Kelly", 18, 42312, "Nursing", "Biology",
                                  "Freshman", 2.8)
    StudentKelly.SayInformation()
    print('')

    InternBill = StudentEmployee(333, 8000, "Bill Intern", 23, 130, "CS",
                                 "Math", 3.14)
    InternBill.sayBoth()

if __name__ == '__main__':
    main()
