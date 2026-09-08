# n = int(input("Enter your number: "))
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print("")

n = int(input("Enter your number: "))
count = 1
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(count):
        print("*", end="")
    print()
    count += 2
