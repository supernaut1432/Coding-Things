largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        ent_num = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = ent_num
        continue
    if smallest is None:
        smallest = ent_num
        continue
    if ent_num > largest:
        largest = ent_num
        continue
    if ent_num < smallest:
        smaller = ent_num
        continue


print("Maximum is", largest)
print("Minimum is", smallest)
