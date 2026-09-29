# Given array of strings, return array of lengths.
L = eval(input("Enter an array: "))
L2 = []

for i in L:
    length = len(i)
    L2.append(length)

print(L2)