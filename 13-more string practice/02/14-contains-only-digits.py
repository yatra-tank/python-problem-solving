# Return true if every character is 0–9 and string is not empty.
def function(s):
    if s == "":
        return "false"

    for i in s:
        if i not in '0123456789':
            return "false"

    return "true"

s = input("Enter a string: ")
print(function(s))