# Return the longest string (if tie, you can return first longest).
L = eval(input("Enter an array: "))
L2 = []

for i in L:
    length = len(i)
    L2.append(length)

n = max(L2)
index = L2.index(n)

print(L[index])