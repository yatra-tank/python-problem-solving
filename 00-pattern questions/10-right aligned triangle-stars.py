n = int(input("Enter your number: "))
for i in range (n + 1):
    for j in range(n):
        print(" "*j +"*", end="")
    print("")