__author__ = 'jordankidd'

import os
import sys
import csv

def main():
    ''' Program to open a file named 'data.csv',
        sort by price column, then print to stdout.
        Author: Jordan Kidd
    '''

    try:
        curdir = os.getcwd()
        path = curdir + '/data.csv'
        print('\nUsing data from: ' + path + '\n')
        file = open(path)
        reader = csv.reader(file)

        headers = GetHeaders(reader)
        records = GetRecords(reader)

        print('Unsorted:')
        print(FormatRecord(headers))
        for row in records:
            print(FormatRecord(row))

        #Ascending:
        records = sorted(records, key=lambda rec: float(rec[3]))
        print('\nAscending Price:')
        print(FormatRecord(headers))
        for row in records:
            print(FormatRecord(row))

        #Descending:
        records.reverse()
        print('\nDescending Price:')
        print(FormatRecord(headers))
        for row in records:
            print(FormatRecord(row))

    except (IOError, TypeError) as e:
        print('Sorter.py error:\n' + str(e), file = sys.stderr)

def FormatRecord(rec):
    ''' Formats the column headers and data records for readability
        Returns a single formatted string
    '''
    return '{:<12} {:<30} {:<13} {:>16}'.format(rec[0], rec[1], rec[2], rec[3])

def GetHeaders(reader):
    return next(reader)

def GetRecords(reader):
    list = []
    for row in reader:
        list.append(row)
    return list

if __name__ == '__main__':
    main()