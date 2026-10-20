# Given an array of strings, return array of their first characters.
L = eval(input("Enter a list of strings: "))
length = []

for i in L:
    for j in i:
        length.append(j[0])
        break

print(length)