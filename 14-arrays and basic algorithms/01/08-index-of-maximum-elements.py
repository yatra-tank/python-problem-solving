# Return the index of the maximum element (first max if multiple).
L = eval(input("Enter a list of numbers: "))

num = L[0]
index = 0

for i in range(1, len(L)):
    if L[i] > num:
        num = L[i]
        index = i

print(index)