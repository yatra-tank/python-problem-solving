# Sort an array using insertion sort.
L = [7, 3, 8, 2, 6, 4, 5]

for i in range(1, len(L)):
    key = L[i]
    j = i - 1

    while j >= 0 and L[j] > key:
        L[j + 1] = L[j]
        j -= 1

    L[j + 1] = key

print(L)