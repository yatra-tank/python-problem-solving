# Given n, print numbers from n down to 1.
def function(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

n = int(input("Enter a number: "))
function(n)