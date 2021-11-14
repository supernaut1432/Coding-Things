import numpy

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
xy = x**y
l = int(numpy.log2(x))


print("x**y =", xy)
print("log(x) =", l)