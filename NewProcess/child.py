__author__ = 'Jordan'


from time import sleep


"""
Child process created from main
"""
def main():
    for x in range(10):
        print("Child running:", x)
        sleep(.5)


if __name__ == '__main__':
    main()