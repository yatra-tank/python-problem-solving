n = int(input("Enter your number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == n // 2 + 1:
            print(j, end="")
        elif j == n // 2 + 1:
            print(n//2 + 1, end="")
        else:
            print(" ", end="")
    print()