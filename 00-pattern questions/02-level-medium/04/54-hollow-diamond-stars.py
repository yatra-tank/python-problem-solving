n = int(input("Enter your number: "))

for i in range(1, n + 1):
        if i == 1:
            print( " "* n + "*")
        print(" " * (n - i) + "*" + " " * (2 * i - 1) + "*")
for i in range(n - 1, 0, -1):

        print(" " * (n - i) + "*" + " " * (2 * i - 1) + "*")
        if i == 1:
            print( " "* n + "*")