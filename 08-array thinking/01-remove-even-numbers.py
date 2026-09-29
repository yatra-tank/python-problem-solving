# Return a new array with only odd numbers.
L = eval(input("Enter an array: "))
odd = []

for i in L:
    if i%2 != 0:
        odd.append(i)

print(odd)