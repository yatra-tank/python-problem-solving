n = int(input("Enter a number:  "))
for i in range(n):
    for j in range(1, i + 2):
        value = (i + j) % 2
        print(value, end=" ")
    print()