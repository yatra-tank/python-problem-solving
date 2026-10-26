# Return true if the string contains at least one vowel (a, e, i, o, u, case-insensitive).
def function(s):
    for i in s:
        if i in 'aeiouAEIOU':
            return "true"
    else:
        return "false"

s = input("Enter a string: ")
print(function(s))