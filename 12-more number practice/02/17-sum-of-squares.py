# Given n, compute sum of squares.
def function(n):
    sq = []
    sum = 0

    for i in range(1, n + 1):
        sqs = i ** 2
        sq.append(sqs)

    for j in sq:
        sum += j
    return sum

n = int(input("Enter your number: "))
print(function(n))