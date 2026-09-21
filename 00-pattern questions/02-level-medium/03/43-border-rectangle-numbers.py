row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
for i in range(1, row + 1):
    for j in range(1, col + 1):
        if i == 1 or i == row or j == 1 or j == col:
            print(j, end="")
        else:
            print(" ", end="")
    print()