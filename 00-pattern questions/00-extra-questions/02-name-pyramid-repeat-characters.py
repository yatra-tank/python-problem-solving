n = input("Enter your name: ")
s = ' '

# for i in range(len(n) + 1):
#     print("   " * (len(n) - i), end="")
#     k = 0
#     for j in range(2 * i - 1):
#         print(s + n[k] + ' ', end="")
#         k = k + 1
#         if k == len(n):
#             k = 0
#     print(" ")

for i in range(len(n) + 1):
    print("   " * (len(n) - i), end="")
    for j in range(2 * i - 1):
        print(s + n[j % len(n)] + ' ', end="")
    print(" ")