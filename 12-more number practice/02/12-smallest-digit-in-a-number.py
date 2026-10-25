# Given a number, return the smallest digit.
def function(n):
    smallest = 0

    while n > 0:
        digit = n % 10
        if digit < smallest:
            smallest = digit
        n //= 10
    print("Smallest digit:", smallest)
    
n = int(input("Enter a number: "))
function(n)