n = int(input("Enter your number: "))
for i in range(n):
    count = 0
    for j in range(n - i):
        print(chr(65 + count), end=" ")
        count += 1
    print("")