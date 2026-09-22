n = int(input("Enter your number: "))
count = 1
for i in range(1, n + 1):
    print("  " * (n - i), end=" ")
    for j in range(1, 2 * i):
        print(count, end=" ")
        count += 1
    print(" ")