# Given array and number k, count how many elements are strictly greater than k.
L = eval(input("Enter a list of numbers: "))
k = int(input("Enter a number: "))
count = 0

for i in L:
    if i > k:
        count += 1

print(count)