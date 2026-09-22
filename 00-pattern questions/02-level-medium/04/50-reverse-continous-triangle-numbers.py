n = int(input("Enter your number: "))
count = n * (n + 1) // 2
for i in range (1, n + 1):
    for j in range(i, 0 , -1):
        print(count, end=" ")
        count -= 1
    print("  ")