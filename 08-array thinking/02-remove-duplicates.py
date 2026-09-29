# Return a new array with unique elements (order can be original order).
L = eval(input("Enter an array: "))
unique = []

for i in L:
    if i not in unique:
        unique.append(i)

print(unique)