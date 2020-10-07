fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)

# Histogram code
wdict = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for w in words:
        wdict[w] = wdict.get(w, 0) + 1

# Find the most common word
largest = -1
theword = None

for k, v in wdict.items():
    if v > largest:
        largest = v
        theword = k

print('Most is', theword, 'at', largest, 'times')
# print(k, v)
