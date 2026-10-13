# A perfect number equals the sum of its proper divisors (excluding itself).
def function(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    if sum == n:
        print("true")
    else:
        print("false")

n = int(input("Enter a number: "))
function(n)