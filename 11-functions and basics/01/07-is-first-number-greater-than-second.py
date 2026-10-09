# Write a function that takes two numbers and returns true if first > second.
def function(a, b):
    if a > b:
        return True
    else:
        return False

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(function(a, b))