n = int(input("Enter a number: "))
mid = n // 2
for i in range(n):
    if i == mid:
        print("*" * n)
    else:
        print(" " * mid + "*")