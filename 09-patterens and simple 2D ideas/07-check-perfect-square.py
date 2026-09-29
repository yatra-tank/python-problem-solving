# Return true if number is a perfect square.
n = int(input("Enter a number: "))
flag = False

for i in range(1, n + 1):
    if i * i == n:
        flag = True
        break

if flag:
    print("true")
else:
    print("false")