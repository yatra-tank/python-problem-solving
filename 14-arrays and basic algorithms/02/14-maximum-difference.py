# Given array, find max - min.
L = eval(input("Enter a list of numbers: "))

max = L[0]
min = L[0]

for i in range(1, len(L)):
    if L[i] > max:
        max = L[i]

for i in range(1, len(L)):
    if L[i] < min:
        min = L[i]

print(max - min)