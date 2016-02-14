import subprocess as sp
from sys import executable
from time import sleep

__author__ = 'Jordan'


def main():
    """
    This is an example of spawning a new python process (with its own interpreter env)
    that handles a new task while the calling one waits.

    Also, showing a concurrent task as both are running together.
    """

    print("Parent starting waiting example...")
    # Executable says use THIS python program exec:
    pid = sp.call([executable, "child.py"])
    print("Parent done waiting.")

    print("Parent starting concurrent example...")
    pid = sp.Popen([executable, "child.py"])
    for x in range(10):
        print("Parent running:", x)
        sleep(.5)
    print("Parent done.\n")

    sleep(1)

    # ------------------  Now an example with using the multiprocessing module:  --------------------
    from multiprocessing import Process

    print("\nStarting example to pass information and use something in the same file...")
    list_one = ["This", "is", "a", "passed", "list."]
    p = Process(target=childFunction, args=list_one)
    p.start() # runs process
    p.join() # this makes the parent block until the child process terminates
    print("Back in parent process and finished.")

    sleep(1)

    print("\nStarting example to pass information and use something in the same file...")
    powers_of_2 = [2**x for x in range(0, 64)]
    p = Process(target=childFunction, args=powers_of_2)
    p.start() # runs process
    print("This will print before the child's list_two.")


def childFunction(*args):
    print("In child and starting to print list...")
    for x in args:
        print(x)


if __name__ == '__main__':
    main()
