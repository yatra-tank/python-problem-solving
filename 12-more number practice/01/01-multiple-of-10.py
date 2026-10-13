# Given a number, check if it is a multiple of 10.
def function(n):
    if n%10 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))
print(function(n))