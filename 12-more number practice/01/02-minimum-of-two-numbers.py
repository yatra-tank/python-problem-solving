# Given two numbers, return the smaller one.
def function(a, b):
    if a < b:
        return a
    else:
        return b
    
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(function(a, b))