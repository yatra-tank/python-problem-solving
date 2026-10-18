# Return the index of the minimum element (first min if multiple).
L = eval(input("Enter a list of numbers: "))

num = L[0]
index = 0

for i in range(1, len(L)):
    if L[i] < num:
        num = L[i]
        index = i

print(index)