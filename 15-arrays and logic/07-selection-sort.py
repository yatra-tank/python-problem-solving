# Sort an array using selection sort.
L = eval(input("Enter a list of numbers: "))

for i in range(len(L) - 1):
    m = i

    for j in range(i + 1, len(L)):
        if L[j] < L[m]:
            m = j

    L[i], L[m] = L[m], L[i]

print(L)