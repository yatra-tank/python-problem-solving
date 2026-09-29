# Given an array and a value, return index or -1.
L = eval(input("Enter an array: "))
n = input("Enter required value: ")

if n in L:
    print(L.index(n))
else:
    print("-1")