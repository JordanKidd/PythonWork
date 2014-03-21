__author__ = 'jordankidd'


import os
import sys
import csv


def main():
    ''' Program to open a file named 'data.csv',
        sort by price column, then print to stdout.
        REQUIRES PYTHON 3+ to run!
        Author: Jordan Kidd
    '''

    try:
        curdir = os.getcwd()
        path = curdir + '/data.csv'
        print('\nUsing data from: ' + path + '\n')
        file = open(path)
        file.seek(0)
        reader = csv.reader(file)

        #Column Headers:
        headers = GetHeaders(reader)
        #Records:
        records = GetRecords(reader)

        #Records (Original):rea
        print('Unsorted:')
        print(FormatHeading(headers))
        for row in records:
            print(FormatRecord(row))

        #Records (Asc):
        sorted = SortRecords(records)
        print('\nAscending Price:')
        print(FormatHeading(headers))
        for row in sorted:
            print(FormatRecord(row))

        #Records (Desc):
        sorted.reverse()
        print('\nDescending Price:')
        print(FormatHeading(headers))
        for row in sorted:
            print(FormatRecord(row))

    except (IOError, TypeError) as e:
        print('Sorter.py error:\n' + str(e), file = sys.stderr)


def FormatHeading(heading):
    ''' Formats the column headers to match data records
        Returns the formatted string
    '''
    return '{:<12} {:<30} {:<13} {:>16}'.format(heading[0], heading[1], heading[2], heading[3])


def FormatRecord(rec):
    ''' Formats the column headers to match data records
        Param1:
        Returns the formatted string
    '''
    return '{:<12} {:<30} {:<13} {:>16}'.format(rec[0], rec[1], rec[2], rec[3])


def GetHeaders(reader):
    ''' Should be called before GetRecords()
        Param1: csv.reader object
        Returns the headings in a list
    '''
    return next(reader)


def GetRecords(reader):
    ''' Should be called after GetHeaders()
            (or first read should be skipped, because of headings)
        Param 1: csv.reader object
        Returns a list containing all records
        from the csv file
    '''
    list = []
    rownum = 0
    for row in reader:
        list.append(row)
        rownum += 1
    return list


def SortRecords(records):
    ''' Sorts the records object the data by price, records[3]
        Param 1: records a list containing a list of strs
        Returns: a new sorted list
    '''
    final_length = len(records)
    sorted = []
    copy = records

    #ASC Price:
    while len(sorted) != final_length:
        lowestPrice = sys.float_info.max
        x_to_add = -1
        for x in range(len(copy)):
            if float(copy[x][3]) < float(lowestPrice):
                lowestPrice = copy[x][3]
                x_to_add = x
        sorted.append(copy[x_to_add])
        copy.remove(copy[x_to_add])
    return sorted


if __name__ == '__main__':
    main()
