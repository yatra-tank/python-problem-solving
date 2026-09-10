# Print all prime numbers from 1 to N.
n = int(input("Enter a number: "))
for num in range(2, n + 1):
    factor = 2
    count = 0

    while factor <= num / 2:
        if num % factor == 0:
            count += 1
        factor += 1

    if count == 0:
        print(num, end=" ")