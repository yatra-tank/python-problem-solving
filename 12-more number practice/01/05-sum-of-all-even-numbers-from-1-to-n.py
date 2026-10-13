# Given n, find sum of all even numbers from 1 to n.
L = []

def function(n):
    sum = 0
    for i in range(1, n + 1):
        if i%2 == 0:
            L.append(i)

    for i in L:
        sum += i

    print(sum) 

n = int(input("Enter a number: "))
function(n)