# assigngroups

In many of my classes, I have the students work together on some activities.
Usually, I want them sorted into groups of about 3 or 4, but I don't want them
only working with their friends or neighbors each time. I'd rather they work in
different groups each time. Hence, this program.

This script will read in the roster for the class from a text file and randomly
assign them into groups. The user can either specify the groups size to aim
for, or the number of groups total to use (but not both). The results are saved
to a text file. Optionally, the groups are displayed on the screen or sent
directly to the printer.

Included is a dummy file `students.txt` which contains 25 names. The names were
themselves randomly generated.

By default, the groups are saved to a text file of the form `YYYYMMDD.txt`
using the current date. If the `-d` option is set, then the date the class
meets (or whatever) can be set instead. If the `-o` option is set, then the
data gets saved to the specified file.

# usage
```
usage: assigngroups [-h] [-i INFILE] [-o OUTFILE] [-d DATE] [-p]
                    [-s GROUPSIZE] [-n NUMBEROFGROUPS] [-v]

Creates randomly assigned groups of students of similar sizes

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --in-file INFILE
                        Name of the file containing the class roster
  -o OUTFILE, --out-file OUTFILE
                        Name of the file to write the groups to
  -d DATE, --date DATE  Date that the groups will be meeting in YYYYMMDD
                        format
  -p, --print           Send the information to the default printer
  -s GROUPSIZE, --size GROUPSIZE
                        Size of the groups to aim for. Do not use with -n
  -n NUMBEROFGROUPS, --number-of-groups NUMBEROFGROUPS
                        Number of groups to make. Do not use with -s
  -v, --verbose         Lots of stuff gets printed out
```

