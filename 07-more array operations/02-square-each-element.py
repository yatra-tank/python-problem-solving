# Given an array, return a new array with each element squared.
L = eval(input("Enter a list of numbers: "))
square = []

for i in L:
    square.append(i ** 2)
print(square)