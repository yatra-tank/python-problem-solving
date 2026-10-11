# Given three numbers, return the smallest.
def function(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
    
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter third number: "))
print(function(a, b, c))