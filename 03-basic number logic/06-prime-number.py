# Given a number, check if it is prime.
n = int(input("Enter a number: "))
count = 0
factor = 1
while factor <= n:
    if n % factor == 0:
        count += 1
    factor += 1

if count == 2:
    print("prime")
else:
    print("not prime")