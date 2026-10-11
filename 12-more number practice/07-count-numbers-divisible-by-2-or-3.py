# Given n, count how many numbers between 1 and n are divisible by 2 or 3.
L = []

def function(n):
    sum = 0
    for i in range(1, n + 1):
        if i%2 != 0:
            L.append(i)

    for i in L:
        sum += i

    print(sum) 

n = int(input("Enter a number: "))
function(n)