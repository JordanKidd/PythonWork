__author__ = 'jordankidd'


import os
import sys
import csv


def main():
    ''' Program to open a file, sort by price,
        then print to stdout
    '''
    try:
        curdir = os.getcwd()
        path = curdir + '/data.csv'
        file = open(path)
        reader = csv.reader(file)
    except (IOError, TypeError) as e:
        print("Sorter.py error:\n" + str(e), file=sys.stderr)

    #Headers:
    headers = GetHeaders(reader)

    #Records (Asc):
    records = GetRecords(reader)
    sorted = SortRecords(records)
    print("Ascending Price:")
    print(FormatHeading(headers))
    for row in sorted:
        print(FormatRecord(row))

    #Records (Desc)
    sorted.reverse()
    print("\nDescending Price:")
    print(FormatHeading(headers))
    for row in sorted:
        print(FormatRecord(row))


def FormatHeading(heading):
    ''' Formats the column headers to match data records
        Returns
    '''
    return "{:<12} {:<30} {:<13} {:>16}".format(heading[0], heading[1], heading[2], heading[3])


def FormatRecord(rec):
    ''' Formats the column headers to match data records
        Returns
    '''
    return "{:<12} {:<30} {:<13} {:>16}".format(rec[0], rec[1], rec[2], rec[3])


def GetHeaders(reader):
    ''' Param 1, csv.reader object
        Returns the headings in a list
    '''
    return next(reader)


def GetRecords(reader):
    ''' Param 1, csv.reader object
        Returns a list containing all records
        from the csv file
    '''
    list = []
    rownum = 0
    for row in reader:
        if rownum == 0:
            pass #skip column headings
        else:
            list.append(row)
        rownum += 1
    return list


def SortRecords(records):
    ''' Purpose: to sort the data by price
        Param 1, records a list containing a list of strs
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
