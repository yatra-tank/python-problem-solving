# A number is Harshad if it’s divisible by sum of its digits.
def function(n):
    sum = 0
    k = n

    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10

    if k%sum == 0:
        return "true"
    else:
        return "false"

n = int(input("Enter your number: "))
print(function(n))