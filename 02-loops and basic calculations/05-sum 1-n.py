# Given N, find sum of numbers from 1 to N.
n = int(input("Enter a number: "))
sum = 0
for i in range(n + 1):
    sum = sum + i
print(sum)