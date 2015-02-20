__author__ = 'Jordan'


from time import sleep


"""
Child process called by main that runs in its own Python environment.
"""
def main():
    for x in range(10):
        print("Child running:", x)
        sleep(.5)
    print("Child done.")


if __name__ == '__main__':
    main()