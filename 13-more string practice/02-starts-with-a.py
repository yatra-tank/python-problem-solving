# Return true if string starts with 'a' or 'A'.
def function(s):
    if s[0] in 'aA':
        return "true"
    else:
        return "false"

s = input("Enter a string: ")
print(function(s))