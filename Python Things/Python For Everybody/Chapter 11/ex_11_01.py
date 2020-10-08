import re

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = "regex_sum_42.txt"

fhand = open(fname)
nsum = 0

for line in fhand:
    numstr = re.findall('[0-9]+', line)
    for n in numstr:
        # print(n)
        no = int(n)
        nsum = nsum + no

print(nsum)
