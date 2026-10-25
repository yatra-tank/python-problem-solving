# A number is automorphic if its square ends with the same digits as the number.
def function(n):
    sq = n ** 2

    if sq%10 == n:
        return "true"
    else:
        return "false"

n = int(input("Enter your number: "))
print(function(n))