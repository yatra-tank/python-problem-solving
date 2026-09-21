n = int(input("Enter your number: "))
for i in range(1, n + 1): 
    count = 1
    print("   " * (n - i), end=" ")
    for j in range(i):
        print(count + j, end="  ")
    print("")