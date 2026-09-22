n = int(input("Enter a number:  "))
for i in range(1, n + 1):
    for j in range(n):
        value = (i + j) % 2
        print(value, end=" ")
    print()