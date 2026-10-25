# Return |a - b|.
def function(a, b):
    c = a - b
    if c > 0:
        return c
    else:
        return -c

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(function(a, b))