# Count how many times target value appears.
L = eval(input("Enter a list of numbers: "))
target = int(input("Enter a number: "))

count = 0

for i in L:
    if i == target:
        count += 1

print(count)