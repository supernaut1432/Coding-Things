# Use the file name mbox-short.txt as the filename
count = 0
csum = 0

fname = input('Enter file name: ')
fhand = open(fname)

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line.rstrip())
    count = count + 1
    cpos = line.find(':')
    ntex = line[cpos+1:]
    num = float(ntex)
    csum = csum + num

avg = csum / count

# print("Count", count)
# print("Confidence sum", csum)
print("Average spam confidence:", avg)
# print("Done.")
