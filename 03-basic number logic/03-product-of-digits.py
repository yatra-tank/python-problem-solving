# Given a number, find product of its digits.
n = int(input("Enter a number: "))
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n = n//10
print(product)