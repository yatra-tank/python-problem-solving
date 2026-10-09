# Write a function that returns true if number is odd, false otherwise. 
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))
print(is_odd(n))