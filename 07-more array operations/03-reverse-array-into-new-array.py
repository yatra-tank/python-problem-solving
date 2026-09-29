# Given an array, create a new array which is the reverse.
L = eval(input("Enter a list: "))
reverse = []

i = len(L) - 1

while i >= 0:
    reverse.append(L[i])
    i -= 1

print(reverse)