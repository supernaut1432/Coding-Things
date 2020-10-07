import random
# 5 numbers between 1 and 50
# 2 numbers between 1 and 12
lnum = []
lstar = []

lnum_count = 0
lstar_count = 0
num = 0

while lnum_count < 5:
    num = random.randint(1, 50)
    if num in lnum:
        # print('Number already in')
        continue
    else:
        # print('Number not in')
        lnum_count = lnum_count + 1
        lnum.append(num)

while lstar_count < 2:
    lsnum = random.randint(1, 12)
    if lsnum in lstar:
        # print('Number already in')
        continue
    else:
        # print('Number not in')
        lstar_count = lstar_count + 1
        lstar.append(lsnum)

print('Lottery numbers:', lnum, 'Lucky Stars:', lstar)
