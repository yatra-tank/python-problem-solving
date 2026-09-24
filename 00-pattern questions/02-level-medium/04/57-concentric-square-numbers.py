n = int(input("Enter your number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i > n // 2 + 1:
            i = n - i + 1
        if j > n // 2 + 1:
            j = n - j + 1
            
        if i < j:
            print(i, end=" ")
        else:
            print(j, end=" ")
    print()