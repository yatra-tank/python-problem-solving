# Reorder array so that all negatives come before non-negatives (0 and positives). Order within groups can be ignored.
L = eval(input("Enter a list of numbers: "))
L1 = []
L2 = []

for i in L:
    if i < 0:
        L1.append(i)
    else:
        L2.append(i)

print(L1 + L2)