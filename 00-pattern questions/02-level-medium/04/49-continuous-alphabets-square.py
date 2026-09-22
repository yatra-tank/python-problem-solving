n = int(input("Enter your number: "))
count = 1
for i in range (1, n + 1):
    for j in range(1, n + 1):
        print(chr(64 + count), end=" ")
        count += 1
    print("")