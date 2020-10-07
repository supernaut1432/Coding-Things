fname = input("Enter file: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)

tmail = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    times = line.split()[5]
    hour = times.split(':')[0]
    tmail[hour] = tmail.get(hour, 0) + 1

lst = list()
for k, v in list(tmail.items()):
    lst.append((k, v))

lst.sort()

for k, v in lst:
    print(k, v)
