# Given an array, print only positive numbers.
L = eval(input("Enter a list of numbers: "))
for i in L:
    if i > 0:
        print(i, end=" ")