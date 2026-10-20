# Return new array with elements at indices 1, 3, 5, …
L1 = eval(input("Enter a list of numbers: "))
L2 = []

for i in range(len(L1)):
    if i % 2 != 0:
        L2.append(L1[i])

print(L2)