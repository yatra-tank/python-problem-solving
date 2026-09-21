n = int(input("Enter your number: "))
for i in range(n, 0, -1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")