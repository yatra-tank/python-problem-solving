# Given a number, count how many digits it has. (Ignore sign.)
n = int(input("Enter a number: " ))
if n < 0:
    n = -n
count = 0
while n > 0:
    count = count + 1
    n = n // 10  
print(count)

