# n = int(input("Enter your number: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i <= n // 2 + 1:
#             a = i
#         else:
#             a = n - i + 1
#         if j <= n // 2 + 1:
#             b = j
#         else:
#             b = n - j + 1
#         if a < b:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()

n = int(input("Enter your number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print(1, end=" ")
        else:
            if j < i:
                x = j
            else:
                x = i
            if n - 1 - i < x:
                x = n - 1 - i
            if n - 1 - j < x:
                x = n - 1 - j
            print(x + 1, end=" ")
    print()