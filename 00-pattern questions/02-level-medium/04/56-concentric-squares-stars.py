n = int(input("Enter your number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or j == 1 or i == n or j == n:
            print("*", end=" ")
        elif i == n // 2 + 1 and j == n // 2 + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()