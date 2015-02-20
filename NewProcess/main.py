__author__ = 'Jordan'

import subprocess as sp
import child
from time import sleep

"""
This is an example of spawning a new python process (with its own interpreter env)
that handles a new task while the calling one waits.

Also, showing a concurrent task as both are running together.
"""
def main():
    print("Parent starting waiting example...")
    # pid = sp.Popen("python child.py")
    # pid.wait()
    # OR ONE COULD USE:
    pid = sp.call("python child.py")
    print("Parent done waiting.")

    print("Parent starting concurrent example...")
    pid = sp.Popen("python child.py")
    for x in range(10):
        print("Parent running:", x)
        sleep(.5)
    print("Parent done.")


if __name__ == '__main__':
    main()