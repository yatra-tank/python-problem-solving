# Return new array with all duplicates removed, using loops (not Set).
L = eval(input("Enter a list of numbers: "))
unique = []

for i in L:
    if i not in unique:
        unique.append(i)

print(unique)