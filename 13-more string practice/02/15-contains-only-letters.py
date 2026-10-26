# Return true if string has only a–z or A–Z (no digits, no spaces).
def function(s):
    if s == "":
        return "false"

    for i in s:
        if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
            return "false"

    return "true"


s = input("Enter a string: ")
print(function(s))