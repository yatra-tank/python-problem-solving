# Given an array of numbers, find the average.
L = eval(input("Enter a list of numbers: "))
count = 0 
sum = sum(L)

for i in L:
        count += 1

print(sum/count)