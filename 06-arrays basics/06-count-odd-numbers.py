# Given an array of integers, count odd numbers.
L = eval(input("Enter a list of numbers: "))
count = 0 
for i in L:
    if i%2 != 0:
        count += 1
print(count)