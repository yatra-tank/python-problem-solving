# Given an array, return new array of absolute values.
L1 = eval(input("Enter a list of numbers: "))
L2 = []

for i in L1:
    if i < 0:
        L2.append(-(i))
    else:
        L2.append(i)

print(L2)