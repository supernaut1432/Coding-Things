fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

cmail = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()[1]
    cmail[words] = cmail.get(words, 0) + 1

mostCommon = 0
emailaddy = None

for k, v in cmail.items():
    if v > mostCommon:
        mostCommon = v
        emailaddy = k

print(emailaddy, mostCommon)
