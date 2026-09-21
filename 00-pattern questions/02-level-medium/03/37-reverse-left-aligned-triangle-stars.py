n = int(input("Enter your number: "))
# for i in range(n):
#     print(" " * i + "*" * (n - i))

for i in range(n):
    for j in range(n):
        if j >= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
