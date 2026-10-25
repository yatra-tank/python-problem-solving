# Given a number, return the largest digit.
def function(n):
    largest = 0

    while n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        n //= 10
    print("Largest digit:", largest)
    
n = int(input("Enter a number: "))
function(n)