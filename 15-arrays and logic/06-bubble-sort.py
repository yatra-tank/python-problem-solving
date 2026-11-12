# Sort an array using bubble sort algorithm.
L = eval(input("Enter a list of numbers: "))
n = len(L)

for i in range(n):
    ok = True
    for j in range(n - i - 1):
        if L[j] > L[j + 1]:
            L[j], L[j +1] = L[j + 1], L[j]
            ok = False

    if ok:
        break

print(L)