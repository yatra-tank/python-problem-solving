# Write a function that returns the average of three numbers.
def function(a, b, c):
    avg = (a + b + c)/3
    return avg

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter third number: "))
print(function(a, b, c))