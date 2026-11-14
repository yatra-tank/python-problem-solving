# Find max possible sum of any contiguous subarray by checking all.
L = eval(input("Enter a list of numbers: "))
max = L[0]

for i in range(len(L)):
    sum = 0

    for j in range(i, len(L)):
        sum += L[j]
        if sum > max:
            max = sum

print(max)