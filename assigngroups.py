#!/usr/bin/env python3
# assigngroups.py
# 
# MIT License
# 
# Copyright (c) 2017 William Kronholm
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from random import shuffle
import subprocess
import argparse
import datetime
import sys


def validdate(date):
    try:
        datetime.datetime.strptime(date, "%Y%m%d")
        return True
    except ValueError:
        return False


def sendtoprinter(filename):
    """
    Note: this probably only works on Linux machines.
    """
    with open(filename, 'r') as f:
        lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        lpr.stdin.write(f.read())
    print("Go check the printer.")
    return


def main():
    description = "Creates randomly assigned groups of students of similar sizes"
    parser = argparse.ArgumentParser(
        prog='assigngroups',
        description=description
    )
    parser.add_argument(
        '-i', '--in-file',
        help='Name of the file containing the class roster',
        default='students.txt',
        dest='infile'
    )
    parser.add_argument(
        '-o', '--out-file',
        help='Name of the file to write the groups to',
        dest='outfile'
    )
    parser.add_argument(
        '-d', '--date',
        help='Date that the groups will be meeting in YYYYMMDD format'
    )
    parser.add_argument(
        '-p', '--print',
        action='store_true',
        dest='printit',
        help='Send the information to the default printer'
    )
    parser.add_argument(
        '-s', '--size',
        help='Size of the groups to aim for.\nDo not use with -n',
        type=int,
        dest='groupsize'
    )
    parser.add_argument(
        '-n', '--number-of-groups',
        help='Number of groups to make.\nDo not use with -s',
        type=int,
        dest='numberofgroups'
    )
    parser.add_argument(
        '-v', '--verbose',
        help='Lots of stuff gets printed out',
        action='store_true',
        dest='verbose'
    )
    args = parser.parse_args()

    if args.groupsize and args.numberofgroups:
        print("Don't give options for both -s and -n.\n")
        parser.print_help()
        sys.exit()

    if args.verbose:
        verbose = True
    else:
        verbose = False

    if args.infile:
        infile = args.infile
    else:
        infile = 'students.txt'

    with open(infile, 'r') as f:
        students = f.readlines()

    if args.date:
        date = args.date
        if not validdate(date):
            print("Invalid date.")
            parser.print_help()
            sys.exit()
    else:
        date = datetime.date.today().strftime("%Y%m%d")

    if args.outfile:
        outfile = args.outfile
    else:
        outfile = date+'.txt'

    if args.groupsize:
        groupsize = args.groupsize
    else:
        groupsize = 3

    if args.numberofgroups:
        numberofgroups = args.numberofgroups
    else:    
        numberofstudents = len(students)
        numberofgroups = numberofstudents//groupsize

    # fix in case groupsize > numberofgroups
    if numberofgroups == 0:
        numberofgroups = 1

    groups = {n: [] for n in range(numberofgroups)}

    # randomize the list
    shuffle(students)
    if verbose:
        print()
        print("Read names from %s" % infile)
        print("Dividing the students into %d groups of roughly %d size each" % (numberofgroups, groupsize))
        print("Saving groups to %s" % outfile)
        print("")

    n = 0
    # separate into groups
    while len(students) > 0:
        groups[n].append(students.pop(0))
        n = (n+1) % numberofgroups

    with open(outfile, 'w') as f:
        for key, value in groups.items():
            if verbose:
                print("Group", key)
            f.write("Group "+str(key)+"\n")
            for x in value:
                f.write(x)
                if verbose:
                    print(x.strip())
            f.write("\n")
            if verbose:
                print("")

    if args.printit:
        if verbose:
            print("Sending to the printer...")
        sendtoprinter(outfile)

    print("Saved groups to %s" % outfile)


if __name__ == '__main__':
    main()
    sys.exit()
