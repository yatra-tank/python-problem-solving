n = int(input("Enter your number: "))
count = 2
for i in range (1, n + 1):
    for j in range(1, i + 1):
        print(count, end=" ")
        count += 2
    print("")