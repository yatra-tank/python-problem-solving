# Write a function that returns true if string length is greater than 5.
def function(s):
    if len(s) > 5:
        return True
    else:
        return False

s = input("Enter a string: ")
print(function(s))