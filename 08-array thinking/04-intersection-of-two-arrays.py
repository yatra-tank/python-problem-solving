# Return new array with elements present in both (no duplicates).
L1 = eval(input("Enter an array1: "))
L2 = eval(input("Enter an array2: "))

common = []

for i in L1:
    if i in L2 and i not in common:
        common.append(i)

print(common)