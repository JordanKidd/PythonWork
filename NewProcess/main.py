"""
    This is an example of spawning a new python process (with its own interpreter
    env, GIL, memory, etc.) that handles a new task.

    Also, shows a concurrent task as both are running together, in parallel.
"""
import os
import subprocess as sp
from sys import executable
from time import sleep

__author__ = 'Jordan'


def main():
    """
    Begins the example.
    """

    print("Parent starting waiting example...")
    # Executable says use THIS python program exec:
    sp.call([executable, os.path.dirname(os.path.realpath(__file__)) + r"\child.py"])
    print("Parent done waiting.")

    print("Parent starting concurrent example...")
    sp.Popen([executable, os.path.dirname(os.path.realpath(__file__)) + r"\child.py"])
    for num in range(10):
        print("Parent running:", num)
        sleep(.5)
    print("Parent done.\n")

    sleep(1)

    # -------  Now an example with using the multiprocessing module:  ------
    from multiprocessing import Process

    print("\nStarting example to pass information and use something in the same file...")
    list_one = ["This", "is", "a", "passed", "list."]
    child = Process(target=child_function, args=list_one)
    child.start() # runs process
    child.join() # this makes the parent block until the child process terminates
    print("Back in parent process and finished.")

    sleep(1)

    print("\nStarting example to pass information and use something in the same file...")
    powers_of_2 = [2**x for x in range(0, 64)]
    child_two = Process(target=child_function, args=powers_of_2)
    child_two.start() # runs process, no join so parent continues immediately
    print("This will print before the child's list_two.")


def child_function(*args):
    """
    This is a function that is the target of the new processes.
    """
    print("In child and starting to print list...")
    for num in args:
        print(num)


if __name__ == '__main__':
    main()
