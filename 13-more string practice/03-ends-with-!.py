# Return true if string ends with exclamation mark.
def function(s):
    if s[-1] == "!":
        return "true"
    else:
        return "false"

s = input("Enter a string: ")
print(function(s))