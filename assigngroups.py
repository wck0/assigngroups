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
from time import strftime
import subprocess # for printing

# list of students names as strings
students = [
            'Noah Carson',
            'Brandon Tyler',
            'Donald Jacobs',
            'Nichole Cruz',
            'Ella Curtis',
            'Antonio Boone',
            'Victor Davis',
            'Milton Vasquez',
            'Kathleen Bradley',
            'Lola Simmons',
            'Teresa Patton',
            'Jody Copeland',
            'Sandra Glover',
            'Terri Powers',
            'Johnnie Tucker',
            'Christian Montgomery',
            'Shari Meyer',
            'Marilyn Lindsey',
            'Angie Olson',
            'Marlene Jimenez',
            'Gary Freeman',
            'Violet Graves',
            'Edwin Tran',
            'Leticia Dawson',
            'Brendan Nguyen'
           ]

groupsize = 3 # how many people in each group
numberofstudents = len(students)
numberofgroups = numberofstudents/groupsize

groups = {n:[] for n in range(numberofgroups)}

shuffle(students) # randomize the list

n=0
# separate into groups
while len(students) > 0:
    groups[n].append(students.pop(0))
    n = (n+1)%numberofgroups

# txt file to save to
today = strftime("%Y%m%d")
f = open(today+".txt", 'w')


# print them out and save to txt file
for key in groups.keys():
    print "Group", key
    f.write("Group "+str(key)+"\n")
    for x in groups[key]:
        f.write(x+"\n")
        print x
    f.write("\n")
    print ""

# close the txt file    
f.close()

# open the txt file for reading
f = open(today+".txt", 'r')

# print the txt file
# code taken from 
# http://stackoverflow.com/questions/12723818/print-to-standard-printer-from-python
lpr = subprocess.Popen("/usr/bin/lpr", stdin = subprocess.PIPE)
lpr.stdin.write(f.read())

# close the txt file again
f.close()

print "Done. Go check the printer."
