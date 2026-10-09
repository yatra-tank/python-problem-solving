# Write a function that returns the longer string. If equal, you can return the first.
def function(s1, s2):
    if len(s1) >= len(s2):
        return s1
    else:
        return s2

s1 = input("Enter a string: ")
s2 = input("Enter another string: ")
print(function(s1, s2))