import sys
import os
import pdb


def main(args):
    print('My Python debugging example...')
    a = 3 #int
    b = 3.14159 #float
    c = [1, 2, 3, '4', '5', 3.444, 5.15] #list
    d = ('23', 4, '12', 'abcde') #tuple
    # Tuples can be thought of as read-only lists
    e = {1:'val1', 2:'val2', 3:'val3'} #dictionary
    f = 'string' #string

    pdb.set_trace()
    #use 'pdb.set_trace()' to set a breakpoint on run!
    x = 'ls'
    y = ['ls -l -a'] #Python list
    os.execvp(x,y)  #uses execvp(arg[0], whole cmd line) and runs it


if __name__ == '__main__':
    main(sys.argv)