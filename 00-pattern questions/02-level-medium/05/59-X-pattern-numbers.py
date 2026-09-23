n = int(input("Enter your number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i:
            print(i, end="")
        elif j == n - i + 1:
            print(n - i + 1, end="")
        else:
            print(" ", end="")
    print()