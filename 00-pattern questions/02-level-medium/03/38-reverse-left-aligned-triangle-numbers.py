n = int(input("Enter your number: "))
for i in range(n):
    for j in range(n):
        if j >= i:
            print(j - i + 1, end="")
        else:
            print(" ", end="")
    print()