# Count how many numbers between 1 and N are divisible by 3.
n = int(input("Enter a number: "))
count = 0
for i in range(1, n+1):
    if i%3 == 0:
        count =count + 1
print(count)