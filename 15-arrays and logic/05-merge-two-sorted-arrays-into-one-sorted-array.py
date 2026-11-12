# Both arrays are sorted; merge into a single sorted array (without sorting at the end).
L1 = eval(input("Enter a list of numbers: "))
L2 = eval(input("Enter another list of numbers: "))
L3 = L1 + L2
n = len(L3)
for i in range(n):
    ok = True
    for j in range(n - i - 1):
        if L3[j] > L3[j + 1]:
            L3[j], L3[j + 1] = L3[j + 1], L3[j]
            ok = False
    if ok:
        break
print(L3)