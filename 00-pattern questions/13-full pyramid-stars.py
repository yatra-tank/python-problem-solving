n = int(input("Enter your number: "))
for i in range(1, n + 1):
    print("*" * (n - i), end=" ")
    if i%2 != 0:
        for j in range(i):
            print(i, end=" ")
    print(" ")