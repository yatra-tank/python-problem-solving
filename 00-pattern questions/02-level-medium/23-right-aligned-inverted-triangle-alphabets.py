n = int(input("Enter a number: "))
for i in range(n + 1, 0, -1):
    print(" " * (n + 1 - i), end="")
    for j in range(1, i):
        print(chr(64 + j), end="")
    print()