# Count how many numbers are greater than the average of array.
L = eval(input("Enter an array: "))

sum = 0
count = 0
greater = 0

for i in L:
    sum += i
    count += 1
avg = sum / count

for i in L:
    if i > avg:
        greater += 1
print(greater)