fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    # print(line.rstrip())
    words = line.split()
    for w in words:
        if w in lst:
            continue
        lst.append(w)

lst.sort()
print(lst)
