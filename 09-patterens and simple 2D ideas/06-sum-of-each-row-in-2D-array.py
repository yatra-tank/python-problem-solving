# Given a 2D array, print sum of each row.
L = eval(input("Enter a 2D array: "))
result = []

for i in L:
    total = 0

    for j in i:
        total += j

    result.append(total)

print(result)