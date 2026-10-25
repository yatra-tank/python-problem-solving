# Given n, compute sum of cubes.
def function(n):
    L = []
    sum = 0

    for i in range(1, n + 1):
        cube = i ** 3
        L.append(cube)

    for j in L:
        sum += j
    return sum

n = int(input("Enter your number: "))
print(function(n))